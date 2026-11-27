#!/usr/bin/env python3
"""Trigger evaluation for an installed skill.

Runs a set of labelled queries through `claude -p` and reports, per query,
how often the target skill was consulted. Because the skills are really
installed, a miss also records which neighbour fired instead — which is
usually the more useful finding.

Usage:
    python3 trigger_eval.py --skill ops:skill-design --eval-set queries.json

Eval set format (a JSON list):
    [
      {"query": "turn my proposal process into a skill", "should_trigger": true},
      {"query": "run this brief every Monday morning",    "should_trigger": false}
    ]

Requires the `claude` CLI on PATH and the skill installed in the environment
the CLI runs in. No third-party dependencies.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

TRIGGER_THRESHOLD = 0.5


def bare(skill_id: str) -> str:
    """'ops:skill-design' -> 'skill-design'."""
    return skill_id.split(":")[-1].strip()


def skills_from_event(event: dict) -> list[str]:
    """Return any skill identifiers a stream event shows being consulted."""
    if event.get("type") != "assistant":
        return []
    found = []
    for item in event.get("message", {}).get("content", []):
        if item.get("type") != "tool_use":
            continue
        name = item.get("name", "")
        args = item.get("input", {}) or {}
        if name == "Skill":
            value = args.get("skill") or args.get("command") or ""
            if value:
                found.append(str(value))
        elif name == "Read":
            path = str(args.get("file_path", ""))
            if path.endswith("SKILL.md"):
                found.append(Path(path).parent.name)
    return found


def run_once(query: str, target: str, model: str | None, timeout: int,
             patience: int) -> tuple[bool, list[str]]:
    """Run one query. Returns (target_fired, all_skills_seen).

    Stops as soon as the target fires, or after `patience` assistant turns
    without it — skills are consulted early, so a later hit is not the
    triggering behaviour being measured.
    """
    cmd = ["claude", "-p", query, "--output-format", "stream-json", "--verbose"]
    if model:
        cmd += ["--model", model]

    # The CLAUDECODE guard exists for interactive terminal conflicts; nesting
    # a non-interactive `claude -p` inside a session is safe.
    env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}

    seen: list[str] = []
    turns = 0
    target_bare = bare(target)

    process = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, env=env, text=True
    )
    try:
        for line in process.stdout:  # type: ignore[union-attr]
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            hits = skills_from_event(event)
            if hits:
                seen.extend(hits)
                if any(bare(h) == target_bare for h in hits):
                    return True, seen

            if event.get("type") == "assistant":
                turns += 1
                if turns >= patience:
                    return False, seen
            if event.get("type") == "result":
                return False, seen
    except Exception as exc:  # noqa: BLE001 - a failed run is a data point
        print(f"  warning: run failed ({exc})", file=sys.stderr)
    finally:
        if process.poll() is None:
            process.kill()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                pass
    return False, seen


def evaluate(eval_set: list[dict], target: str, runs: int, workers: int,
             model: str | None, timeout: int, patience: int) -> dict:
    jobs = [(item, i) for item in eval_set for i in range(runs)]
    results: dict[str, dict] = {}

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(run_once, item["query"], target, model, timeout, patience): item
            for item, _ in jobs
        }
        for future in as_completed(futures):
            item = futures[future]
            key = item["query"]
            record = results.setdefault(
                key,
                {"query": key, "should_trigger": bool(item["should_trigger"]),
                 "fired": [], "others": []},
            )
            try:
                fired, seen = future.result()
            except Exception as exc:  # noqa: BLE001
                print(f"  warning: {exc}", file=sys.stderr)
                fired, seen = False, []
            record["fired"].append(fired)
            record["others"].extend(
                s for s in seen if bare(s) != bare(target)
            )

    rows = []
    for record in results.values():
        rate = sum(record["fired"]) / max(len(record["fired"]), 1)
        triggered = rate >= TRIGGER_THRESHOLD
        rows.append({
            "query": record["query"],
            "should_trigger": record["should_trigger"],
            "trigger_rate": round(rate, 2),
            "triggered": triggered,
            "correct": triggered == record["should_trigger"],
            "other_skills": sorted(set(record["others"])),
        })

    positives = [r for r in rows if r["should_trigger"]]
    negatives = [r for r in rows if not r["should_trigger"]]
    true_pos = sum(1 for r in positives if r["triggered"])
    false_pos = sum(1 for r in negatives if r["triggered"])

    summary = {
        "skill": target,
        "runs_per_query": runs,
        "queries": len(rows),
        "accuracy": round(sum(1 for r in rows if r["correct"]) / max(len(rows), 1), 3),
        "recall": round(true_pos / len(positives), 3) if positives else None,
        "precision": round(true_pos / max(true_pos + false_pos, 1), 3) if positives else None,
        "misses": [r["query"] for r in positives if not r["triggered"]],
        "false_fires": [r["query"] for r in negatives if r["triggered"]],
    }
    return {"summary": summary, "results": sorted(rows, key=lambda r: (r["correct"], r["query"]))}


def report(data: dict) -> None:
    s = data["summary"]
    print(f"\n{s['skill']} — {s['queries']} queries x {s['runs_per_query']} runs")
    print(f"accuracy {s['accuracy']}   recall {s['recall']}   precision {s['precision']}\n")

    for row in data["results"]:
        mark = "ok  " if row["correct"] else "FAIL"
        want = "should" if row["should_trigger"] else "should NOT"
        print(f"{mark} [{row['trigger_rate']:.2f}] {want} — {row['query'][:88]}")
        if not row["correct"] and row["other_skills"]:
            print(f"       fired instead: {', '.join(row['other_skills'])}")

    if s["misses"]:
        print(f"\n{len(s['misses'])} miss(es): the description does not reach these phrasings.")
    if s["false_fires"]:
        print(f"{len(s['false_fires'])} false fire(s): the boundary clause is too weak.")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--skill", required=True,
                        help="Installed skill ID, e.g. ops:skill-design")
    parser.add_argument("--eval-set", required=True, type=Path,
                        help="JSON list of {query, should_trigger}")
    parser.add_argument("--runs", type=int, default=3,
                        help="Runs per query; triggering is stochastic (default 3)")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--model", default=None,
                        help="Model ID; use the one the principal actually runs")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--patience", type=int, default=3,
                        help="Assistant turns to wait before calling it a no-trigger")
    parser.add_argument("--out", type=Path, default=None, help="Write results JSON here")
    args = parser.parse_args()

    eval_set = json.loads(args.eval_set.read_text())
    if not isinstance(eval_set, list) or not eval_set:
        print("eval set must be a non-empty JSON list", file=sys.stderr)
        return 1
    for item in eval_set:
        if "query" not in item or "should_trigger" not in item:
            print(f"malformed entry: {item}", file=sys.stderr)
            return 1

    data = evaluate(eval_set, args.skill, args.runs, args.workers,
                    args.model, args.timeout, args.patience)
    report(data)
    if args.out:
        args.out.write_text(json.dumps(data, indent=2))
        print(f"written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
