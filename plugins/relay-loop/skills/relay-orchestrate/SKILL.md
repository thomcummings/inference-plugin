---
name: relay-orchestrate
description: "Use when running one issue through the Relay loop to a PR."
---

# Relay orchestrator

The sequencing layer over relay-spec, relay-build and relay-review. One
invocation takes a ready issue as far as a merge-ready PR without the operator asking
for each stage: builder pass → independent review → fix rounds until
`{loop_name}-approved`, or an escalation lands in the room as a question.

The orchestrator never builds and never reviews. Its job is to hold the state
machine, dispatch one fresh agent per stage, verify each stage's outcome
against the tracker and the PR (never against the agent's say-so), and stop
at the gates that are human by design.

## When to use

The user types `/relay-orchestrate INF-123` (any ID on a configured team) or
asks to run an issue through the loop without hand-holding each stage. The ID
may already be `{loop_name}-ready` (run it) or `{loop_name}-draft` (report the
gate, or run the spec interview in-room if the user is present and asks).

## Lane discipline

- **A fresh agent per stage.** Builder, reviewer and any overlay reviewer are
  separate passes in separate contexts. Never review in the same context that
  built, and never fold the orchestrator's own judgement into a verdict.
- **Verify gates live, every dispatch.** Tracker labels, issue state, PR labels
  and head SHAs all move between turns. Re-fetch in the same turn you act on
  them; report unverified as unverified, never as absent.
- **Never merge, never enable auto-merge.** `{loop_name}-approved` is evidence
  for a human, not merge authorisation. The merge is the operator's.
- **Never apply `{loop_name}-ready` autonomously** — one exception, see §2.
- **Never answer an escalated product decision.** Surface it in-room in the
  three-line shape (§7) and stop. Deciding is the operator's; you may give a read.

## The state machine

```
/relay-orchestrate <ID>
  │
  ├─ 0. map ID → repo (relay.config.md initiative)
  ├─ 1. gate check (fresh read of the issue)
  │      ├─ already has an open PR → resume at the right stage (§1)
  │      ├─ not ready → gate report, or spec interview in-room (§2) → end
  │      └─ ready → continue
  │
  ├─ 2. BUILD  — one fresh builder pass (relay-build) in a clean clone
  │      └─ pass fails → failure ladder (§3); never blind-redispatch
  │
  ├─ 3. OVERLAY REVIEW (only when the repo's AGENTS.md mandates one) — fresh
  │      agent at the settled head SHA
  │
  ├─ 4. REVIEW  — one fresh reviewer pass (relay-review)
  │
  └─ 5. verdict loop (cap: 2 fix rounds, then force a human call)
         approved ──► report "ready to merge" → end
         human    ──► escalate in-room, three lines → end
         changes  ──► FIX pass (relay-build picks up the -changes PR)
                      → re-REVIEW → loop
```

Stages are strictly sequential. Two builder passes must never share one
workspace, and a re-review must never run while a fix pass is mid-flight on
the same PR.

## 0. Map the ID to a repo

Read the issue's team and project. Match against the loop setup declared in
`relay.config.md`; when in doubt read each candidate's `relay.config.md` and
compare `initiative` and `team` to the issue before committing to a repo. Never
guess. When the issue belongs to no configured setup, ask which repo to run in.

## 1. Gate check — fresh, same turn

Fetch the issue with relations. Green to build when ALL hold:

- status is not Done / Canceled;
- carries `{loop_name}-ready` and not `{loop_name}-blocked`;
- no unresolved blocker relation;
- not already assigned to a live builder pass (stale claims surface via the
  lane lock at build time — don't over-police).

**Already has an open PR for this ID?** Resume instead of rebuilding: no
`{loop_name}-*` terminal label and no newer verdict than the head SHA → go
straight to §4 review. `{loop_name}-changes` → go straight to the fix pass in
§5. `{loop_name}-approved` with head unchanged → the loop is done; report it.
`{loop_name}-human` → that is parked for the operator; surface what it needs and end.

Not green → give the gate report, one line per missing condition, and the
next action. Do not invent work, do not pick another issue, do not proceed.

## 2. Spec stage — two modes

The default on a `{loop_name}-draft` issue is a **gate report**, not a spec
run: the interview is where product decisions get made, and the human owns
them. The report says: the issue is a draft, here is what readies it, apply
`{loop_name}-ready` when it survives your read.

**Spec mode** runs only when the user asks for it explicitly in the same
invocation (`/relay-orchestrate INF-123 spec`), or says so in the room: run
relay-spec here, in this session, interactively — every product decision is
asked, never guessed. It files the issue (or chain) with `{loop_name}-draft`.

Then the hard rule binds: **`{loop_name}-ready` is the human's final read.**
Agents never apply it autonomously. The one exception: the user, in this
session, after seeing the filed draft, explicitly says to ready it — then you
apply the label as their instructed action and record the read on the issue
comment: "Readied in-room by the operator on <date> — final read done here." Without
that explicit instruction, stop after filing and hand back: "Spec filed —
read it, then say 'ready it' or apply relay-ready in the tracker, and I'll run the
loop." A chain is readied one issue at a time; orchestrate only the issue the
user actually readied.

## 3. Build dispatch

One fresh builder pass, established shape: `relay-build` loaded, run against
a clean clone or isolated worktree of the repo so the operator's own checkout
is never dirtied. Background the pass with a completion notification (the
build may take several minutes). Ensure the builder's environment has:

- Git auth to the VCS (e.g. `gh auth status` under the right token)
- A clean checkout at the default branch tip
- The correct runtime toolchain for the repo (Node version, Python venv, etc.)

The builder's own lane lock and cooperative claim protect the workspace and
the tracker — do not duplicate them, and do not launch a second build into
the same workspace while one is out.

**Verify the outcome, don't relay it.** When the pass reports done: read the
PR list for the repo and the issue state fresh. The pass shipped only when
there is an open PR carrying `Closes {ID}` and the issue has no
`{loop_name}-*` terminal label (the awaiting-review resting state). Audit the
builder's claim before passing it on — read its output for unrun or
unverifiable checks (browser checks with Chrome unavailable, CI status behind
a scope-limited token) and route those as open items, not completed work.

Pass failed → read the live transcript, classify the death: did the builder
fail mid-research (salvage findings, nothing else) or mid-implementation (check
the worktree for uncommitted work and whether the lane lock moved)? Redispatch
once with research handed forward as directives, and on a second failure complete the pass yourself under the
same contract with full disclosure ("completed by the orchestrating agent
after dispatched passes failed"). A third blind dispatch wastes the operator's time.

## 4. Overlay reviews (per-repo)

When the repo's AGENTS.md mandates an independent review before a human merge
decision, dispatch it between build and relay-review as its own fresh pass at
the settled head SHA — never fold it into the Relay review, and never let the
builder run it. A PASS WITH FOLLOW-UPS verdict behaves like review feedback:
ratify its follow-ups, then run the fix pass. New commits invalidate the prior
verdict, so an overlay review that pre-dates a fix push must be re-run at the
new head before the loop can finish.

## 5. Review dispatch

One fresh reviewer pass (`relay-review`) once the PR's checks are green and
the head is settled. relay-review finds the PR itself; you dispatch the pass
and then read the labels it left.

## 6. Verdict handling — the fix loop

Read the PR labels fresh after the review pass:

- **`{loop_name}-approved`** → loop complete. Report: PR link, verdict,
  checks, and that the merge belongs to the operator. End.
- **`{loop_name}-human`** → escalate in-room (§7). End. Never auto-answer.
- **`{loop_name}-changes`** → one fix pass (a fresh relay-build dispatch
  picks up `-changes` PRs by itself — its step 1 reads the verdict's Must-fix
  list), then re-review at the new head. **Cap at 2 fix rounds.** If the
  third verdict is still `-changes`, do not keep burning tokens on a loop the
  machine isn't converging: force a human call — add `{loop_name}-human` to
  the PR and issue (mirror both), post the round history in the escalation,
  end.

The verdict's ledger governs the fix — the reviewer's reading of each `AC-N`
was written before the code was read. Where the fix would cross an `NG-N` or
needs a product decision, relay-build already escalates it to
`{loop_name}-human`; treat that as a stop, not a fix.

## 7. Escalation shape

When the loop needs the operator, put the escalation in the room in exactly three
lines (same shape relay-review uses for `needs you` verdicts):

- **Deciding:** the question in one sentence.
- **Options:** the two or three real ones.
- **My read:** your recommendation, and why it is still his call.

Back it with the round history (PR, verdict SHAs, what each round changed)
when the cap forced the call. Then stop — the loop resumes on his answer, not
on your inference of it.

## 8. Completion report

State and next action first, then short bullets — mirror the family's writing
rules (verdict first, no throat-clearing, exact numbers, name unrun checks).
Always say **who did what** (builder / reviewer / overlay / orchestrator), so
the operator can tell which agent produced which artefact. One line: what shipped,
what each gate said, what is left for the operator (usually: merge).

## Hard limits

- Never merge or enable auto-merge; never review or build in your own context.
- Never apply `{loop_name}-ready` without the user's explicit in-room read (§2).
- Never answer an escalated product decision.
- Never run two passes into one workspace, or review while a fix is mid-flight.
- Never redispatch the same failing stage a third time without completing it
  yourself, disclosed.
- Never report a stage done from an agent's summary — verify against the
  tracker, the PR and the head SHA first.

Sibling contracts: relay-spec (interview + filing), relay-build (builder
pass), relay-review (reviewer pass).
