# Relay Loop

A Claude Code plugin that runs an issue from a rough idea to a merge-ready PR
through a disciplined, human-gated agent loop, then carries it on through QA
and a weekly release. Twelve skills that work together (or standalone) to give
you the rigour of a well-run product and engineering team without the headcount.

Built on the conviction that the value of agentic coding isn't raw autonomy —
it's **discipline applied at the boundaries**. Relay's job is to make sure the
right agent does the right pass, never reviews its own work, and never decides
the things a human should decide.

## What it does

You give it a tracker (Linear, GitHub Issues, whatever you configure) and a
repo. Relay turns raw ideas into build-ready issues, builds them one at a time
in isolated workspaces, reviews each PR against its written contract, and loops
on fixes until the work is either approved or parked in front of a human.

```
spec → ready → build → review → approved / changes / human → merge → wrap
                ↑                    │
                └──── fix pass ◄─────┘

release branch → QA sweep → release → retro
```

### The core loop

Six skills, each one pass, each runnable on its own:

- **`relay-spec`** — interviews you about a raw idea until a spec is so precise
  that two different agents would build the same thing, then files it (or an
  ordered chain of issues) in your tracker. *Opens the book.*
- **`relay-batch`** — specs several unspecced tickets in one session: pick from
  a ranked list, interview each in turn, then dispose of each draft (ready /
  parked) in one closing gate. *The morning-coffee pass over the backlog.*
- **`relay-build`** — claims the next gate-labelled issue, implements it against
  its acceptance criteria, verifies, and opens a PR with an evidence ledger.
- **`relay-review`** — independently reviews an open PR against the *issue*, not
  the PR's own account of itself, and posts a three-group verdict
  (must-fix / should-fix / safe).
- **`relay-orchestrate`** — runs one issue through the whole loop without you
  asking for each stage; escalates only the decisions that are yours by design.
- **`relay-wrap`** — checks the loop actually reached a terminal state, surfaces
  anything left undone, and tells you whether the thread is safe to archive.
  *Closes the book.* Explicit invocation only.

### Around the loop

- **`relay-decide`** — puts one decision in front of a busy owner so it can be
  answered cold: what and where, why now, a picture of each option, and a
  recommendation. Keeps every open call in one needs-you list.
- **`relay-design`** — gets app UI right before and after it's built: frames the
  problem, explores genuinely different options at real sizes and states, runs
  them past an independent critic and automatic layout checks, converges on a
  design contract, then checks the build matches it.
- **`ui-analysis`** — turns a design image or URL into a structured spec
  (tokens, components, implementation notes) a builder can work from.
- **`relay-qa`** — a release-candidate QA sweep: cheap tester agents, each with
  one lens, try to break the real build; one auditor reproduces and files only
  confirmed bugs. Never fixes code itself.
- **`relay-release`** — runs one release a week as PM across agent threads:
  scope, release branch, daily needs-you list, freeze, store builds, tags and
  the one release PR to main.
- **`relay-retro`** — reviews how the owner and their agents have worked
  together over a period and returns a short, ranked set of changes worth
  formalising.

## Why it's built this way

The single most important rule in the loop is **separation of concerns**:

- A builder that reviews its own PR reads the contract through the code it just
  wrote — the verdict then confirms the build's interpretation instead of
  testing it. So building and reviewing are always separate passes, and review
  writes its ledger from the issue *before* it reads a line of code.
- The loop is coordinated by **labels, not opinions**. `relay-ready` means a
  human has read the spec; `relay-approved` is evidence for a human, never merge
  authorisation. An agent can drive the machine, but the human owns the gates.
- Every stage re-verifies its gates live against the tracker and the PR head
  SHA. Nothing is trusted from a previous turn or another agent's summary.

This is a workflow for teams that want agents to *do the work* without letting
the work quietly redefine itself. The loop's discipline holds whether one agent
runs every stage (as long as each is a fresh context) or a fleet does.

## Installation

```bash
/plugin marketplace add thomcummings/inference-plugin
/plugin install relay-loop@inference
```

The skills then load namespaced by plugin, for example
`/relay-loop:relay-spec`, `/relay-loop:relay-orchestrate` or
`/relay-loop:relay-qa`.

## Usage

### One-shot (a single skill)

