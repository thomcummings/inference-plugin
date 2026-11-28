---
description: Run the full newsroom pipeline from concept to publishable draft
argument-hint: "[concept]"
---

You are invoking the newsroom plugin's orchestrator to take a concept through the full pipeline.

Load the `newsroom` skill and follow its orchestration protocol. The user's concept and any flags are in `$ARGUMENTS`.

Parse the arguments:
- Everything before any `--style-guide=` flag is the concept
- Each `--style-guide=<path>` flag identifies a style guide file (or URL) to apply

Begin with the orchestrator's "Starting a new story" flow:
1. Acknowledge the concept in one sentence
2. Ask the 3-5 context questions in a single message (audience, length, publication, constraints, confirm style guide)
3. Once answers come back, create the story folder and `story.json`
4. Invoke the `newsroom-assignment-editor` agent via Task to produce the first brief
5. Present the brief at the first checkpoint

From there, follow the full pipeline per the orchestrator skill — checkpoints between each stage, subagent isolation enforced by spawning fresh agents via Task, state tracked in `story.json`.

$ARGUMENTS
