# Plays & systems

## The play is the unit of ABM work
A **play** is a coordinated, multi-channel sequence aimed at an account (or
cluster) and its buying group, at a specific funnel stage, in response to a
trigger. It is not a campaign blast and not a single email — it's marketing and
sales acting together against one account context.

Every play should name:

- **Trigger** — what fires it (a signal, a stage change, a buying-group gap, a
  trigger event). "It's Tuesday" is not a trigger.
- **Tier & stage** — which tier and funnel stage it serves.
- **Message hypothesis** — the shared pain/insight the play is built on. For
  1:few, one hypothesis across the cluster with 1–3 specific data points beats
  bespoke-per-account effort; tight relevance usually outperforms heavy
  personalisation when the signal is right.
- **Channels** — pull the route mix from `channel-map`; don't re-derive it.
- **Sales + marketing actions** — what each side does, in sequence.
- **Joint owner** — the single person accountable for the account/cluster.
- **Exit** — what "worked / didn't" looks like, so it can be ranked (`growth-bets`).

## Plays per tier × stage (the classic backbone)
Build a grid: tiers (1:1 / 1:few / 1:many) down one axis, account stages
(Unaware → Aware → Engaged → Evaluating → Buying → Customer, from
`funnel-stages.md`) across the other. For each
live cell, define the play. This is the durable, teachable core — it works for a
client with a spreadsheet and an inbox.

Depth scales with tier: 1:1 plays are bespoke per account; 1:few reuse assets
across the cluster; 1:many are programmatic (dynamic ads, web/email
personalisation, intent-triggered sequences).

## The systems / agentic overlay — MATURITY-GATED
The leading edge is moving from discrete calendar-scheduled plays to **systems**:
timing becomes dynamic, triggered by a **signal cluster** (several signals
stacking on one account in a short window) rather than a schedule, and parts of
the sequence run via automation or AI agents — building the micro-list,
enriching it, drafting copy, staging for review or auto-sending against a
confidence threshold.

This is powerful but **only usable above a maturity floor**. Gate it. Before
recommending the systems layer, check:

- **Data floor:** is account/contact data in a CRM, clean enough to trigger on?
- **Signal access:** are there real signals to cluster (intent, product usage,
  web de-anon)? See `references/signals.md`.
- **Capacity & governance:** can someone configure ICP/signal sources, set
  thresholds, and review output? Who owns a bad auto-send?

If the client clears the floor, design the systems layer as an *advanced upgrade*
to the classic plays, and hook `agentic-opportunity` to map exactly which steps
should be automated vs kept human, honest about cost, drift and maintenance. If
they don't clear it, keep them on the classic backbone and name the systems layer
as where they go next — don't sell orchestration to a team without the plumbing.

## Honest limits
Even at maturity, a human configures the ICP and signal sources and typically
reviews before send; "fully autonomous ABM" is aspirational, not the default.
Over-automation produces generic-personalised noise. The through-line: relevance
and buying-group coverage win, not personalisation theatre or send volume.

## The account plan (Tier 1, one per account)

| Field | What goes in it |
| --- | --- |
| Current stage → target stage | For example Aware → Evaluating |
| By | Target date, usually the quarter end |
| Aim | One sentence: what winning this quarter means |
| Trigger | Why now for them: launch, scale-up, pain, funding, hiring |
| Message | The one thing we want their buying group to believe |
| Owner | One accountable person, plus supporting owners |
| Buying group | Roles covered or missing (`buying-groups.md`) |
| Sales steps | Dated next steps owned by sales or solutions engineering |
| Marketing steps | Dated next steps owned by marketing |
| Programs | The 1:few programs this account is also in |
| Notes | Running log |

Coverage = number of dated steps + number of programs. An account with zero
coverage is a warning.

## Starter play library by stage
S = sales-led, M = marketing-led. Stages from `funnel-stages.md`.

| Stage | Plays |
| --- | --- |
| Unaware | M: list-based ads to the buying-group roles · S: warm intro through an investor or shared contact · M: a short teardown of the problem as it shows up in their public product · S: founder note to their senior leader |
| Aware | M: retarget visitors from the account with proof content · S: personal outreach naming their use case · M: invite to an owned event or roundtable · M: case study from a company like them |
| Engaged | S: offer a 30-minute expert review · M: a demo in their own context · S: reach a second person in the buying group · M: extended trial or pilot |
| Evaluating | M: proof on their data (pilot, benchmark, POC) · S: shared channel for the evaluation · S: reference call with a current customer · M: the business case |
| Buying | S: executive sponsor call · M: security and compliance pack · S: mutual close plan · S: pricing workshop |
| Customer | M: joint case study · S: expand into a second use case · M: co-marketing launch · S: quarterly business review |

High-leverage 1:1 plays:
- A curated dinner around a conference, built around one account's buying group.
- An expert audit of the account's live product or process, shared with them.
- A bespoke deck, benchmark or video for one strategic account.
- A strong warm intro. Often the single biggest unlock for a stalled account; ask
  the whole company and the investors.

## 1:few and 1:many program patterns
A program serves several accounts at once. Lay programs on a grid of stages
(columns) × tiers (rows), each tagged with a cluster.

| Program pattern | Stage | Tier |
| --- | --- | --- |
| Cluster proof: publish the problem gap in that cluster's real conditions and send it to the cluster's technical leads | Aware | 1:few |
| Teardown content for an emerging cluster, as a conversation starter | Unaware | 1:few |
| Assess each target's public product or material and give sales a one-page result to open with (public material only) | Unaware | 1:few |
| Invite-only roundtable for one cluster's leads | Engaged | 1:few |
| Owned-event invite list built only from target accounts, each attendee with a named follow-up owner | Aware | 1:few |
| Case studies cut by cluster for reps to send personally | Engaged | 1:few |
| Evaluation fast lane: proof on their data within a week | Evaluating | 1:few |
| Quarterly customer expansion review | Customer | 1:few |
| Security and deployment pack for procurement | Buying | 1:many |
| List-based ads to the buying-group roles | Unaware | 1:many |
| Integration pages and co-marketing with the platforms targets build on | Unaware | 1:many |
| Alert when a listed domain signs up for the product | Aware | 1:many |
| High-intent page visit from a listed domain routed to the owner | Aware | 1:many |
| Launches: target accounts hear first, with a personal note | Aware | 1:many |
| Founders posting on each cluster's problem | Unaware | 1:many |

## Rules
- Every play and program has an owner and a date. Undated ideas live in an ideas
  list, not in the plan.
- Content made for one account usually generalises to its cluster (1:1 → 1:few
  reuse). Don't broaden the 1:1 execution itself.
- Proposals derived from signals ("they read the pricing page") go to the owner
  as suggestions, after the owner has checked the latest thread, commitments and
  sequences. Nobody is contacted automatically.
