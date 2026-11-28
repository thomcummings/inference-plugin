---
name: skill-design
description: >-
  Use when someone wants a new skill, wants to turn a repeatable process into
  one, or is deciding whether a need is a skill at all — "make this a skill",
  "turn my proposal process into a skill", "we keep doing this by hand every
  time". Runs a gate against the installed library, a five-box canvas (Job,
  Trigger, Intake, Method, Placement and proof) and a three-test trial, and
  either produces a built skill with its trigger eval, or rejects the request
  in favour of an edit to an existing skill, a context note, a mode, a routine,
  an agent or a script. Also use to restructure a skill that has outgrown its
  SKILL.md, review one that has drifted or stopped firing, or retire one. Do
  not use for one-off prompts, for writing the domain material a skill encodes,
  or for building or customising a plugin.
---

# Skill Design

Design the capability, not the prompt.

> A skill is a repeatable method with a defined output, a stated trigger and a
> stated boundary — encoded once so it stops being re-improvised.

The method is small: **five boxes, one shape decision, three tests.** Depth is
available on request (`references/conventions.md` for the canon,
`references/trigger-eval.md` for the triggering test), but it is not the
default. Most "let's make this a skill" requests are an edit to a skill that
already exists.

## Modes

A **repeatable method** is being encoded, changed, reviewed or questioned — not
a one-off prompt and not a single deliverable. The discovery boundary lives in
the description, where it can affect whether this skill runs; the table below
is for routing once it has.

| Mode | Reach for it when |
| :--- | :---------------- |
| **design** | Someone wants a new skill, or a process done by hand three times should stop being re-improvised |
| **reject** | The question is whether this should be a skill at all — or a previous yes needs reversing |
| **restructure** | A working skill has outgrown a single SKILL.md, or its step files carry their own ordering |
| **review** | A trial date arrives; a skill stopped firing, fires on the wrong things, or its output always gets edited the same way |
| **retire** | The skill should stop: drop it from the build, keep the record |

**Do not use this** for writing or tuning a one-off prompt; for authoring the
domain material a skill encodes (a positioning framework, a brand canon — the
skill holds the method, the practitioner holds the material); or for
scaffolding, packaging or customising a plugin.

## 0. Substrate

Resolve the library before doing anything else. There is no skills registry to
maintain — the build is the registry — but the installed set is read on every
run.

1. **The installed skills**, by namespaced ID, with their descriptions. This is
   the library the new skill has to live beside.
2. **The plugin source repo** — where an edit actually lands. The installed
   copy is a read-only cache; never edit it and never treat it as canonical.
3. **A vault mirror**, if one exists, may lag the build. The plugin is source
   of truth.

That one read buys two things: the overlap audit in §4, and the negative half
of the trigger eval in box 5. Keep it; do not go looking twice.

If the installed set cannot be listed, say so and continue without an overlap
audit. A hallucinated neighbour is worse than none. Never invent skill IDs.

Show outputs first, then propose a diff. Never write into a plugin repo
silently, and never let an installed copy become canonical on its own.

## 1. Pick a mode

Choose from the table above. If two could apply, ask once. Then follow the
shared method below; each mode only changes where it starts and what it emits.

A failed gate **is** a reject — switch mode and stop. Do not fill five boxes
for a need that should not be a skill.

## 2. Interview

Do not dump the canvas. Ask one to three unresolved questions at a time, each
with a recommended answer and one line of reasoning, then wait. The principal
should barely have to think unless they want to steer hard.

Do not ask what the library or the conversation already answers — when the
request arrives with the process described, or the session already contains the
work being encoded, reflect it back in a sentence rather than asking again.

Mark genuine unknowns `[NEEDS DECISION]`; do not invent inputs, questions or
boundaries to fill a slot. At **Intake** and at **examples**, always present
"none / not applicable" as a visible option even when recommending otherwise —
a builder that cannot say "this skill needs no inputs" will manufacture some.

A complete skill from one paragraph of intake is a failed interview, not a
shortcut.

## 3. The gate

Never start with the name, the folder, or the SKILL.md. Start with the work.

Ask: **is this a method that repeats, carries judgement, and has an output
someone can recognise as right or wrong?**

A skill needs **all four**:

- **Repetition** — it will be invoked more than a couple of times.
- **Judgement** — encoding it saves real thinking, not just typing. Pure
  determinism is a script.
