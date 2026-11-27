#!/usr/bin/env python3
"""Build or refresh an IMSM client model from diagnostic response JSON files."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parent.parent
MAPPING_PATH = SKILL_DIR / "references" / "diagnostic-v1-mapping.json"

ORDINALS = {
    "ad_hoc": 1,
    "early": 2,
    "working": 3,
    "strong": 4,
    "unknown": None,
    "not_applicable": None,
}
ORDINAL_TO_CONDITION = {1: "ad_hoc", 2: "early", 3: "working", 4: "strong"}
# Display labels for the internal condition codes. Codes are kept stable
# (ad_hoc/early/working/strong = the questionnaire's native ordinal-1..4 values);
# only the human-facing label changes. The ladder is an L1-L4 maturity scale:
#   ad_hoc  -> L1 Ad hoc   (reactive/by default; not absent)
#   early   -> L2 Activated (switched on: a deliberate start exists, minimal/unproven)
#   working -> L3 Adept     (done well and dependably; skilled and fluent)
#   strong  -> L4 Adaptive  (learns and evolves, with humans in the right places)
CONDITION_LABELS = {
    "ad_hoc": "L1 · Ad hoc",
    "early": "L2 · Activated",
    "working": "L3 · Adept",
    "strong": "L4 · Adaptive",
    "unknown": "Unknown",
    "not_applicable": "Not applicable",
}


def condition_label(value: Any) -> str:
    if not value:
        return "Unresolved"
    return CONDITION_LABELS.get(value, str(value))
ALLOWED_SCHEMA_VERSIONS = {"ims-diagnostic-response-v1"}


class DiagnosticError(ValueError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise DiagnosticError(f"Input does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise DiagnosticError(f"Invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise DiagnosticError(f"Expected a JSON object in {path}")
    return data


def load_mapping() -> dict[str, Any]:
    return read_json(MAPPING_PATH)


def require_string(data: dict[str, Any], key: str, source: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise DiagnosticError(f"{source}: missing non-empty string '{key}'")
    return value


def normalize_condition(value: Any, aliases: dict[str, str], source: str) -> str:
    if not isinstance(value, str):
        raise DiagnosticError(f"{source}: condition must be a string")
    normalized = aliases.get(value, value)
    if normalized not in ORDINALS:
        allowed = ", ".join(sorted(set(ORDINALS) | set(aliases)))
        raise DiagnosticError(f"{source}: unsupported condition '{value}' (allowed: {allowed})")
    return normalized


def validate_and_normalize_response(
    payload: dict[str, Any], mapping: dict[str, Any], source_path: Path
) -> dict[str, Any]:
    source = str(source_path)
    schema_version = require_string(payload, "schemaVersion", source)
    if schema_version not in ALLOWED_SCHEMA_VERSIONS:
        raise DiagnosticError(f"{source}: unsupported schemaVersion '{schema_version}'")

    assessment_id = require_string(payload, "assessmentId", source)
    response_id = require_string(payload, "responseId", source)
    questionnaire_version = require_string(payload, "questionnaireVersion", source)
    completed_at = require_string(payload, "completedAt", source)

    company = payload.get("company")
    respondent = payload.get("respondent")
    answers = payload.get("answers")
    if not isinstance(company, dict):
        raise DiagnosticError(f"{source}: company must be an object")
    if not isinstance(respondent, dict):
        raise DiagnosticError(f"{source}: respondent must be an object")
    if not isinstance(answers, list):
        raise DiagnosticError(f"{source}: answers must be an array")
    require_string(respondent, "role", source)

    normalized_answers: list[dict[str, Any]] = []
    seen_questions: set[str] = set()
    for index, answer in enumerate(answers):
        answer_source = f"{source}: answers[{index}]"
        if not isinstance(answer, dict):
            raise DiagnosticError(f"{answer_source} must be an object")
        question_id = require_string(answer, "questionId", answer_source)
        if question_id in seen_questions:
            raise DiagnosticError(f"{source}: duplicate questionId '{question_id}'")
        seen_questions.add(question_id)

        original_condition = require_string(answer, "condition", answer_source)
        condition = normalize_condition(
            original_condition, mapping.get("condition_aliases", {}), answer_source
        )
        expected = mapping.get("questions", {}).get(question_id)
        component = require_string(answer, "component", answer_source)
        if expected and component != expected["component"]:
            raise DiagnosticError(
                f"{answer_source}: component '{component}' does not match mapping "
                f"'{expected['component']}' for {question_id}"
            )

        normalized_answers.append(
            {
                "question_id": question_id,
                "component": component,
                "original_condition": original_condition,
                "condition": condition,
                "ordinal": ORDINALS[condition],
                "question_version": str(answer.get("questionVersion", "unknown")),
                "question_copy": str(answer.get("questionCopy", question_id)),
                "answer_copy": str(answer.get("answerCopy", "")),
            }
        )

    context = payload.get("context") if isinstance(payload.get("context"), dict) else {}
    presenting = payload.get("presentingProblems", [])
    if not isinstance(presenting, list) or not all(isinstance(item, str) for item in presenting):
        raise DiagnosticError(f"{source}: presentingProblems must be an array of strings")

    return {
        "source_path": source_path,
        "raw": payload,
        "schema_version": schema_version,
        "questionnaire_version": questionnaire_version,
        "assessment_id": assessment_id,
        "response_id": response_id,
        "started_at": payload.get("startedAt"),
        "completed_at": completed_at,
        "company": company,
        "respondent": respondent,
        "presenting_problems": presenting,
        "context": context,
        "answers": normalized_answers,
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def preserve_source(input_path: Path, response_id: str, source_dir: Path) -> Path:
    source_dir.mkdir(parents=True, exist_ok=True)
    target = source_dir / f"{response_id}.json"
    if target.exists():
        if sha256(target) != sha256(input_path):
            raise DiagnosticError(
                f"A different source already exists for responseId '{response_id}': {target}"
            )
        return target
    shutil.copy2(input_path, target)
    return target


def lower_median(values: list[int]) -> int | None:
    if not values:
        return None
    ordered = sorted(values)
    return ordered[(len(ordered) - 1) // 2]


def derive_capability(respondent_assessments: list[dict[str, Any]]) -> dict[str, Any]:
    known = [item for item in respondent_assessments if item["ordinal"] is not None]
    unknown_count = sum(item["condition"] == "unknown" for item in respondent_assessments)
    na_count = sum(item["condition"] == "not_applicable" for item in respondent_assessments)

    if len(respondent_assessments) == 1:
        only = respondent_assessments[0]
        if only["condition"] == "unknown":
            return {"condition": None, "condition_range": [], "state": "unknown", "confidence": "low"}
        if only["condition"] == "not_applicable":
            return {
                "condition": None,
                "condition_range": [],
                "state": "not_applicable",
                "confidence": "low",
            }
        return {
            "condition": only["condition"],
            "condition_range": [only["condition"]],
            "state": "single_response",
            "confidence": "low",
        }

    if not known:
        state = "not_applicable" if na_count and not unknown_count else "unknown"
        return {"condition": None, "condition_range": [], "state": state, "confidence": "low"}

    ordinals = [item["ordinal"] for item in known]
    low, high = min(ordinals), max(ordinals)
    condition_range = [ORDINAL_TO_CONDITION[low]]
    if high != low:
        condition_range.append(ORDINAL_TO_CONDITION[high])

    # The synthesised condition is always a real model state derived from the
    # respondents who expressed a view: take the majority ordinal, and on a tie
    # (which includes every two-respondent disagreement) fall back to the lower
    # ordinal. Divergence between respondents is carried by `state`, not by
    # blanking the condition to Unknown. If later evidence beyond the diagnostic
    # materially shifts a capability, the diagnostic stops being the sole source
    # of truth and the condition is revised in the evidence pass.
    frequencies = Counter(ordinals)
    top_frequency = max(frequencies.values())
    winning_ordinal = min(o for o, count in frequencies.items() if count == top_frequency)
    condition = ORDINAL_TO_CONDITION[winning_ordinal]

    if high - low >= 2:
        state = "material_difference"
    elif unknown_count:
        state = "visibility_gap"
    elif na_count:
        state = "applicability_difference"
    elif high - low == 1:
        state = "adjacent"
    else:
        state = "agreement"

    confidence = "medium" if state == "agreement" and len(known) >= 2 else "low"
    return {
        "condition": condition,
        "condition_range": condition_range,
        "state": state,
        "confidence": confidence,
    }


def merge_company(responses: list[dict[str, Any]], overrides: dict[str, str | None]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    fields = {"name", "website", "stage", "buyingMotion", "marketingTeamShape"}
    company: dict[str, Any] = {}
    conflicts: list[dict[str, Any]] = []
    for field in fields:
        observed: dict[str, list[str]] = {}
        for response in responses:
            value = response["company"].get(field)
            if value not in (None, ""):
                observed.setdefault(str(value), []).append(response["response_id"])
        if len(observed) == 1:
            company[field] = next(iter(observed))
        elif len(observed) > 1:
            conflicts.append({"field": field, "values": observed})
            company[field] = None

    if overrides.get("name"):
        company["name"] = overrides["name"]
    if overrides.get("website"):
        company["website"] = overrides["website"]
    return company, conflicts


def build_model(
    responses: list[dict[str, Any]],
    mapping: dict[str, Any],
    existing_model: dict[str, Any] | None,
    overrides: dict[str, str | None],
) -> dict[str, Any]:
    assessment_ids = {response["assessment_id"] for response in responses}
    if len(assessment_ids) != 1:
        raise DiagnosticError(
            "All responses in one model must share an assessmentId; found: "
            + ", ".join(sorted(assessment_ids))
        )
    assessment_id = next(iter(assessment_ids))

    if existing_model and existing_model.get("assessment_id") != assessment_id:
        raise DiagnosticError(
            "Existing model assessment_id does not match diagnostic sources in this output directory"
        )

    company, company_conflicts = merge_company(responses, overrides)
    conflict_fields = {item["field"] for item in company_conflicts}
    if existing_model:
        for field, value in existing_model.get("company", {}).items():
            if field not in conflict_fields and company.get(field) in (None, "") and value not in (None, ""):
                company[field] = value
    now = utc_now()
    model_id = (
        existing_model.get("model_id")
        if existing_model and existing_model.get("model_id")
        else f"model_{uuid.uuid4()}"
    )
    created_at = existing_model.get("created_at", now) if existing_model else now

    respondents = [
        {
            "response_id": response["response_id"],
            "role": response["respondent"].get("role"),
            "name": response["respondent"].get("name"),
            "email": response["respondent"].get("email"),
            "completed_at": response["completed_at"],
        }
        for response in sorted(responses, key=lambda item: item["completed_at"])
    ]

    current_context = {
        "desired_outcomes": [
            {
                "response_id": response["response_id"],
                "role": response["respondent"].get("role"),
                "value": response["context"].get("desiredOutcomes", ""),
            }
            for response in responses
            if response["context"].get("desiredOutcomes")
        ],
        "biggest_constraints": [
            {
                "response_id": response["response_id"],
                "role": response["respondent"].get("role"),
                "value": response["context"].get("biggestConstraint", ""),
            }
            for response in responses
            if response["context"].get("biggestConstraint")
        ],
    }

    presenting_problems = sorted(
        {problem for response in responses for problem in response["presenting_problems"]}
    )
    response_answers = {
        response["response_id"]: {answer["question_id"]: answer for answer in response["answers"]}
        for response in responses
    }

    components: dict[str, Any] = {}
    existing_components = existing_model.get("components", {}) if existing_model else {}
    for component_id, component_map in sorted(
        mapping["components"].items(), key=lambda item: item[1]["order"]
    ):
        capabilities: dict[str, Any] = {}
        existing_capabilities = existing_components.get(component_id, {}).get("capabilities", {})
        mapped_questions = [
            (question_id, question_map)
            for question_id, question_map in mapping["questions"].items()
            if question_map["component"] == component_id
        ]
        mapped_questions.sort(key=lambda item: item[1]["order"])

        for question_id, question_map in mapped_questions:
            assessments: list[dict[str, Any]] = []
            question_copy = question_id
            for response in responses:
                answer = response_answers[response["response_id"]].get(question_id)
                if not answer:
                    continue
                question_copy = answer["question_copy"] or question_copy
                assessments.append(
                    {
                        "response_id": response["response_id"],
                        "role": response["respondent"].get("role"),
                        "condition": answer["condition"],
                        "original_condition": answer["original_condition"],
                        "ordinal": answer["ordinal"],
                        "answer": answer["answer_copy"],
                        "completed_at": response["completed_at"],
                    }
                )

            derived = derive_capability(assessments) if assessments else {
                "condition": None,
                "condition_range": [],
                "state": "unknown",
                "confidence": "low",
            }
            existing_capability = existing_capabilities.get(question_id, {})
            evidence_assertions = existing_capability.get("evidence_assertions", [])
            evidence_refs = [
                f"diagnostic:{item['response_id']}#{question_id}" for item in assessments
            ]
            for assertion in evidence_assertions:
                if isinstance(assertion, dict) and assertion.get("evidence_ref"):
                    evidence_refs.append(assertion["evidence_ref"])

            capabilities[question_id] = {
                "question_id": question_id,
                "question": question_copy,
                "order": question_map["order"],
                "primary_subcomponent": question_map["primary_subcomponent"],
                "secondary_subcomponents": question_map.get("secondary_subcomponents", []),
                "condition": derived["condition"],
                "condition_range": derived["condition_range"],
                "assessment_state": derived["state"],
                "confidence": derived["confidence"],
                "evidence_basis": "self_reported_diagnostic",
                "respondent_assessments": assessments,
                "evidence_assertions": evidence_assertions,
                "evidence_refs": sorted(set(evidence_refs)),
            }

        component_values = [
            ORDINALS[capability["condition"]]
            for capability in capabilities.values()
            if capability["condition"] in ORDINALS and ORDINALS[capability["condition"]] is not None
        ]
        unresolved = sum(capability["condition"] is None for capability in capabilities.values())
        if unresolved > len(capabilities) / 2:
            display_condition = "unknown"
        else:
            median = lower_median(component_values)
            display_condition = ORDINAL_TO_CONDITION[median] if median else "unknown"

        counts = Counter(
            capability["condition"] if capability["condition"] else "unknown"
            for capability in capabilities.values()
        )
        medium_count = sum(capability["confidence"] == "medium" for capability in capabilities.values())
        component_confidence = "medium" if medium_count > len(capabilities) / 2 else "low"
        components[component_id] = {
            "component_id": component_id,
            "name": component_map["name"],
            "role": component_map["role"],
            "order": component_map["order"],
            "subcomponents": component_map["subcomponents"],
            "display_condition": display_condition,
            "confidence": component_confidence,
            "counts": dict(sorted(counts.items())),
            "capabilities": capabilities,
        }

    mapped_question_ids = set(mapping["questions"])
    unmapped_answers = [
        {
            "response_id": response["response_id"],
            "role": response["respondent"].get("role"),
            **answer,
        }
        for response in responses
        for answer in response["answers"]
        if answer["question_id"] not in mapped_question_ids
    ]

    strengths: list[dict[str, str]] = []
    gaps: list[dict[str, str]] = []
    unknowns: list[dict[str, str]] = []
    contested: list[dict[str, str]] = []
    for component_id, component in components.items():
        for question_id, capability in component["capabilities"].items():
            item = {
                "component": component_id,
                "question_id": question_id,
                "question": capability["question"],
            }
            if capability["condition"] == "strong":
                strengths.append(item)
            if capability["condition"] in {"ad_hoc", "early"}:
                gaps.append({**item, "condition": capability["condition"]})
            if capability["assessment_state"] == "unknown":
                unknowns.append(item)
            if capability["assessment_state"] in {
                "material_difference",
                "visibility_gap",
                "applicability_difference",
            }:
                contested.append({**item, "comparison": capability["assessment_state"]})

    source_log = [
        {
            "source_id": f"diagnostic:{response['response_id']}",
            "source_type": "diagnostic_response",
            "response_id": response["response_id"],
            "role": response["respondent"].get("role"),
            "questionnaire_version": response["questionnaire_version"],
            "completed_at": response["completed_at"],
            "provenance": f"sources/diagnostic/{response['response_id']}.json",
        }
        for response in responses
    ]

    return {
        "schema_version": "ims-client-model-v1",
        "taxonomy_version": mapping["taxonomy_version"],
        "model_id": model_id,
        "assessment_id": assessment_id,
        "model_status": "working",
        "created_at": created_at,
        "updated_at": now,
        "company": company,
        "company_conflicts": company_conflicts,
        "respondents": respondents,
        "current_context": current_context,
        "presenting_problems": presenting_problems,
        "components": components,
        "system_observations": {
            "strengths": strengths,
            "gaps": gaps,
            "unknowns": unknowns,
            "contested": contested,
        },
        "source_log": source_log,
        "unmapped_answers": unmapped_answers,
    }


def markdown_escape(value: Any) -> str:
    return str(value if value not in (None, "") else "—").replace("|", "\\|").replace("\n", " ")


def render_markdown(model: dict[str, Any]) -> str:
    company = model["company"]
    lines = [
        f"# Marketing System Model — {company.get('name') or 'Unnamed company'}",
        "",
        "> Working model generated from self-reported IMS diagnostic responses. It is not an evidence-verified audit or canonical company record.",
        "",
        f"- **Model status:** {model['model_status']}",
        f"- **Assessment ID:** `{model['assessment_id']}`",
        f"- **Updated:** {model['updated_at']}",
        f"- **Respondents:** {len(model['respondents'])}",
        "",
        "## Company profile",
        "",
        "| Field | Value |",
        "|---|---|",
        f"| Stage | {markdown_escape(company.get('stage'))} |",
        f"| Buying motion | {markdown_escape(company.get('buyingMotion'))} |",
        f"| Marketing team | {markdown_escape(company.get('marketingTeamShape'))} |",
        f"| Website | {markdown_escape(company.get('website'))} |",
        "",
        "## Current context",
        "",
    ]
    for item in model["current_context"]["desired_outcomes"]:
        lines.append(f"- **Desired outcomes ({item['role']}):** {item['value']}")
    for item in model["current_context"]["biggest_constraints"]:
        lines.append(f"- **Biggest constraint ({item['role']}):** {item['value']}")
    if not model["current_context"]["desired_outcomes"] and not model["current_context"]["biggest_constraints"]:
        lines.append("- No current context supplied.")

    lines.extend(["", "## Component overview", "", "| Component | Condition | Confidence | Gaps | Unresolved |", "|---|---|---|---:|---:|"])
    for component in sorted(model["components"].values(), key=lambda item: item["order"]):
        gaps = sum(
            capability["condition"] in {"ad_hoc", "early"}
            for capability in component["capabilities"].values()
        )
        unresolved = sum(
            capability["condition"] is None for capability in component["capabilities"].values()
        )
        lines.append(
            f"| {component['name']} | {condition_label(component['display_condition'])} | {component['confidence']} | {gaps} | {unresolved} |"
        )

    for component in sorted(model["components"].values(), key=lambda item: item["order"]):
        lines.extend(
            [
                "",
                f"## {component['name']}",
                "",
                f"_{component['role']}_",
                "",
                "| Capability question | Condition | Confidence | Comparison | Respondent answers |",
                "|---|---|---|---|---|",
            ]
        )
        for capability in sorted(component["capabilities"].values(), key=lambda item: item["order"]):
            respondent_text = "; ".join(
                f"{item['role']}: {condition_label(item['condition'])}" for item in capability["respondent_assessments"]
            ) or "No answer"
            lines.append(
                "| "
                + " | ".join(
                    [
                        markdown_escape(capability["question"]),
                        markdown_escape(condition_label(capability["condition"])),
                        capability["confidence"],
                        capability["assessment_state"],
                        markdown_escape(respondent_text),
                    ]
                )
                + " |"
            )

    observations = model["system_observations"]
    lines.extend(["", "## System observations", "", "### Strong capabilities", ""])
    lines.extend(
        [f"- **{item['component']}:** {item['question']}" for item in observations["strengths"]]
        or ["- None identified from the current responses."]
    )
    lines.extend(["", "### L1 Ad hoc or L2 Activated capabilities", ""])
    lines.extend(
        [
            f"- **{item['component']} · {condition_label(item['condition'])}:** {item['question']}"
            for item in observations["gaps"]
        ]
        or ["- None identified from the current responses."]
    )
    lines.extend(["", "### Unknowns", ""])
    lines.extend(
        [f"- **{item['component']}:** {item['question']}" for item in observations["unknowns"]]
        or ["- None."]
    )
    lines.extend(["", "### Contested or visibility gaps", ""])
    lines.extend(
        [
            f"- **{item['component']} · {item['comparison']}:** {item['question']}"
            for item in observations["contested"]
        ]
        or ["- None."]
    )
    lines.extend(["", "## Source log", ""])
    lines.extend(
        [
            f"- `{item['source_id']}` — {item['role']}, completed {item['completed_at']} (`{item['provenance']}`)"
            for item in model["source_log"]
        ]
    )
    lines.append("")
    return "\n".join(lines)


def archive_current(output_dir: Path, model: dict[str, Any]) -> None:
    json_path = output_dir / "client-model.json"
    md_path = output_dir / "client-model.md"
    if not json_path.exists() and not md_path.exists():
        return
    history_dir = output_dir / "history"
    history_dir.mkdir(parents=True, exist_ok=True)
    stamp = str(model.get("updated_at", utc_now())).replace(":", "-").replace("+", "_")
    for current in (json_path, md_path):
        if not current.exists():
            continue
        target = history_dir / f"{current.stem}-{stamp}{current.suffix}"
        counter = 2
        while target.exists():
            target = history_dir / f"{current.stem}-{stamp}-{counter}{current.suffix}"
            counter += 1
        shutil.copy2(current, target)


def write_outputs(model: dict[str, Any], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "client-model.json"
    md_path = output_dir / "client-model.md"
    json_path.write_text(json.dumps(model, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(model), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build or refresh an IMSM client model from one or more diagnostic JSON responses."
    )
    parser.add_argument("inputs", nargs="+", type=Path, help="Diagnostic response JSON file(s)")
    parser.add_argument("--output-dir", required=True, type=Path, help="Client model workspace")
    parser.add_argument("--company-name", help="Override or supply the company name")
    parser.add_argument("--company-website", help="Override or supply the company website")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        mapping = load_mapping()
        output_dir = args.output_dir.expanduser().resolve()
        source_dir = output_dir / "sources" / "diagnostic"

        new_responses = [
            validate_and_normalize_response(read_json(path.expanduser()), mapping, path.expanduser())
            for path in args.inputs
        ]
        for response in new_responses:
            preserve_source(response["source_path"], response["response_id"], source_dir)

        all_source_paths = sorted(source_dir.glob("*.json"))
        responses = [
            validate_and_normalize_response(read_json(path), mapping, path) for path in all_source_paths
        ]
        response_ids = [response["response_id"] for response in responses]
        if len(response_ids) != len(set(response_ids)):
            raise DiagnosticError("Duplicate responseId values found in preserved sources")

        existing_path = output_dir / "client-model.json"
        existing_model = read_json(existing_path) if existing_path.exists() else None
        model = build_model(
            responses,
            mapping,
            existing_model,
            {"name": args.company_name, "website": args.company_website},
        )
        if existing_model:
            archive_current(output_dir, existing_model)
        write_outputs(model, output_dir)

        print(f"Built IMSM client model from {len(responses)} diagnostic response(s).")
        print(f"JSON: {output_dir / 'client-model.json'}")
        print(f"Markdown: {output_dir / 'client-model.md'}")
        print("Status: working; questionnaire conclusions remain self-reported and low-confidence.")
        return 0
    except DiagnosticError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
