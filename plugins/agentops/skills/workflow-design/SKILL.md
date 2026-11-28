---
name: workflow-design
description: >-
  Use when a job needs several agent passes rather than one: a pipeline, a
  multi-agent process, a build-then-review loop, a research-write-edit chain,
  or "should this be several agents?". Decides first whether it needs to be a
  workflow at all (most multi-step jobs are one skill), then designs the
  stages, the artefact each stage hands on, where independent contexts matter,
  the human gates, where state lives and what happens when a stage fails.
  Produces a workflow card and an orchestrator outline; each stage that is a
  real method is built with skill-design. Also use to review a workflow that
  has started converging, stalling or skipping its gates. Not for one method
  run by one agent (skill-design), a standing role (agent-design) or a
  scheduled trigger (routine-design).
---

# Workflow Design

Design the handoffs, not the agents.

> A workflow is a job split into passes that run in separate contexts, each
> with its own role, handing written artefacts to the next, with checks and
> human gates between them. It earns its cost only when one context doing all
> of it would make the result worse.

Most multi-step jobs are a skill. Steps are not stages: a skill can have
twenty steps and still be one mind. Splitting work across agents costs tokens,
time and coordination, and it loses context at every handoff. The point of a
workflow is to buy something a single context can't give you.

## Modes

| Mode | Reach for it when |
| :--- | :---------------- |
| **design** | A job looks like it needs more than one pass |
| **reject** | It doesn't: route to a skill, an agent, a routine or a script |
| **review** | A workflow's stages have started agreeing too easily, stalling, or skipping gates |

## 0. Read first

Read what exists before asking: the job's current version (a prompt, a doc,
a skill, how it's done by hand today), the installed skills that might cover
a stage, and any workflows already in the library. Ask one to three questions
at a time, each with a recommended answer. Mark unknowns `[NEEDS DECISION]`.

## 1. The gate: does this need to be a workflow?

Ask one question: **does the job get worse if one context does all of it?**
It's a workflow only if at least one of these is true:

- **Independence.** A pass must not see another's reasoning: a reviewer who
  didn't build it, a fact-checker who didn't write it, personas who can't
  anchor on each other.
- **A human gate.** Someone must approve between stages, and work must stop
  until they do.
- **Different powers.** Stages need different tools, access or models that
  shouldn't sit in one context (one pass reads private data, another
  publishes).
- **Scale.** The work is genuinely parallel and too big for one context.

If none is true, recommend the lighter home and stop:

| The need is really | Home |
| :----------------- | :--- |
| One method, however many steps | a **skill** (`skill-design`) |
| A standing role across many jobs | a **persistent agent** (`agent-design`) |
| The same job on a schedule or event | a **routine** (`routine-design`), which may run a workflow |
| Fixed steps with no judgement | a **script** |

"This is one skill, not a workflow" is a good outcome.

## 2. The workflow card

Fill one box at a time. Keep each to about five lines; more means the
workflow is doing too much.

### 1. Job and output
What the whole workflow produces, for whom, and what "done" means.

### 2. Stages
For each stage: its role, its single job, and the skill it runs (existing, or
to be built with `skill-design`). Name the stage that owns the final output.
Fewer is better: every stage you add is a handoff that loses context.

### 3. Artefacts
For each handoff: the written artefact passed on (a brief, a dossier, a
draft, a ledger, a verdict), its required sections, and where it is saved.
A stage reads its inputs from artefacts, never from another stage's chat.

### 4. Independence
Which stages must run in fresh contexts, and what each one is not allowed to
see. Example: the reviewer writes its checklist from the brief **before** it
reads the draft, so it tests the work instead of confirming it.

### 5. Gates
Where a human must approve before the next stage, what they see when asked,
and what the workflow does while it waits. Mark which decisions an agent may
never make (readying work, merging, publishing, spending).

### 6. State and failure
Where progress lives (files, labels, a tracker), so any stage can resume
cold. For each stage: what happens when it fails, how many fix rounds are
allowed before it goes to a human, and how a stale or duplicate run is
detected and discarded.

## 3. The outputs

1. **Workflow card:** the six boxes above, saved beside the workflow.
2. **Orchestrator outline:** a short skill that runs the stages in order,
   enforces the gates, checks each artefact exists before moving on, and
   holds no stage's method itself.
3. **Stage list:** for each stage, the existing skill it uses or a brief for
   `skill-design` to build it.
4. **A trial plan:** one real job run end to end, plus one deliberate failure
   (a bad artefact, a refused gate) to check the workflow stops where it
   should.

Show everything before writing files, and write only after the user approves.

## 4. Review

Check a live workflow against its card. Look for:

- **Convergence:** later stages echoing earlier ones (independence has leaked;
  check what each stage can see).
- **Stalls:** artefacts missing sections, or stages asking each other
  questions in chat.
- **Gate skipping:** work that moved on without the approval the card names.
- **Dead stages:** a stage whose output nobody reads. Merge it or cut it.

Recommend exactly one: **keep**, **revise** (with the change), **merge stages**
or **collapse to a skill**.

## Patterns

Three common shapes, each with a reference workflow in this marketplace:

- **Pipeline with independent checks** (`gtm:newsroom`): brief, research,
  write, edit, fact-check. Each role is a separate subagent; the fact-checker
  works from the dossier, not the writer's account.
- **Independent views, then synthesis** (`thinking-tools:debate-room`):
  personas answer alone, then see each other once to rebut, then one pass maps
  the tensions and synthesises.
- **Build, review, fix loop with human gates** (`relay-loop`): spec, build,
  independent review, capped fix rounds, and a human owning readiness and
  merge.

## Pitfalls

1. **Agents for the sake of agents.** Splitting a one-mind job adds cost and
   loses context. Apply the gate honestly.
2. **Handoffs in chat.** If the next stage can't start from a saved artefact,
   the workflow can't resume or be checked.
3. **Leaky independence.** A reviewer that reads the builder's summary first
   is confirming, not reviewing.
4. **Gates as suggestions.** A gate the orchestrator can talk itself past is
   not a gate.
5. **Unbounded loops.** Cap fix rounds and send the rest to a human.
6. **Method in the orchestrator.** The orchestrator routes and checks; each
   stage's method lives in its own skill.

## Checklist

- [ ] Gate applied; lighter home recommended where it failed
- [ ] Every stage has one job and a named skill
- [ ] Every handoff is a saved artefact with required sections
- [ ] Independence stated: what each fresh-context stage can't see
- [ ] Gates named, with the decisions agents may never make
- [ ] State, failure handling and fix-round caps defined
- [ ] Trial plan includes one deliberate failure
- [ ] Nothing written without the user's approval

## Method lineage

Part of the Inference agentops design set with `skill-design`,
`agent-design` and `routine-design`: each decides first whether the need
belongs to it at all. The patterns come from Inference's own newsroom,
debate-room and relay-loop workflows.
