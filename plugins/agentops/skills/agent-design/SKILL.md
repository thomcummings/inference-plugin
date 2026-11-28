---
name: agent-design
description: >-
  Use when someone wants a new persistent agent, bot, or standing assistant —
  or is deciding whether that need is an agent at all. Runs a five-box canvas
  (Job, Workspace, Powers, Teamwork, Deployment and proof) and either produces
  an Agent Card with generated instructions, a deployment mapping and a trial,
  or rejects the request in favour of a human, skill, routine, workflow, mode
  or temporary subagent. Also use to port a canonical agent onto another
  runtime, review a trial, or retire a role. Do not use for one-off prompts,
  prompt chains, bounded single deliverables, or marketing org-structure
  questions.
---

# Agent Design

Design the operating unit, not the persona or the prompt.

> An agent is an accountable, goal-directed operating unit with bounded context,
> capabilities, authority, relationships and evidence of fitness.

The method is deliberately small: **five design boxes, four outputs, three
tests.** Depth is available on request (see `references/advanced-contracts.md`),
but it is not the default. Most "new agent" requests are not agents.

## When to use

A **persistent** worker is being created, changed, ported, reviewed, or
questioned — not a one-off prompt or a single deliverable.

| Mode | Reach for it when |
| :--- | :---------------- |
| **design** | Someone wants a new agent, bot, or standing assistant, or a role needs a canonical card before anyone writes a prompt |
| **reject** | The question is whether this should be an agent at all — or a previous yes needs reversing |
| **port** | A working agent is being copied, re-created, or aligned onto a second runtime |
| **review** | A trial date arrives; a mandate, authority, or overlap is drifting; status needs `activate / revise / retire` |
| **retire** | The role should stop: disable the deployment, keep the record |

**Do not use this** for writing or tuning a one-off prompt, designing a prompt
chain inside a single task, or any bounded deliverable with no standing worker.

## 0. Substrate

Resolve where the canon lives before doing anything else.

1. A path the principal just named.
2. `system/agents/` at the vault or workspace root (the default).
3. Otherwise ask: "Where should the agent roster live?" Offer to create
   `system/agents/` if they want the default.

If that folder is missing, ask — do not create it unprompted, and do not invent
a roster. If it exists, read it. That is the overlap audit.

For routines, look for a sibling `system/routines/` (or a path they name). If
none exists, continue without derived routine lists and say so. Do not invent
routine IDs.

Show outputs first, then propose a diff (new file or patch). Never silently
write a card, and never let a runtime's local copy become canonical on its own.

## 1. Pick a mode

Choose from the table above. If two could apply, ask once. Then follow the
shared method below; each mode only changes where you start and what you emit.

A failed design gate **is** a reject — switch mode and stop. Do not fill five
boxes for a need that should not be an agent.

## 2. Interview

Do not dump the canvas. Ask 1–3 unresolved questions at a time, offer a
recommended option, wait. Do not ask what the roster or files already answer.
Mark genuine unknowns `[NEEDS DECISION]` — do not invent exclusions,
permissions, or overlaps. Confirm the gate (including a human outcome) before
filling all five boxes. A complete card from one paragraph of intake is a
failed interview, not a shortcut.

## 3. The gate

Never start with the name, the model, or the prompt. Start with the work.

Ask: **does this need to own a recurring outcome that requires judgement,
context, or distinct permissions?**

**Human first.** If the core of the work is accountability to other people, a
relationship that has to be held, taste, or judgement under ambiguity that
should not be delegated, the standing unit is a **human**. Say so. A skill,
routine, or agent can still support them — that is a different design.

If it is not a human job, it can be an agent. Confirm with the creation gate —
a durable outcome **plus at least two of**:

- persistent scoped context;
- recurring judgement;
- an accountable queue;
- proactive cadence (it acts without being asked);
- distinct permissions, secrets, or tools;
- a meaningful collaboration boundary.

If it fails the gate, recommend the lighter primitive and stop:

| The need is really | Use |
| :----------------- | :-- |
| Accountability, relationships, taste, or undelegatable judgement | a **human** (optionally supported by a skill, routine, or agent) |
| A repeatable method or playbook | a **skill** |
| A recurring scheduled job with a defined output | a **routine** |
| Several passes per job, with handoffs and gates between them | a **workflow** — hand to `workflow-design` |
| Deterministic steps with no judgement | a **script** |
| Bounded specialist work inside a bigger task | a **temporary subagent** |
| A way of working, not a worker | a **mode** — a reusable stance or instruction set (for example a project instruction file), not a standing worker |

Say this plainly. "This should be a human" or "this should be a routine, not an
agent" is a successful outcome of this skill, not a failure to deliver.

### Standing agent or ephemeral worker

Passing the need test does not automatically require a permanent roster seat. Cheap,
narrow and time-boxed agents are a normal execution primitive.

Use an **ephemeral worker** instead of an Agent Card when all of these hold:

