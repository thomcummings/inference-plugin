---
description: Run only the Assignment Editor — concept to brief
argument-hint: "[concept]"
---

Invoke the `newsroom-assignment-editor` agent via Task with the concept in `$ARGUMENTS`.

Before invoking, load the `newsroom` skill so you understand the expected story folder structure. Create the story folder (`stories/<slug>/`) and initial `story.json` if one doesn't exist.

Then call the agent with the concept and let it run its 2-3 question interrogation plus brief production. When it returns, present the brief for user review and stop — do not proceed to the Researcher stage.

$ARGUMENTS