```bash
# Turn a rough idea into a build-ready issue (interactive — you answer)
/relay-loop:relay-spec "Add a usage dashboard"

# Spec several unspecced tickets in one session (pick, interview, dispose)
/relay-loop:relay-batch

# Build the next ready issue in this repo
/relay-loop:relay-build

# Review open PRs that need a verdict
/relay-loop:relay-review

# Check a finished thread is safe to archive
/relay-loop:relay-wrap
```

### Full loop (orchestrated)

```bash
# Run one issue end to end — it'll stop only for your gates
/relay-loop:relay-orchestrate PROJ-123
```

`relay-orchestrate` will: gate-check the issue, dispatch a builder in an
isolated clone, run the review, loop on fixes (capped at two rounds, then it
forces a human call), and hand you a merge-ready PR — or park an escalation in
front of you with exactly three lines: *Deciding / Options / My read*.

### Around a release

```bash
# Kick off this week's release, then sweep the candidate for bugs
/relay-loop:relay-release
/relay-loop:relay-qa

# Put a waiting decision in front of the owner
/relay-loop:relay-decide

# Look back at how the work went
/relay-loop:relay-retro
```

## Configuration

Each skill reads `relay.config.md` from the repo root (or `./.relay/config.md`).
If it's missing, the skill prompts for the pieces and offers to save. The config
declares:

- `tracker` and `team` — where issues live (Linear, GitHub Issues, …)
- `loop_name` — the label prefix that drives the whole loop (default `relay`)
- `initiative` / `project` — how a spec resolves to the right project
- `vcs`, `default_branch`, `branch_pattern` — repo mechanics
- `policies` — optional rules the reviewer enforces (e.g. "client-visible
  changes need a changelog entry")

A minimal example:

```yaml
# relay.config.md
loop_name: relay
tracker: linear
team: Product
initiative: Website
project: "[varies]"
vcs: github
default_branch: main
branch_pattern: "{ID}-{slug}"
```

## The labels (the loop's nervous system)

| Label | Meaning | Who applies it |
|-------|---------|----------------|
| `relay-draft` | Spec written, not yet read — or deliberately parked | relay-spec / relay-batch |
| `relay-ready` | A human read the spec; safe to build | **A human — never an agent** |
| `relay-blocked` | A pass needs an answer before it can continue | relay-build |
| `relay-changes` | Review found must-fixes on a PR | relay-review |
| `relay-human` | Needs a human decision before the loop resumes | relay-review / relay-build |
| `relay-approved` | Independent review passed; evidence for a human | relay-review |

The asymmetry is deliberate: agents apply every label *except* `relay-ready`.
When relay-spec or relay-batch files a draft, the operator chooses its
disposition in the same session — **ready** (the agent applies `relay-ready`
as the operator's instructed in-room read, recorded on the issue) or **park**
(leaves it as a deliberately-saved `relay-draft` for a later cold read). The
agent never readies anything on its own; the human owns that boundary.

## Architecture & design principles

- **Fresh context per pass.** Never review in the context that built. Where the
  runtime supports it, each pass runs in its own subprocess/session so no
  stage inherits another's reading of the work.
- **Read the contract, not the PR's self-report.** The reviewer writes its
  ledger (what each `AC-N` demands) before opening the diff or the PR
  description, so it checks the work against the agreement — not against the
  builder's account of the agreement.
- **Concurrency-safe by construction.** Builders take a lane lock and push
  without `--force` (a rejected non-fast-forward push means another pass won —
  discard, don't reconcile). Reviewers write only one verdict at the very end,
  behind a check that discards a verdict another pass beat them to.
- **File-based state, no infrastructure.** Everything coordinates through
  `relay.config.md`, repo labels and PR comments. No databases, no services.
- **Escalations are shaped.** When a decision is the human's, the loop says so
  in exactly three lines — deciding question, real options, recommendation —
  and stops. It never guesses the answer and resumes on the human's call, not
  its inference of it.

## When NOT to use this

- Repos where you're happy for agents to push straight to main with no
  contract and no independent read. Relay would be overhead, not rigour.
- Work that is genuinely exploratory and shouldn't be gated by a spec. Use it
  when the *outcome* matters and is describable; use a loose experiment loop
  when you're still finding the question.

## Credits and philosophy

Built from the operating method Inference uses to run real product and client
work through an agent loop: the point was never maximum autonomy, but maximum
trust in the work an agent hands back. When a machine can build, review and fix
on its own, the scarce thing is *judgement at the gates* — so the loop spends
its discipline there. It's the difference between an agent that does everything
and an agent that can be relied on.

## Licence

MIT. See [LICENSE](../../LICENSE) at the root of this repository.
