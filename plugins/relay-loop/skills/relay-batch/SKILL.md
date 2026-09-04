---
name: relay-batch
description: "Pick a set of unspecced tickets, interview them one after another in a single session, and dispose of each approved draft — ready or deliberately parked — in one closing gate. Use to run the Relay spec in batch mode. Interactive — the user is present and owns every product decision; never runs unattended."
---

# Relay batch

A front-door layer over relay-spec for the days when several unspecced tickets
are waiting. Instead of one idea per session, relay-batch surfaces the
candidates, lets the operator choose a set, interviews each chosen ticket to a
draft in sequence, and closes with a per-ticket disposition — ready or
deliberately parked.

relay-batch **composes** relay-spec; it does not fork it. Each individual
interview inside a batch follows relay-spec's rules exactly: rounds of 1–4
genuine product questions, the confidence test per ticket, never unattended.
The batch adds only the selection screen, the sequential session shape, and the
closing disposition gate.

The operator's attention is the bottleneck — the machine can always take more
work than the operator can review. relay-batch concentrates that attention into
one efficient sitting and never adds downstream load beyond what the operator
signs for in the session.

## When to use

- The operator opens the session wanting to spec several tickets in one go.
- A queue of unspecced work has built up and nothing has surfaced which tickets
  most deserve attention.
- The operator wants to clear a backlog of ideas into build-ready drafts (or
  deliberately park them) in a single pass.

Don't use for a single idea — that is plain relay-spec. Don't use for the truly
large (a multi-issue chain or a strategy-shaped question that needs its own
conversation) unless the operator, after the advisory flag, chooses to keep it
in the batch.

## 0. Load config

Read `relay.config.md` (repo root, then `./.relay/config.md`). If missing, ask
for tracker, team, `initiative`, `project`, and `loop_name`, then offer to save
it before continuing. Labels and skill prefixes come from `loop_name`. A batch
session targets the configured team and its projects.

## 1. Selection — the candidate list

Query the tracker for unspecced open work on the configured team:

- tickets labelled `needs-relay-spec` (the explicit "unspecced work" marker);
- `idea`-labelled open tickets that have sat unlooked-at;
- `{loop_name}-draft` tickets whose draft is already written (labels drifted —
  these surface the hygiene case, not a spec need);
- any open ticket blocking other open work (the highest-value specs: spec'ing
  them unblocks a downstream build).

Present the candidates as a checkbox list, **ranked** by priority, then
due-soonest, then blocker-count, then oldest. Give each row a one-line reason —
why it surfaced (due soon / unblocks 2 / stale idea / P1). Keep it a skim-list.

The operator may add any ticket by ID or title beyond the auto-pool. There is
**no cap** on how many tickets a session may take, and no warning at any count.

## 2. Interview — one ticket at a time

After selection, interview each chosen ticket **sequentially** — one fully to a
spec draft, then the next — using the relay-spec interview rules: research
before asking, rounds of 1–4 genuine product questions, the confidence test per
ticket:

> Could two different people read this spec and ship the same observable outcome?

Run the interviews as real relay-spec interviews, one after another, in this
session. The operator is present and owns every product decision; never guess,
never batch-attend.

## 3. Scope triage — advisory, never enforced

When a ticket's interview reveals it is large or chain-shaped, flag it:
"this one is looking like it deserves its own session — your call." The skill
guides; it never refuses. If the operator says keep it, keep it — it runs the
same rounds and confidence test as any other ticket, even if it takes more
rounds. Only the truly large get flagged; a moderately large ticket that stays
coherent in one issue stays in the batch.

## 4. Filing and disposition — one closing gate

When all chosen tickets have reached a draft, the session ends with one closing
gate. For each ticket, show its draft and let the operator choose a
disposition:

- **Ready** — apply `{loop_name}-ready` now (as the operator's instructed
  in-room read; record "Readied in-room by the operator on <date> — final read
  done here" on the issue). The loop may then continue.
- **Park** — leave `{loop_name}-draft`; deliberately saved for a later cold
  read. Parked is an active choice.
- **Drop** — discard the draft; the ticket was not worth spec'ing.

One apply action commits the kept set to the tracker with their dispositions.
Then give the batch-end report: the split — N readied (the loop may pick these
up) and M deliberately parked (awaiting a later read). Readied tickets flow to
orchestration only when the operator runs the loop; parked tickets never
auto-ready or auto-orchestrate.

## Resume — if the operator steps away

If the session is interrupted mid-way, the operator may resume later. Re-open
only the ticket that was in progress — never re-ask answered questions, and
preserve already-filed tickets and dispositions. If the operator doesn't
remember where things stood, ask; never guess at their place in the batch.

## Hard rule

Never apply `{loop_name}-ready` autonomously or by batch default. It is applied
only as the operator's explicit per-ticket choice in the closing disposition
(or their later in-tracker read). relay-batch never auto-orchestrates anything
it filed. This skill never runs unattended.

Sibling contracts: relay-spec (interview + filing + the two-option ending),
relay-orchestrate (runs a readied issue to a merge-ready PR). This skill is the
batch front door over relay-spec's single-idea session.
