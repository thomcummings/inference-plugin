---
description: Resume a newsroom pipeline from the last completed stage
argument-hint: "[story-slug]"
---

Resume the newsroom pipeline for the story slug in `$ARGUMENTS`.

1. Load the `newsroom` skill
2. Read `stories/<slug>/story.json` — if it doesn't exist, stop and tell the user that slug has no pipeline state (suggest starting fresh with `/newsroom`)
3. Inspect the `stages` object in `story.json` to identify the last stage with `status: "complete"` and the next stage with `status: "pending"` or `"in_progress"`
4. Summarise pipeline state to the user — what's done, what's next, any open flags from earlier stages
5. Ask the user: "Resume from [next stage]? Or jump to a specific stage?"
6. On confirmation, invoke the appropriate next agent via Task, loading the shared context and upstream artefact paths from `story.json`

From the point of resumption, continue the full orchestration flow per the `newsroom` skill — checkpoints between stages, subagent isolation, state updates to `story.json`.

$ARGUMENTS
