#!/usr/bin/env python3
"""Render a human-readable Markdown view from an IMSM client model JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from import_diagnostic import render_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description="Render client-model.md from client-model.json")
    parser.add_argument("model", type=Path)
    parser.add_argument("--output", type=Path, help="Defaults to client-model.md beside the JSON")
    args = parser.parse_args()

    model_path = args.model.expanduser()
    try:
        model = json.loads(model_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Error: cannot read model JSON: {exc}", file=sys.stderr)
        return 2
    if not isinstance(model, dict):
        print("Error: model must be a JSON object", file=sys.stderr)
        return 2

    output = args.output.expanduser() if args.output else model_path.with_name("client-model.md")
    output.write_text(render_markdown(model), encoding="utf-8")
    print(f"Rendered: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
