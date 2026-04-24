---
description: Run only the Fact-checker — verify claims and produce a final publishable draft
argument-hint: "[story-slug]"
---

Invoke the `newsroom-fact-checker` agent via Task for the story slug in `$ARGUMENTS`.

Before invoking:
1. Load the `newsroom` skill so you understand the pipeline's file structure
2. Confirm `stories/<slug>/draft-v2.md` exists — if not, stop and tell the user an edited draft is required first
3. Read `story.json` for shared context
4. Also pass dossier and interview paths (the Fact-checker reads these to verify specific claims)

Call the agent with the draft-v2 path, upstream artefacts, and shared context. The agent extracts checkable claims, verifies each convergently, applies surgical corrections, and produces `claims-check.md` and `final.md`.

When the agent returns, present the claims-check summary. If there are UNCERTAIN verdicts requiring user decisions, surface them and wait for resolution before marking the pipeline complete. If all claims are VERIFIED or handled, the pipeline is done — surface `final.md` as the publishable artefact.

$ARGUMENTS
