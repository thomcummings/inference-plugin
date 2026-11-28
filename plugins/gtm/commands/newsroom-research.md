---
description: Run only the Researcher — produce a dossier from an existing brief
argument-hint: "[story-slug]"
---

Invoke the `newsroom-researcher` agent via Task for the story slug in `$ARGUMENTS`.

Before invoking:
1. Load the `newsroom` skill so you understand the pipeline's file structure
2. Confirm `stories/<slug>/brief.md` exists — if it does not, stop and tell the user the brief is required first (suggest `/newsroom-commission`)
3. Read `story.json` to get the shared context to pass to the agent

Call the agent with the brief path and shared context. When it returns, present the dossier summary for user review and stop — do not proceed to the Interviewer stage.

$ARGUMENTS
