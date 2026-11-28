---
name: abm-setup
description: >-
  Install account-based marketing as a company's GTM operating model once it has
  committed: the kickoff workshop, locking the stage model and mapping it to the
  CRM, the target list as one source of truth synced to CRM, ad and visitor tools,
  the ABM weekly rhythm, a command center on top of the CRM, read-only signal
  routines, re-pointing channels at the list, and a 12-week rollout. Use for "we're
  doing ABM, make it real", "run the ABM kickoff workshop", "lock our stage
  definitions", "sync the target list", "build the ABM board / command center",
  "set up ABM signals or routines", "roll out ABM", "migrate from volume marketing
  to ABM". Not for deciding whether to do ABM or designing tiers and plays
  (abm-strategy), or running a live programme week to week (abm-ops).
---

# ABM setup

Takes a company from "marketing generates volume, sales picks leads" to "one GTM
team works a named list of accounts through an agreed funnel, measured by account
movement". This skill installs the operating model: the decisions, the list, the
rhythm, the tooling and the channel changes.

| Skill | Job |
| --- | --- |
| `abm-strategy` | Decide and design: fit, case, list, tiers, stages, buying groups, plays, measurement spec |
| `abm-setup` (this one) | Install it: workshop, locked definitions, list sync, rhythm, command center, routines, channels |
| `abm-ops` | Run it: weekly meeting, monthly re-tier, quarterly reset, signals review, health check |

**Entry condition.** Leadership has endorsed ABM as the operating model, with
account-movement KPIs replacing volume. If that hasn't happened, go to
`abm-strategy` (fit gate and business case) first. If there is no design yet
(stage model, tier rules, buying-group roles, play library, measurement spec),
draft it with `abm-strategy` before the workshop, or use the workshop to draft
it.

**Exit condition.** Two weekly ABM meetings have run, each ending with top
actions per function, and the acceptance checklist below is mostly ticked. From
then on the programme belongs to `abm-ops`.

This skill reads `abm-strategy`'s references for the method (stages, tiers,
buying groups, plays, measurement) and keeps only the install detail here.

## Non-negotiables
1. **Client separation.** Start with an empty list. Never carry account names,
   contacts, deal notes, scores, tiers, product names, people or internal tool
   names between clients. Re-derive the ICP rubric from this client's won deals.
2. **The target list is the critical path.** Plans, goals, dashboards, content,
   audiences and agents all depend on it. Get it agreed, tiered and owned before
   building anything on top.
3. **The CRM stays the system of record** for accounts, contacts and deals. Any
   ABM board or hub is a view and a working surface on top of it, never a second
   CRM.
4. **Facilitate, don't decree.** Stage definitions and tiers have to be the
   team's. Bring sales in first: the list review and stage mapping need sales
   sign-off or they won't be used.
5. **Rhythm before tooling.** A spreadsheet plus a weekly meeting proves the habit.
   Tooling then serves the meeting. Don't build reporting before the stages are
   locked, or automate signals before the list is in one source.
6. **Suggest, don't act.** Automation proposes stage moves, flags signals and
   drafts next steps. Owners confirm, and nobody gets contacted automatically.
7. **Unknown is not zero.** De-anonymisation, consent banners and domain matching
   all undercount. Every surface states its coverage.
8. **Decisions are recorded** with a date and a decider.

## Phases

| Phase | Outcome | Reference |
| --- | --- | --- |
| 0. Ground | Sponsor, ABM owner, sales lead and list owner named; systems inventoried; last two quarters of deals reviewed | `references/week-one.md` |
| 1. Workshop | Shared understanding; draft stages, tiers and plans; next steps with owners | `references/workshop-facilitation.md` |
| 2. Lock | Stage definitions agreed and mapped to CRM deal stages; Tier 1 vs 2 criteria written; glossary started | `references/stage-lock-and-crm-mapping.md` |
| 3. List | A reviewed, tiered list in one source, synced to the CRM, ad and visitor tools | `references/list-source-and-sync.md` |
| 4. Rhythm | The existing sales weekly renamed to the ABM weekly with marketing in it; monthly recalibration scheduled | `abm-ops` `references/operating-model.md` |
| 5. Instrument | Command center on top of the CRM, then read-only signal routines | `references/command-center-spec.md`, `references/routines-and-guardrails.md` |
| 6. Channels | Content, paid, events, partner and developer relations, and launches re-pointed at the list | `references/channel-alignment.md` |
| 7. Measure | North star and driver tree on the GTM dashboard; definitions agreed; attribution level stated | `abm-strategy` `references/measurement.md` |

Phases overlap. Phases 3 and 4 should start within two to three weeks of the
workshop, even with imperfect tooling. The week-by-week sequence and exit
criteria are in `references/rollout-plan.md`.

## How to run it

### 0. Ground the engagement
Confirm the sponsor, one ABM owner, the sales lead and who owns the list.
Inventory the systems and record coverage and permissions. Pull the last two
quarters of closed deals and ask: how many came from accounts we could have
named in advance, who was in the buying group, and where did they stall? Settle
the week-one questions in `references/week-one.md`, using the defaults where the
client has no view.

### 1. Run the workshop
Two hours, four steps: define the funnel, map accounts, prioritise, plan. Use a
live shared board so decisions persist; it becomes v0 of the command center.
Close with owners and dates for the standard next steps. Write the summary within
48 hours. Detail in `references/workshop-facilitation.md`.