- **A defined output** — an artifact, a decision, a structured answer.
- **A statable boundary** — what it does *not* do, and who it hands to.

If it fails, recommend the lighter home and stop:

| The need is really | Home |
| :----------------- | :--- |
| A stable fact, a client context, a canon | a **context note** — `CONTEXT.md`, a vault note, a training doc |
| A way of working that applies to every task | a **mode** — `AGENTS.md`, project instructions; not a worker and not a skill |
| Something done once | **just do it**, or a prompt |
| Recurring work with a trigger and an output | a **routine** — hand to `routine-design` |
| A standing role holding judgement across many tasks | a **persistent agent** — hand to `agent-design` |
| Several passes that must not share a context, or human sign-offs between stages | a **workflow** — hand to `workflow-design` |
| Deterministic steps with no judgement | a **script** the skill calls, or a script on its own |
| A missing branch of something that already exists | an **edit to that skill** |
| Reference material several skills read | the repo's **shared training material**, not a skill and not inside one |

Say it plainly. "This is an edit to `gtm:positioning`, not a new skill" and
"this is a routine, not a skill" are successful outcomes of this skill, not
failures to deliver. In a library of any size, the edit is the most common
right answer.

## 4. Audit overlap

Read the library from §0, then check, **by purpose and not by name** — two
positioning skills are a duplicate even when one is called something else:

- Does an existing skill already own this method?
- Is this a new method, or a new entry point to one that exists?
- Could this be a branch, mode or reference file inside a neighbour?
- If two skills will cover adjacent ground, which one wins on an ambiguous
  request, and does each say so?

Prefer **extending an existing skill** over adding one. Prefer a **smaller set
with sharper boundaries** over a large catalogue that competes with itself.

Name every overlap and resolve it explicitly — merge, split, hand off, or state
why both exist. The resolutions become the `not for X, hand to Y` lines in box
1 and the near-miss queries in box 5. Skip this in **reject** when no library
is readable; do not skip it in **design**, **restructure** or **review**.

## 5. The five boxes

Fill one box at a time. Do not move on while a box holds an unresolved decision
— mark it `[NEEDS DECISION]`. Keep the language operational: a reader should be
able to predict what the skill does and what it refuses.

If a box needs more than about five lines, the scope is wrong — split the skill
or push the detail into a reference file.

### 1. Job

```text
Method: every time X happens, produce Y
Also covers:
Does not cover (exclusions):
Hands off to:
```

State the job as "every time X happens, produce Y" — if that sentence will not
form, the gate was passed too generously. The **exclusions** matter as much as
the mandate: name the adjacent work the skill hands back rather than absorbing,
and name the neighbour it hands to. Choose the name last, kebab-case and
descriptive of the method (`proposal-writer`, `win-loss-analysis`).

### 2. Trigger

```text
Description (what it does AND when to use it):
Trigger phrases (the principal's actual words, 3-5):
Competes with:
Explicitly not for:
```

This is the frontmatter `description`, and it is the only thing that decides
whether the skill ever runs. Get it drafted and signed off here, not at build
time.

**All when-to-use information lives in the description.** The body loads only
after the skill has triggered, so a "when to use this skill" section in the
body cannot affect discovery — it is dead weight that reads like diligence.

