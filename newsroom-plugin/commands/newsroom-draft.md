---
description: Run only the Writer — produce a first draft from brief, dossier, and interview
argument-hint: "[story-slug]"
---

Invoke the `newsroom-writer` agent via Task for the story slug in `$ARGUMENTS`.

Before invoking:
1. Load the `newsroom` skill so you understand the pipeline's file structure
2. Confirm `stories/<slug>/brief.md`, `stories/<slug>/dossier.md`, and `stories/<slug>/interview.md` all exist — if any is missing, stop and tell the user what's needed first
3. Read `story.json` for shared context and check whether any style guides are listed; if yes, load them and pass contents to the agent
4. Read any additional interview files (`interview-2.md` etc.) and pass them if present

Call the agent with all upstream artefact paths, shared context, and style guides. The agent will do its pre-flight check, then draft straight through without self-editing, apply its AI-slop self-check, and write `draft-v1.md`.

When the agent returns, present the draft summary for review and stop — do not proceed to the Editor stage.

$ARGUMENTS
