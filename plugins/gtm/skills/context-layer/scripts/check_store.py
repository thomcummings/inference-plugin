#!/usr/bin/env python3
"""Check a git/markdown GTM context store against its conventions.

Read-only. Reports frontmatter gaps, invalid values, slugs that don't match
their path, duplicate slugs, rows past their freshness window, expired proof
and registry trials past their review date.

Usage:
    python3 check_store.py STORE_ROOT [--as-of YYYY-MM-DD] [--json] [--strict]
                           [--export ROWS.jsonl]

--strict exits 1 when any finding exists (for CI). --export writes one JSON
line per row (slug, path, frontmatter, body) for building a search index;
the index is derived and never written back. Standard library only.
"""

import argparse
import datetime as dt
import json
import os
import re
import sys

SECTION_PREFIX = {
    "01-context": "core",
    "02-memory": "memory",
    "03-agent-ops": "ops",
    "04-manual": "infra",
}
STATUS = {"canonical", "working", "stub", "archived"}
STAGE = {"proposed", "active", "superseded", "archived", "draft", "final"}
REGISTRY_STATUS = {"draft", "trial", "active", "degraded", "dormant", "retired"}
REGISTRY_KIND = {"agent", "skill", "routine"}
RUN_RESULT = {"success", "partial", "failed", "blocked"}
NEEDS_DECISION = "[NEEDS DECISION]"


def parse_frontmatter(text):
    """Parse a simple YAML frontmatter block: scalars and [inline, lists]."""
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if value and value[0] not in "\"'":
            value = re.split(r"\s+#", value, maxsplit=1)[0].strip()
        if value.startswith("[") and value.endswith("]"):
            items = [v.strip().strip("\"'") for v in value[1:-1].split(",")]
            data[key.strip()] = [v for v in items if v]
        else:
            data[key.strip()] = value.strip("\"'")
    return None  # no closing ---


def parse_date(value):
    try:
        return dt.date.fromisoformat(str(value)[:10])
    except (TypeError, ValueError):
        return None


def freshness_window(slug):
    if "/competitive/battlecards/" in slug:
        return 90
    if slug.startswith(("core/operations/", "core/active/", "core/team/")) or "/market-signals" in slug:
        return 90
    if slug.startswith("core/foundations/") or slug.startswith("core/proof/"):
        return 365
    return 180


def expected_slug(rel_path):
    parts = rel_path.replace(os.sep, "/").split("/")
    if parts[0] == "00-start-here":
        return "infra/start-here"
    prefix = SECTION_PREFIX.get(parts[0])
    if not prefix:
        return None
    rest = "/".join(parts[1:])
    return f"{prefix}/{rest[:-3]}" if rest.endswith(".md") else None


def check(root, as_of):
    findings = []
    slugs = {}
    covered = 0

    def add(tier, check_name, path, evidence):
        findings.append({"tier": tier, "check": check_name, "row": path, "evidence": evidence})

    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith((".", "_")))
        for name in sorted(filenames):
            if not name.endswith(".md") or name == "README.md":
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root)
            section = rel.replace(os.sep, "/").split("/")[0]
            if section not in SECTION_PREFIX and section != "00-start-here":
                continue
            covered += 1
            try:
                with open(full, encoding="utf-8") as fh:
                    fm = parse_frontmatter(fh.read())
            except (OSError, UnicodeDecodeError) as exc:
                add(1, "unreadable", rel, str(exc))
                continue
            if fm is None:
                add(2, "no frontmatter", rel, "missing or unclosed --- block")
                continue

            if section == "03-agent-ops":
                rel_posix = rel.replace(os.sep, "/")
                key = f"ops/{rel_posix.split('/', 1)[1][:-3]}"
                if "/registry/" in rel_posix:
                    check_registry(fm, rel, as_of, add)
            else:
                key = fm.get("slug")
                exp = expected_slug(rel)
                if not key:
                    add(2, "slug missing", rel, f"expected {exp}")
                elif exp and key != exp:
                    add(2, "slug does not match path", rel, f"slug {key}, path implies {exp}")

            if key:
                slugs.setdefault(key, []).append(rel)

            if section == "01-context":
                check_context(fm, rel, as_of, add)
            elif section == "02-memory":
                check_memory(fm, rel, add)

    for slug, paths in slugs.items():
        if len(paths) > 1:
            add(1, "duplicate slug", ", ".join(paths), slug)

    findings.sort(key=lambda f: (f["tier"], f["check"], f["row"]))
    return findings, covered


