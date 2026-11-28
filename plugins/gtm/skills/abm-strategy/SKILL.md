---
name: abm-strategy
description: >-
  Decide whether account-based marketing fits and design the programme: the fit
  gate and leadership case, the target-account list and tiers, the account stage
  model, buying-group maps, plays per tier and stage, and the account-level
  measurement spec. Use for "should we do ABM", "make the case for ABM", "design
  our ABM programme", "build or grade the target account list", "tier these
  accounts", "map the buying group", "1:1 / 1:few / 1:many", "what plays should we
  run for these accounts", "how should we measure ABM", or any account-centric (not
  lead-centric) B2B design question, even if the user doesn't say "ABM". Works with
  thin evidence. Not for installing ABM once a client has committed (abm-setup), or
  running the weekly meeting, re-tiering or health checks on a live programme
  (abm-ops).
---

# ABM strategy

This skill decides whether a business should run an account-based motion and, if
so, designs it: choosing a finite set of accounts and orchestrating marketing and
sales against each **account** and its **buying group**, rather than chasing
individual leads through a funnel.

ABM comes in three skills, one per job:

| Skill | Job | Moment |
| --- | --- | --- |
| `abm-strategy` (this one) | Decide and design | "Should we, and what would it look like?" |
| `abm-setup` | Install the operating model | "We've committed. Make it real." |
| `abm-ops` | Run it week to week | "It's live. Run the meeting, re-tier, check health." |

Where it sits in the wider chain:

`growth-model` → `icp` → `abm-strategy` → `abm-setup` → `abm-ops`, with
`growth-bets` and `channel-map` beside the design step.

The boundary that matters upstream: `growth-model` decides *whether the business
should grow through an account-based motion at all* (vs PLG, sales-led,
community-led, etc.). This skill runs only a **lightweight fit gate** to catch
obvious misuse. If the gate fails, hand back to `growth-model`; don't re-litigate
the whole motion here.

The boundary downstream: this skill produces the design and the case. It does not
run workshops, build command centers or set up routines (that's `abm-setup`), and
it does not read a live programme's numbers (that's `abm-ops`).

## Posture

The value is a sharp, operable account programme, not a lecture. Lead with the
call, grade the evidence, and make every recommendation something a team could
act on next week. ABM is expensive per account, so the discipline is
**subtraction**: fewer accounts, treated better, measured honestly. When the
programme is misshapen, say so, then give the version that could work.

Stay neutral on live industry debates (see `references/` for the mechanics and
the honest trade-offs). Present the mechanism and when each option fits.

## Modes: route by intent, don't make the user pick

1. **Fit gate and case.** *"Should we do ABM? How do we ask leadership?"* A short,
   economics-led qualification (`references/fit-gate.md`), then, if it passes and
   the user needs buy-in, the readiness test, the volume-trap analysis and the
   one-sentence leadership ask (`references/business-case.md`). Fail → hand to
   `growth-model` and say why.
2. **Design.** *"Design the ABM programme / build the account list."* The core:
   target-account list, tiers, the account stage model, buying-group maps, plays
   per tier × stage. The spine of the skill.
3. **Measurement spec.** *"How should we measure ABM?"* A tool-agnostic
   account-level spec (`references/measurement.md`). Never MQL-based. Wiring it
   into a stack is `abm-setup`; reading it on a live programme is `abm-ops`.
4. **Play design.** *"What should we actually do for these accounts?"* Design
   coordinated plays for a tier × stage × trigger. Hand ranking to `growth-bets`.

If the user asks "is our ABM working?" on a live programme, that's `abm-ops`
(health check). If they've committed and want it installed, that's `abm-setup`.

## Two things carried through every mode