Draw the trigger phrases from what the principal would actually type, not from
the skill's own vocabulary. Lean slightly pushy: skills under-trigger far more
often than they over-trigger, so "use whenever someone mentions X, even if they
do not ask for it by name" earns its place. Then bound it — the `do not use
this for` clause is what stops a pushy description from stealing its
neighbours' work, and §4 has already named them.

### 3. Intake

```text
Required inputs: <list> | none
Asked at invocation if missing: yes | n/a
Per-run questions: <list> | none
```

Two separate questions, both of which are legitimately answered "none".

**Required inputs** are what a run needs to start — a file, a URL, a client
name. Many skills need none and work from the workspace. If a run needs them,
the skill states them and asks for anything missing before doing other work.

**Per-run questions** are only for decisions that genuinely vary run to run and
cannot be encoded. Anything a good default settles is not a question. Any that
survive get written into the skill in recommend-then-confirm form — the skill
leads with its recommended answer plus alternates, so its user can confirm in a
word.

### 4. Method

```text
Steps (ordered, one line each):
Artifact and where it lands:
Template source: <real past example> | <to be supplied> | n/a
Self-check (definition of done):
```

Lay out the ordered steps and show the whole sequence for confirmation before
anything is written.

**Mine the template from real work.** If the process has been done by hand
before, the past outputs are the template — a real example aligns a skill's
output better than any description of one. Go looking for them before inventing
a format; if none exist, ask for one or say plainly that the format is
invented.

The **self-check** is what the skill runs against its own output before
declaring a run complete. It is box 4's last line because it is the definition
of done for the method, not an afterthought.

### 5. Placement and proof

```text
Plugin / location:
Status: draft | trial | active | degraded | retired
Test 1 — trigger:
Test 2 — core job:
Test 3 — boundary:
Pass condition:
Review date:
```

Placement is chosen **after** the job, trigger, intake and method are settled —
which plugin a skill belongs to is a distribution decision, not part of its
identity. Ask rather than assuming; a skill in the wrong plugin is invisible to
the person who needs it.

Every new skill enters at `trial` with a named review date. Trials expire
unless renewed; an expired trial becomes `dormant` — dropped from the build,
record kept.

The three tests, run against real work:

1. **Trigger** — does it fire on the phrases from box 2, and stay quiet on its
   neighbours' work? Run the trigger eval: `references/trigger-eval.md`. This
   is the cheap one and the one that catches the failure that actually
   happens — in a library of any size, collision with a neighbour is more
   common than a bad method.
2. **Core job** — one real invocation against real material. Is the artifact
   good enough to use unedited? Who judges is the principal, not the skill.
3. **Boundary** — an out-of-scope request that sits just outside the
   exclusions. Does it decline and reroute to the named neighbour, or does it
   have a go anyway?

Pass condition covers all three. A skill that keeps failing the same test is
retired or rewritten, not re-trialled indefinitely.

Full with-and-without benchmarking — running the task twice, once with the
skill and once without, and comparing — is the **advanced extension**, not the
default. Escalate to it only when **both** apply: the output is objectively
checkable, and the skill will run often enough to repay the setup. For
subjective work (writing, design, strategy) it measures nothing the principal
cannot see faster by reading two outputs.

## 6. The shape

One decision, made after the boxes are filled and recommend-then-confirm like
the rest. Recommend the simplest shape that holds the method:

- **Simple** (the default): one SKILL.md, plus a template file if the artifact
  has a defined format. Right when the method fits in a page or two.
- **Structured:** SKILL.md carries order and orchestration only; each step's
  detail unpacks into a topic-named file. Add reference files for material the
  skill consults, and scripts for anything it executes. Right when the SKILL.md
  would otherwise sprawl.
- **Phased** (rare): for genuinely large processes, where each phase
  orchestrates its own steps. Do not reach for this until structured has
  actually strained.

**Structure must be earned by real complexity, never added on spec.** A
skeleton of empty folders is a worse skill than a whole one-pager.

Wherever structure is used, **order lives only in the orchestrator**. SKILL.md
carries the numbering and points at each file; the files themselves are
unnumbered, topic-named and position-agnostic — no "in the previous step", no
"before moving to step 4". Steps get reordered, split and dropped as a skill
improves; when order lives in one file that is a one-file edit, and when it is
baked into filenames and prose it is a rewrite with stale instructions left
behind.

The full canon — progressive disclosure, what belongs in reference files, what
never belongs in a skill folder, and the writing rules — is in
`references/conventions.md`. Read it before building and check the finished
skill against it before handing off.

## 7. The outputs

Emitted in **design**. Other modes reuse a subset.

1. **The skill** — SKILL.md plus whatever the shape earned, written complete.
   A skill with stub files is worse than a simpler skill that is whole.
2. **The trigger eval set** — the queries from box 5 test 1, saved beside the
   skill in the plugin repo but **not inside the skill folder**: it is not a
   file a run uses.
3. **The trial card** — the three tests, the pass condition and the review
   date, with the result column empty until **review**.
4. **The placement diff** — the proposed change to the plugin repo, shown
   before it is written.

## 8. What each mode does

**design.** Substrate → gate → overlap → five boxes → shape → outputs. Status
`trial` with a named review date. Propose the diff; do not write it silently.

**reject.** The gate table, the recommended home, and one line on what to do
instead. Where the answer is "edit an existing skill", name the skill and the
specific change. Stop — no folder, no SKILL.md.

**restructure.** Read the current skill in full and list what it does before
changing anything. Note where it strains: an overlong SKILL.md, duplicated
instructions across steps, ordering baked into filenames or prose, hardcoded
values that should be inputs, a when-to-use section in the body. Re-run the
shape decision (§6) and move detail into files — the method does not change
unless the restructure exposed a genuine gap, which is a **review**. Every
instruction in the old skill goes somewhere or is listed as dropped, with a
reason. Nothing disappears silently.

**review.** Load the skill and run the three tests against real work. Then
recommend exactly one: **keep**, **revise** (with the specific diff), or
**retire**. Two things to look for that the tests will not surface on their
own: parts of the output that get edited the same way every time (promote the
edit into the skill), and sections that never get used (cut them). Skills get
good by being run, not by being designed — expect the shape to change, and
expect some of what was predicted at design time to have gone unused.

**retire.** Drop the skill from the build and keep the record. Do not delete
history. Where something still needs the method, say where it went.

## Pitfalls

1. **Designing the SKILL.md instead of the capability.** The file is a
   generated artifact. Start from the method and the exclusions.
2. **A new skill where an edit was wanted.** The most common failure in a
   library that already covers the ground. §4 exists to catch it; skipping it
   is how a catalogue starts competing with itself.
3. **Structure added on spec.** Empty `steps/` folders and one-line reference
   files look like rigour and behave like debt.
4. **Order baked into the steps.** Numbered filenames and "as established
   above" survive every reordering and quietly mislead.
5. **When-to-use in the body.** It loads after the decision it was meant to
   inform. It only ever works in the description.
6. **A description with no boundary.** Pushy earns triggering; unbounded steals
   from neighbours and makes the whole library less reliable.
7. **Inventing inputs and questions to fill the slots.** "None" is a real
   answer at Intake and at examples, and the interview must show it as one.
8. **Inventing the template.** When past outputs of the work exist, the format
   is mined from them. A format invented from a description produces output
   that reads like it was.
9. **ALL-CAPS MUSTs standing in for a reason.** Explain why something matters
   and a capable model will generalise; stack imperatives and it will follow
   them past the point where they help. Caps are a yellow flag that the
   reasoning has not been worked out yet.
10. **Overfitting to the test cases.** Fixing the three examples in front of
    you is not the same as fixing the skill. If an issue is stubborn, try a
    different framing rather than a narrower rule.
11. **Skipping the trial.** An untriggered, untested skill in a shared build is
    not a shortcut — it is a skill that nobody will ever know failed.
12. **Benchmarking subjective work.** Assertions on writing quality create
    false confidence. Read two outputs instead.

## Reference files

- `references/conventions.md` — the skill canon: structure, progressive
  disclosure, file placement, writing rules, and the three shapes. Read before
  building; check against it before handing off.
- `references/trigger-eval.md` — how to build the query set for test 1, and how
  to run it. Read at box 5, or whenever a skill is firing on the wrong things.
- `references/worked-example.md` — one filled design and one gate rejection.
  Read when the shape of a good pass is unclear.
- `scripts/trigger_eval.py` — runs the query set and reports trigger rate,
  precision and recall, and which neighbour fired instead on a miss.

## Verification checklist

- [ ] Substrate resolved: installed library read, plugin source located, and
      the absence of either stated rather than guessed
- [ ] Mode named (design / reject / restructure / review / retire)
- [ ] The gate was applied against all four criteria
- [ ] A lighter home was recommended wherever the need failed the gate
- [ ] Overlap checked by purpose against the installed library, and every
      near match resolved explicitly
- [ ] All five boxes complete, or open items marked `[NEEDS DECISION]`
- [ ] Exclusions stated, with a named neighbour to hand to
- [ ] All when-to-use information is in the description; none in the body
- [ ] "None" was offered as a visible option at Intake and at examples
- [ ] Template mined from real past work, or its absence stated
- [ ] Self-check present and specific enough to fail against
- [ ] Shape is the simplest that holds the method; no speculative folders
- [ ] If structured: order lives only in SKILL.md, step files unnumbered,
      topic-named and position-agnostic
- [ ] Every unpacked file is linked from SKILL.md with a note on when to read it
- [ ] Nothing in the skill folder that a run does not use — no README, no
      changelog, no notes on how it was made
- [ ] Prose is imperative, and reasons are given rather than capitalised
- [ ] Placement chosen last, and asked rather than assumed
- [ ] Trigger eval set written and saved outside the skill folder
- [ ] Three tests, a pass condition and a review date exist; status is `trial`
- [ ] Any repo change proposed as a diff, not written silently