def check_context(fm, rel, as_of, add):
    status = fm.get("status")
    if status not in STATUS:
        add(2, "invalid status", rel, f"status {status!r}; allowed {sorted(STATUS)}")
    for field in ("owner", "last_reviewed", "source"):
        if not fm.get(field):
            add(2, f"{field} missing", rel, "required on every Context row")
    if fm.get("owner") == NEEDS_DECISION:
        add(2, "owner needs decision", rel, NEEDS_DECISION)
    if status == "archived":
        return
    if status == "stub":
        add(2, "stub", rel, "empty scaffold")
    slug = fm.get("slug", "")
    reviewed = parse_date(fm.get("last_reviewed"))
    window = freshness_window(slug)
    if reviewed is None:
        add(1 if status == "canonical" else 2, "stale", rel, "no valid last_reviewed date")
    elif (as_of - reviewed).days > window:
        tier = 1 if status == "canonical" else 2
        add(tier, "stale", rel, f"last_reviewed {reviewed}, window {window} days")
    expires = parse_date(fm.get("expires"))
    if expires and expires < as_of and status == "canonical":
        add(1, "expired proof still canonical", rel, f"expires {expires}")


def check_memory(fm, rel, add):
    rel_posix = rel.replace(os.sep, "/")
    if "/runs/" in rel_posix:
        if fm.get("result") not in RUN_RESULT:
            add(2, "run result missing or invalid", rel, f"result {fm.get('result')!r}")
        return
    stage = fm.get("stage")
    if stage not in STAGE:
        add(2, "invalid stage", rel, f"stage {stage!r}")
    if "status" in fm:
        add(2, "status on a Memory row", rel, "Memory rows use stage, not status")
    if not re.search(r"/(decisions|reports)/\d{4}-\d{2}-\d{2}-", rel_posix) and "/learnings/" not in rel_posix:
        add(4, "undated memory row", rel, "decisions and reports start YYYY-MM-DD-")


def check_registry(fm, rel, as_of, add):
    if not fm.get("name"):
        add(2, "registry name missing", rel, "kebab-case name required")
    if fm.get("kind") not in REGISTRY_KIND:
        add(3, "registry kind invalid", rel, f"kind {fm.get('kind')!r}")
    status = fm.get("status")
    if status not in REGISTRY_STATUS:
        add(3, "registry status invalid", rel, f"status {status!r}")
    if not fm.get("owner") or fm.get("owner") == NEEDS_DECISION:
        add(3, "registry owner missing", rel, fm.get("owner") or "empty")
    if status == "trial":
        review = parse_date(fm.get("review_date"))
        if review is None:
            add(3, "trial without review date", rel, "review_date required at trial")
        elif review < as_of:
            add(3, "trial past review date", rel, f"review_date {review}")


def export_rows(root, out_path):
    """Write one JSON line per row in the numbered sections. Read-only on the store."""
    count = 0
    with open(out_path, "w", encoding="utf-8") as out:
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames if not d.startswith((".", "_")))
            for name in sorted(filenames):
                if not name.endswith(".md") or name == "README.md":
                    continue
                full = os.path.join(dirpath, name)
                rel = os.path.relpath(full, root).replace(os.sep, "/")
                section = rel.split("/")[0]
                if section not in SECTION_PREFIX and section != "00-start-here":
                    continue
                try:
                    with open(full, encoding="utf-8") as fh:
                        text = fh.read()
                except (OSError, UnicodeDecodeError):
                    continue
                fm = parse_frontmatter(text) or {}
                body = text
                if text.startswith("---"):
                    parts = text.split("\n---", 2)
                    body = parts[1].split("\n", 1)[1] if len(parts) > 1 and "\n" in parts[1] else ""
                slug = fm.get("slug") or expected_slug(rel) or rel[:-3]
                out.write(json.dumps({"slug": slug, "path": rel, "frontmatter": fm, "body": body.strip()}) + "\n")
                count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root")
    parser.add_argument("--as-of", default=dt.date.today().isoformat())
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--export", metavar="ROWS.jsonl")
    args = parser.parse_args()

    as_of = parse_date(args.as_of)
    if as_of is None or not os.path.isdir(args.root):
        sys.exit("usage: check_store.py STORE_ROOT [--as-of YYYY-MM-DD]")

    if args.export:
        n = export_rows(args.root, args.export)
        print(f"Exported {n} rows to {args.export}", file=sys.stderr)

    findings, covered = check(args.root, as_of)
    if args.json:
        print(json.dumps({"as_of": str(as_of), "rows_checked": covered, "findings": findings}, indent=2))
    else:
        tiers = {t: sum(1 for f in findings if f["tier"] == t) for t in (1, 2, 3, 4)}
        print(f"# Store check, {as_of}\n")
        print(f"Rows checked: {covered}. Findings: " + " · ".join(f"tier {t}: {n}" for t, n in tiers.items()) + "\n")
        if findings:
            print("| Tier | Check | Row | Evidence |\n| --- | --- | --- | --- |")
            for f in findings:
                print(f"| {f['tier']} | {f['check']} | `{f['row']}` | {f['evidence']} |")
        print("\nThis checks frontmatter against the conventions. It does not prove content is true.")
    sys.exit(1 if args.strict and findings else 0)


if __name__ == "__main__":
    main()
