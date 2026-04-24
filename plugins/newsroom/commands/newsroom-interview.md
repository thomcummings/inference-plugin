---
description: Run only the Interviewer — produce interview plan and transcript (or interactive artefact)
argument-hint: "[story-slug]"
---

Invoke the `newsroom-interviewer` agent via Task for the story slug in `$ARGUMENTS`.

Before invoking:
1. Load the `newsroom` skill so you understand the pipeline's file structure
2. Confirm both `stories/<slug>/brief.md` and `stories/<slug>/dossier.md` exist — if either is missing, stop and tell the user what's needed first
3. Read `story.json` for shared context

Call the agent with brief path, dossier path, and shared context. The agent will ask the user to choose between conversational or interactive-artefact mode, then plan the interview and run it (or generate the shareable HTML artefact).

When the agent returns, present the interview summary for review and stop — do not proceed to the Writer stage.

$ARGUMENTS