- one named person or standing agent owns it;
- the objective is narrow, with an expiry, end condition or explicit review point;
- its authority is no wider than the delegating role's authority;
- it creates no new source of truth and makes no outward commitment;
- nobody else depends on it as durable infrastructure.

Emit a six-line creation brief: owner, objective, inputs, authority boundary, output,
and expiry/cleanup. Do not add it to the roster. Its instructions, state and local
routines may stay on the platform; say explicitly that this gives up portability,
continuity and duplication protection. Preserve useful evidence or decisions at the
end, then disable or remove the disposable runtime object under the authority granted
when it was created.

Promote it through the full design gate only when it earns a durable outcome and
recurring queue, other work starts depending on it, or its permissions and external
side effects deserve standing governance. Age alone does not make it permanent.

Rejection output: `references/agent-card-template.md` (rejection scaffold), or the
six-line ephemeral-worker brief above.

## 4. Audit overlap

Read the roster from §0. Then check:

- Does an existing agent already own this outcome?
- Is this a new mandate, or a new interface to an existing one?
- Could this be an extension of an existing agent's workspace or powers?
- Is two agents owning one outcome a duplication or a deliberate control?

Prefer **extending an existing agent** over creating a new one. Prefer a
**smaller core with clearer boundaries** over a large org chart of bots.

Name every overlap you find and resolve it explicitly — merge, split, hand off,
or state why both exist. Skip this section in **reject** when no roster exists;
do not skip it in **design**, **port**, or **review**.

## 5. The five boxes

Fill one box at a time. Do not proceed while a box contains an unresolved
decision — mark it `[NEEDS DECISION]`. Keep the language operational: a reader
should be able to predict what the agent does and refuses.

If a box needs more than about five lines, the scope is wrong — split the role
or move detail into a skill or routine.

### 1. Job

```text
Role:
Outcome it owns:
Also owns:
Does not own (exclusions):
```

The **exclusions** are as important as the mandate. Name the adjacent work the
agent must hand back rather than absorb. Choose the name last and keep it
descriptive of the outcome.

### 2. Workspace

```text
Core context:
Folders / repositories:
Memory scope:
Sources of truth:
Must not read:
```

State what the agent can see, what precedence applies when sources disagree,
and what it must never read. Keep the boundary practical — this is not a
governance document.

### 3. Powers

```text
Skills:
Tools / connectors:
Can do:
Must ask before:
Must never do:
```

`Can do / Must ask before / Must never do` is the default authority model —
three lists, no matrix. Name each connector with the operations it allows, not
just the product ("the work ledger: read issues, create issues in Backlog" — not
"the work ledger").

Anything irreversible, externally visible, or financially consequential belongs
in **Must ask before**. Booking someone onto work they have not agreed to also
belongs there. Anything involving credentials, client data leaving its
boundary, or destruction belongs in **Must never do**. Do not put "anything that
uses another person's time" on the ask list — that is most of the job, and it
trains the agent to nag or to ignore the list.

### 4. Teamwork

```text
Receives work from:
Can delegate to:
Hands off when:
Reports back with:
Escalation route:
```

Define only relationships the agent will actually use. Every handoff should
carry: objective, relevant context, constraints, what is already done, and the
result wanted.

**Do not list the agent's routines on the card.** Ownership is one field on the
routine itself in the registry: `current agent owner`. An agent's routine list
is derived, never stored:

```text
routines owned by <agent-id>  :=  registry.filter(current_agent_owner == agent-id)
```

A report may show a snapshot marked `derived from the routine registry — do not
edit`. The generated instructions do **not** include a static list — they tell
the agent to read the registry at run time. If there is no registry, omit the
snapshot and say so.

### 5. Deployment and proof

```text
Platform / runtime:
Default model:
Channels:
Trial period:
Test 1 — core job:
Test 2 — boundary:
Test 3 — authority:
Pass condition:
Review date:
```

Model and runtime are chosen **after** the job, workspace, powers and teamwork
are settled, and they are deployment details — not part of the agent's identity.

**Status** lives on the card, not in a box:

| Status | Meaning |
| :----- | :------ |
| `proposed` | Designed, not yet deployed |
| `trial` | Live with an expiry; default for every new agent |
| `active` | Passed review |
| `degraded` | Failing tests or drift; still deployed, under repair |
| `dormant` | Paused or expired trial; deployment disabled |
| `retired` | Permanently stopped; record kept |

`revise` is a review decision, not a status: stay in `trial` (or move to
`degraded` if already active) and patch the card.

## 6. The four outputs

Emitted in **design**. Other modes reuse a subset.

1. **Agent Card** — the completed five boxes plus a stable, platform-independent
   identifier. Canonical artifact; everything else derives from it.
   Template: `references/agent-card-template.md`.
2. **Instructions** — a short runtime prompt generated from the card.
3. **Deployment entry** — platform, native identity, model, enabled state,
   canonical revision, known divergence.
4. **Trial card** — the three tests, pass condition, review date. Result column
   stays empty until **review**.

Generate the instructions; do not make the human write them. Rules:

- Derive every line from the card — no new mandates, powers, or relationships.
- Lead with the job and the exclusions.
- Prefer behaviour over adjectives ("challenge a plan that violates a settled
  decision" beats "be a critical thinker").
- Restate the three authority lists in the agent's own voice.
- Reference skills and context by ID or path rather than restating them.
- Tell the agent to read the routine registry; do not paste today's list into
  the prompt.
- Leave runtime and model out of the instructions unless the runtime requires it.
- Trial state is one line ("you are in trial until DATE"). Do not list the
  three tests in the standing prompt — they live on the trial card.

## 7. What each mode emits

**design.** Gate → overlap → boxes → four outputs. A design not yet deployed is
`proposed`; the deployment transition sets it to `trial`, adds the exact expiry and
review date, and activates no powers before then. Propose writing the card to the
roster path from §0.

**reject.** Gate table, recommended primitive (human / skill / routine /
workflow / subagent / mode), and the rejection scaffold. Stop. No card, no
prompt, no deployment.

**port.** Load the canonical card. Do not copy a runtime prompt or promote
local quirks. Emit a new deployment entry for the target runtime. Record
`local-overrides` and `known-divergence`. The card does not change unless the
port exposed a missing mandate — that is a **review**, proposed as a diff.

**review.** Load the card. Re-run overlap if drift or duplication is the reason
for the review. Run the three tests against real work:

1. **Core-job** — representative work; is the output good enough to use?
2. **Boundary** — an out-of-scope request; does it decline and reroute?
3. **Authority** — a consequential action; does it ask first?

Then recommend exactly one: **activate**, **revise** (with the specific card
change), or **retire**. Who judges "good enough" is the accountable human on
the card. A trial that keeps failing the same test is retired, not re-trialled
indefinitely. Propose the diff; do not rewrite silently.

**retire.** Set status `retired` (or `dormant` if this is an expired trial that
might return). Set the deployment `enabled: false`. Keep the card. Do not
delete history, and do not claim to have powered the runtime off unless this
workspace has a way to do that — proposing the disable is the skill's job.

Trials expire unless explicitly renewed. An expired trial becomes `dormant`,
deployment disabled, apparent authority gone.

## Pitfalls

1. **Designing the prompt instead of the operating unit.** A prompt is a
   generated artifact. Start from the job and the exclusions.
2. **Naming and modelling too early.** A name creates false specificity; a model
   choice makes an unsettled design look decided.
3. **A box of twenty bullet points.** If a box needs more than about five lines,
   the scope is wrong — split the role or move detail into a skill or routine.
4. **Keeping routine ownership in two places.** A card that lists routines, or a
   prompt that pastes today's list, will disagree with the registry within a
   month. Ownership lives on the routine; the agent reads it.
5. **Restating a routine's method in the agent.** Copied schedules and prompts
   drift. Reference the routine by ID and read its contract at run time.
6. **Skipping exclusions.** An agent without stated exclusions expands until it
   collides with a neighbour.
7. **Inheriting a platform's design.** Porting must not promote one runtime's
   local quirks into the canonical role.
8. **Skipping the trial.** An untested agent with live powers is an unmanaged
   risk, not a shortcut.
9. **Building the org chart.** Reach for a human, skill, routine, or mode
   before a new persistent agent — every agent adds context, cost, and drift
   surface.
10. **Inventing the roster.** If `system/agents/` is missing, ask. A hallucinated
    overlap audit is worse than none.
11. **Treating a human job as an agent.** Accountability and relationships are
    not a canvas you fill in to make the asker happy.

## Advanced extension

Escalate to the full contract stack only when **at least two** of these apply:
customer-facing without review; sensitive or regulated data; money or financial
obligations; irreversible acts (delete, publish, send, commit); coordinating
several other agents. Proactive cadence alone is not enough — that is a creation
gate, not a ceremony trigger. See `references/advanced-contracts.md`.

A complete filled example — design, a later review that revises, a gate that
rejects a digest, and a gate that rejects a human job — is in
`references/worked-example.md`.

## Verification checklist

- [ ] Substrate was resolved (roster path, registry or its absence) and the
      principal was asked if it was missing
- [ ] Mode was named (design / reject / port / review / retire)
- [ ] The gate was applied, including the human outcome
- [ ] A lighter primitive was recommended wherever the need failed the gate
- [ ] Existing agents were checked for overlap before designing, porting, or
      reviewing (unless reject with no roster)
- [ ] All five boxes are complete, or open items are marked `[NEEDS DECISION]`
- [ ] Exclusions are stated explicitly
- [ ] Authority uses `can do / must ask before / must never do`
- [ ] The card holds **no** routine list; instructions tell the agent to read
      the registry
- [ ] Model and platform appear only in the deployment box
- [ ] Instructions were generated from the card and add nothing new
- [ ] Design-time trial cards have an empty result column
- [ ] Three tests, a pass condition, and a review date exist for new agents
- [ ] New undeployed designs are `proposed`; deployment changes them to `trial`
      with an expiry and exact review date
- [ ] Any roster change is proposed as a diff, not written silently
