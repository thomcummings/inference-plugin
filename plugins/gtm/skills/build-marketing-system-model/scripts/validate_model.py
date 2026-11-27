#!/usr/bin/env python3
"""Validate the structural invariants of an IMSM client model."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SKILL_DIR = Path(__file__).resolve().parent.parent
MAPPING_PATH = SKILL_DIR / "references" / "diagnostic-v1-mapping.json"
CONDITIONS = {"ad_hoc", "early", "working", "strong"}
ASSESSMENT_STATES = {
    "single_response",
    "agreement",
    "adjacent",
    "material_difference",
    "visibility_gap",
    "applicability_difference",
    "unknown",
    "not_applicable",
}
CONFIDENCE = {"low", "medium", "high"}


def load(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("Model must be a JSON object")
    return data


def validate(model: dict[str, Any], mapping: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if model.get("schema_version") != "ims-client-model-v1":
        errors.append("schema_version must be ims-client-model-v1")
    if model.get("taxonomy_version") != mapping.get("taxonomy_version"):
        errors.append("taxonomy_version does not match the bundled IMSM mapping")
    if model.get("model_status") not in {"working", "reviewed", "canonical"}:
        errors.append("model_status must be working, reviewed, or canonical")
    for field in ("model_id", "assessment_id", "created_at", "updated_at"):
        if not isinstance(model.get(field), str) or not model[field]:
            errors.append(f"{field} must be a non-empty string")

    components = model.get("components")
    if not isinstance(components, dict):
        return errors + ["components must be an object"]
    expected_components = set(mapping["components"])
    if set(components) != expected_components:
        errors.append(
            f"components must exactly match mapping: expected {sorted(expected_components)}, "
            f"got {sorted(components)}"
        )

    seen_questions: set[str] = set()
    for component_id, component in components.items():
        if not isinstance(component, dict):
            errors.append(f"components.{component_id} must be an object")
            continue
        display = component.get("display_condition")
        if display not in CONDITIONS | {"unknown"}:
            errors.append(f"components.{component_id}.display_condition is invalid: {display}")
        if component.get("confidence") not in CONFIDENCE:
            errors.append(f"components.{component_id}.confidence is invalid")
        capabilities = component.get("capabilities")
        if not isinstance(capabilities, dict):
            errors.append(f"components.{component_id}.capabilities must be an object")
            continue

        expected_questions = {
            question_id
            for question_id, question in mapping["questions"].items()
            if question["component"] == component_id
        }
        if set(capabilities) != expected_questions:
            errors.append(
                f"components.{component_id}.capabilities mismatch: expected "
                f"{sorted(expected_questions)}, got {sorted(capabilities)}"
            )

        for question_id, capability in capabilities.items():
            if question_id in seen_questions:
                errors.append(f"duplicate capability question: {question_id}")
            seen_questions.add(question_id)
            path = f"components.{component_id}.capabilities.{question_id}"
            condition = capability.get("condition")
            if condition is not None and condition not in CONDITIONS:
                errors.append(f"{path}.condition is invalid: {condition}")
            if capability.get("assessment_state") not in ASSESSMENT_STATES:
                errors.append(f"{path}.assessment_state is invalid")
            if capability.get("confidence") not in CONFIDENCE:
                errors.append(f"{path}.confidence is invalid")
            if not isinstance(capability.get("respondent_assessments"), list):
                errors.append(f"{path}.respondent_assessments must be an array")
            for item in capability.get("respondent_assessments", []):
                if item.get("condition") not in CONDITIONS | {"unknown", "not_applicable"}:
                    errors.append(f"{path} contains invalid respondent condition")

    expected_questions = set(mapping["questions"])
    if seen_questions != expected_questions:
        errors.append(
            f"question coverage mismatch: expected {len(expected_questions)}, got {len(seen_questions)}"
        )

    source_log = model.get("source_log")
    if not isinstance(source_log, list) or not source_log:
        errors.append("source_log must contain at least one source")
    elif len({item.get("source_id") for item in source_log}) != len(source_log):
        errors.append("source_log source_id values must be unique")

    observations = model.get("system_observations")
    if not isinstance(observations, dict):
        errors.append("system_observations must be an object")
    else:
        for key in ("strengths", "gaps", "unknowns", "contested"):
            if not isinstance(observations.get(key), list):
                errors.append(f"system_observations.{key} must be an array")

    serialized = json.dumps(model)
    for legacy in ("limited", "missing"):
        if f'"condition": "{legacy}"' in serialized or f'"display_condition": "{legacy}"' in serialized:
            replacement = "early" if legacy == "limited" else "ad_hoc"
            errors.append(f"model contains legacy condition label {legacy}; use {replacement}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an IMSM client model JSON file")
    parser.add_argument("model", type=Path)
    args = parser.parse_args()
    try:
        model = load(args.model.expanduser())
        mapping = load(MAPPING_PATH)
        errors = validate(model, mapping)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Valid IMSM client model: {args.model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
