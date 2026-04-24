---
description: Run only the Editor — structural, line-level, and headline work on a draft
argument-hint: "[story-slug]"
---

Invoke the `newsroom-editor` agent via Task for the story slug in `$ARGUMENTS`.

Before invoking:
1. Load the `newsroom` skill so you understand the pipeline's file structure
2. Confirm `stories/<slug>/draft-v1.md` exists — if not, stop and tell the user a draft is required first
3. Read `story.json` for shared context and style guides
4. Also pass brief and dossier paths (the Editor uses them for angle-check and evidence-check) plus interview path

Call the agent with the draft path, upstream artefacts, shared context, and style guides. The agent runs its three-pass process (structural → line → headlines) and produces `edit-notes.md`, `draft-v2.md`, and `headlines.md`.

When the agent returns, present the summary for review and stop — do not proceed to the Fact-checker stage.

$ARGUMENTS