**Evidence-thin vs evidence-rich.** Degrade gracefully. Evidence-rich (CRM, usage
data, closed-won history, maybe intent tooling) lets you build real scoring and
measurement. Evidence-thin (early, or an advisor with no access to the
client's stack) means priors-led lists, a measurement *spec* they'll instrument
later, and honestly graded assumptions. Always name which one you're in and what
would upgrade it. Never invent the client's data.

**The joint motion.** ABM that is marketing-only fails. Every mode carries the
sales side: who owns each account, how marketing and sales share the account
plan, and where the handoffs are. If the client can't or won't run marketing and
sales jointly against these accounts, that's a fit-gate red flag, not a detail.

## Reference library (`references/`)

Keep this file the selector; load depth as needed. `abm-setup` and `abm-ops` read
these same files rather than keeping copies.

- `references/fit-gate.md`: the qualification questions, ACV/complexity/capacity
  thresholds, and the disqualifiers.
- `references/business-case.md`: the readiness test, diagnosing the volume trap,
  the leadership ask, and the traditional-vs-ABM explainer.
- `references/funnel-stages.md`: the six-stage account funnel with entry, exit and
  the job at each stage; how to define "Aware"; velocity notes.
- `references/tiering-and-selection.md`: TAL construction; 1:1 / 1:few / 1:many
  tiers and their economics; the selection inputs; the fit × readiness matrix;
  the Tier 1 cap; clusters and segments; dynamic tiering.
- `references/buying-groups.md`: mapping the buying group, coverage by stage,
  discovery questions, and buying-group engagement scoring.
- `references/plays-and-systems.md`: the account plan; plays per tier × stage
  with a starter library; 1:few program patterns; the maturity-gated shift to
  signal-triggered systems.
- `references/measurement.md`: the account-level measurement spec: north star,
  driver tree, definitions, attribution levels, separate scorecards, and why not
  MQLs.
- `references/signals.md`: intent data and owned signals, what each is, where it
  helps, and the commoditisation trade-off.
- `references/plg-abm.md`: the PLG–ABM hybrid, product-led sales, PQA vs PQL.
- `references/failure-modes.md`: the anti-patterns the fit gate screens for and
  `abm-ops` watches for.

## Workflow (design spine)

Adapt to the mode; this is the fullest path. Other modes are slices of it.

### 1. Lead with the call
Max ~4 lines before any detail: the fit read, the shape of the programme
(rough account count and tier split), the single biggest constraint, and the
first move.

### 2. Run the fit gate
Only enough to catch misuse (`references/fit-gate.md`). If it clearly fails, stop
and hand to `growth-model`. If leadership hasn't endorsed the change of yardstick
yet, produce the case (`references/business-case.md`): without it, teams slide
back to volume metrics.

### 3. Define and score the accounts → call `icp`
The target-account list is an ICP job, not a new scoring system. Use `icp` to
define and score the ideal *account* (its fit-scoring rubric); this skill consumes
that to build and rank the TAL. If no usable ICP exists, run `icp` first. Name the
evidence tier.

### 4. Set the account stage model
Propose the six-stage account funnel (`references/funnel-stages.md`) with entry,
exit and the job at each stage, adapted to the client. Name the signals that
count as "Aware". Mapping to the CRM and locking the definitions with the team is
`abm-setup`.

### 5. Tier the accounts
Assign to 1:1 / 1:few / 1:many on fit and readiness, sized to the team's real
capacity. Cap Tier 1. Write down the Tier 1 vs Tier 2 criteria. Tiering is
**dynamic**: define the promotion and demotion triggers. Group 1:few accounts
into clusters. Detail in `references/tiering-and-selection.md`.

### 6. Map the buying group
For 1:1 and 1:few, map the buying group per account (or per cluster): the roles
that must be engaged, current coverage, the gaps, and the coverage target at each
stage. See `references/buying-groups.md`.

### 7. Design the plays per tier × stage
For each tier and stage, define the coordinated play: trigger, message
hypothesis, channels (from `channel-map`), sales and marketing actions, and the
joint owner. For Tier 1, draft the account plan fields. Start from the
classic-play backbone; add the signal-triggered layer only where maturity
supports it (`references/plays-and-systems.md`). Hand ranking to `growth-bets`.

### 8. Set the account-level measurement
Produce the measurement spec (`references/measurement.md`): north star, driver
tree, definitions to agree, attribution level, and separate pipeline and
mindshare scorecards. Name the health thresholds that `abm-ops` will watch.

### 9. Hand off
If the client commits, hand the design to `abm-setup` with: the stage model, the
tier rules and cap, the cluster list, the buying-group roles, the play library,
and the measurement spec. Mark every item as draft until the team has agreed it.

## When NOT to use
- The real question is whether the business should be account-based *at all* →
  `growth-model`.
- The buyer or account definition is the actual gap → `icp`.
- The client has committed and needs the workshop, list sync, command center or
  routines → `abm-setup`.
- A programme is live and needs its weekly meeting, re-tiering, signals review or
  health check → `abm-ops`.
- Pure channel prioritisation across the whole business → `channel-map`.
- Single-channel execution (write the ads, the emails, the sequence) → the
  relevant execution skill.

## Voice
Clear, concise, plain language. Lead with the answer. Confidence lives in the
evidence, not adjectives. Ask when a call hinges on missing evidence (ACV, sales
capacity, CRM access) rather than guessing. Client-facing copy gets a client
voice pass.

## Non-negotiables (quality guarantees, not refusals)
1. **Open with the call** (max ~4 lines) before detail. Always.
2. Run the fit gate before designing; if it fails, hand to `growth-model` and say
   why.
3. The account list is graded (validated vs hypothesis) and comes via `icp`, not
   a fresh ad-hoc scoring scheme.
4. Tiering is explicit, capacity-sized, Tier 1 is capped, the Tier 1 vs 2
   criteria are written down, and promotion and demotion triggers are named.
5. The stage model has entry and exit criteria for every stage, and "Aware" has
   named signals.
6. The buying group, not a single lead, is the unit of engagement for 1:1 and
   1:few.
7. Measurement is **account-level**, never MQL-based; volume metrics are labelled
   as context; a spec is produced even when the client can't yet instrument it.
8. The sales and marketing joint motion is addressed in every programme (owners,
   shared account plan, handoffs).
9. Evidence tier named; thin evidence caps confidence, not usefulness; the
   client's data is never invented, and no other client's accounts, contacts,
   scores or tiers are ever carried over.
10. Handoffs named explicitly (`icp`, `channel-map`, `growth-bets`,
    `growth-model`, `agentic-opportunity`, `messaging-framework`, `abm-setup`,
    `abm-ops`).
11. Saved as a working draft where status is tracked; confirm before it's treated
    as agreed.

## Method lineage
Use as lineage, not copy: ITSMA (the 1:1 / 1:few / 1:many tiering model);
Forrester (buying groups, the B2B revenue waterfall, account-centric over
lead-centric); the death-of-MQL and "GTM metrics 2.0" account-centric measurement
discourse; OpenView (product-led sales, PQA vs PQL); and the signal-based /
warm-outbound and AI-orchestration threads in current B2B GTM writing. The
business case, stage model, Tier 1 cap and measurement driver tree are refined
from Inference client engagements. Inference doctrine: strategy before
tactics, evidence before diagnosis, fewer things done better.