### 2. Lock the design
Mark each stage agreed, map it to CRM deal stages and to any sales pipeline view,
and settle "Aware" explicitly. Write the Tier 1 vs 2 criteria and the ICP rubric
(via `icp`) in one canonical place. Start the glossary. Unlocked items become named
next steps with owners. Detail in `references/stage-lock-and-crm-mapping.md`.

### 3. Build the list and sync it
One source of truth for membership and tier, synced to a period-named CRM tier
property, CRM segments, visitor-tool lists, ad audiences and the command center.
Log every add, remove and re-tier. Detail in `references/list-source-and-sync.md`.

### 4. Stand up the rhythm
Rename the existing sales or account review to the ABM weekly and add marketing;
don't add a meeting. Every account gets an owner, a current stage, a target stage,
a date and a next step. Schedule the first monthly recalibration. Running these
from then on is `abm-ops`.

### 5. Instrument
Build or adopt a command center (`references/command-center-spec.md`) in the
sequence v0 → v4, iterating from what's asked for in the weekly meeting. Add
routines in order of value (`references/routines-and-guardrails.md`), each
specified with the routine template and designed with `agentops:routine-design`
where the client runs agents. Where it would help to automate more,
`agentic-opportunity` maps which steps to automate and which to keep human.

### 6. Align channels
Audit recent content by segment × persona × stage and fill the procurement and
security gap first; point paid at the list's buying groups; re-score events on
pipeline vs mindshare; give developer or community relations the job of finding
people at target accounts; brief target accounts before launches. Detail in
`references/channel-alignment.md`.

### 7. Instrument the measurement
Put the `abm-strategy` measurement spec on the GTM dashboard: an ABM section
(target accounts by tier and stage) and, where there's a self-serve surface, a
PQL → sales crossover. Agree the glossary definitions before building charts.
State the attribution level.

## Working with the client's people
- **Make the first win visible:** one stalled account moved through a coordinated
  play.
- **Keep marketing in the room** where account decisions are made.
- **Share the approach company-wide early.** People outside GTM often hold the
  warm intro that unlocks a stalled account.

## Acceptance checklist (the end product)

**Decisions recorded**
- [ ] ABM endorsed as the GTM operating model; account-movement KPIs adopted
- [ ] One ABM owner, and one accountable owner per Tier 1 account
- [ ] Stage definitions locked (entry, exit, job; Aware signals named), mapped to
      CRM deal stages and any sales pipeline view
- [ ] ICP rubric, overrides and Tier 1 vs 2 criteria written down
- [ ] CRM confirmed as the system of record; the list source named

**Working assets**
- [ ] A tiered target list in one source, synced to a CRM tier property, CRM
      segments, ad audiences and visitor-tool lists
- [ ] A command center with board, account pages, suggested and confirmed stages,
      owners, next steps, notes and buying group
- [ ] A weekly signals routine with coverage reporting
- [ ] Next steps mirrored to CRM tasks; reminders and tag digests for owners
- [ ] A weekly ABM meeting ending in top 1–3 actions per function; a monthly
      recalibration in the calendar
- [ ] A glossary covering target account, ABM stage, tier, PQL, core market and
      deal origin
- [ ] The GTM dashboard's ABM section live

**Channel alignment**
- [ ] A content map (segment × persona × stage) and a procurement/security asset
- [ ] List-based paid live, with target-account reach reported separately
- [ ] Events scored on pipeline vs mindshare
- [ ] A goal for finding people at target accounts (DevRel, community or partners)
- [ ] Target accounts pre-briefed before launches

**Measurement**
- [ ] North star = target-account stage movement by tier; driver tree in place;
      attribution level stated

Unticked items are listed as open with an owner, never quietly dropped.

## Self-check before handing back
- No account names, contacts, deal values, tier lists or tool names from any other
  client.
- Stage definitions have entry and exit criteria, and Aware has named signals.
- Tier 1 is capped and the criteria are written down.
- Each routine lists its reads, writes, no-contact rule and failure behaviour.
- KPIs are account-movement based, and volume metrics are labelled as context.
- Coverage limits (match rates, consent, domain mapping) are stated.

## Reference map

| File | Read when |
| --- | --- |
| `references/week-one.md` | Grounding the engagement: questions with defaults, systems needed |
| `references/workshop-facilitation.md` | Preparing and running the kickoff workshop |
| `references/stage-lock-and-crm-mapping.md` | Locking stages and mapping them to the CRM and sales views |
| `references/list-source-and-sync.md` | Making the list one source of truth and syncing it outward |
| `references/command-center-spec.md` | Building the ABM board and account pages |
| `references/routines-and-guardrails.md` | Designing signal routines and their guardrails |
| `references/channel-alignment.md` | Re-pointing content, paid, events, relations and launches |
| `references/rollout-plan.md` | The 12-week sequence with exit criteria |
| `references/templates.md` | Leadership ask, stage card, account plan, routine spec |
| `abm-strategy` references | The method: stages, tiers, buying groups, plays, measurement |
| `abm-ops` `references/operating-model.md` | Roles, cadence and the weekly agenda being installed |

## Voice
Clear, concise, plain language. Lead with what's decided, what's next and who
owns it. Client-facing copy gets a client voice pass.
