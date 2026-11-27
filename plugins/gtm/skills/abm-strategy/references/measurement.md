# Account-level measurement

This is also a standalone mode: a client often needs the measurement spec on its
own. The output is a **tool-agnostic spec** — what to track, why, and the target
— with an optional "how to instrument it in [their stack]" layer when evidence-rich.

## Why not MQLs
The lead/MQL funnel is the wrong instrument for an account-based motion. Its
well-documented flaws: attribution is opaque; it drives marketing-sales blame
over "who gets credit" instead of "what moved the account"; stages are arbitrary
and disconnected from real buyer intent; the lead bucket leaks and wastes spend;
and it incentivises spray-and-pray volume over account progression. Account-based
work needs account-level measures.

## The three-question spine
Anchor the whole measurement model on three questions (the "GTM metrics 2.0"
frame):

1. **How many accounts are in the ICP?** (the addressable, qualified universe)
2. **Where are they in their buying journey?** (stage distribution across the TAL)
3. **Which activities most effectively move them along it?** (what actually
   progresses accounts — the thing to invest more in)

Everything below serves one of these three.

## Core account-level metrics
Pick the subset the client can support; name the rest as targets to instrument.

- **ICP coverage / TAL size** — how much of the qualified universe is in the
  programme, by tier.
- **Account penetration** — depth of engagement within each account (how much of
  the account/buying group is engaged), not just whether it was touched.
- **Buying-group coverage** — the required-roles-engaged score from
  `references/buying-groups.md`. The account-based answer to "are we reaching the
  committee?"
- **Account engagement** — a composite of meaningful interactions at the account
  level (weighted by role and recency), trended over time. The leading indicator.
- **Stage progression / velocity** — accounts moving between journey stages, and
  how fast. Movement is the point.
- **Pipeline coverage** — pipeline generated from target accounts vs the target;
  and the share of pipeline/revenue coming from the TAL vs off-list.
- **Win rate & deal size on target accounts** — vs non-target, to prove the
  motion is earning its cost.
- **Tier movement** — accounts promoting/demoting (from `references/tiering...`);
  a healthy programme shows flow, not a frozen list.

## What to avoid
Lead counts, MQL volume, and cost-per-lead as headline metrics; last-touch
attribution fights; vanity reach ("we touched 4,000 accounts") divorced from
penetration or progression.

## Evidence-thin vs evidence-rich
- **Evidence-rich:** define the metrics *and* the instrumentation — where each
  lives in the CRM/MAP/analytics stack, how the account-level roll-ups compute,
  and reporting cadence. Hand deep CRM plumbing (field design, score decay,
  routing) to RevOps.
- **Evidence-thin / no stack access:** deliver the spec — the metric set, the
  definitions, the targets, and the "what you'd need to see this" list — so the
  client (or a future engagement) can instrument it. A good spec is a real
  deliverable even with zero access to their data.

## North star and driver tree
**North star: target-account progress.** Tier 1 and 2 accounts moving at least one
stage in the period, by tier. A quarterly goal per tier makes it concrete, for
example "N Tier 2 accounts from Unaware to Aware this quarter".

The driver tree shows marketing's contribution underneath it:

| Level | Measure | Marketing levers |
| --- | --- | --- |
| Outcome | Target accounts progressing a stage this period, by tier | All of the below |
| Engage | People from target accounts visiting, attending, engaging with ads | ABM ads, events, outbound support content |
| Acquire | Core-market visitors by channel | Search and answer engines, paid, social, community, events |
| Convert | Visitor → sign-up or hand-raise, by landing page | Website conversion, landing pages, CTAs |
| Activate | Sign-up → meaningful usage; PQLs and PQAs (where there's a self-serve surface) | Onboarding, nurture, docs |
| Hand over | PQLs or PQAs with a deal; time from qualification to deal | Routing, sales follow-up |

## Definitions to agree (they go in a glossary)
- **Target account:** a company with a current-period tier in the CRM, matched to
  product accounts by domain.
- **ABM stage:** the confirmed account stage from `funnel-stages.md`.
- **Core market:** the countries or segments that count. Exclude legacy or
  irrelevant traffic from headline numbers.
- **Week:** one agreed time zone, complete weeks only.
- **Conversion:** cohort-based (share of a period's visitors reaching the next
  step within N days), not same-period ratios.
- **PQL (draft until sales signs off):** a company-domain account, not free email
  and not already enterprise, reaching a usage threshold within a window.
- **Deal origin:** the CRM's origin field. Show bulk imports separately, so list
  loads don't read as demand.
- **Discovery source:** self-reported at sign-up. Directional, not attribution.
- **Paid:** first touch tagged with paid mediums. Fix UTM conventions first; paid
  social is often mis-tagged as organic.

## Attribution levels (state which one you're at)
1. Deal origin plus self-reported discovery.
2. Tracked touchpoints and UTMs through to deals.
3. Multi-touch models or incrementality tests.

Most clients start at level 1. Write down what's needed to reach level 2 (usually
a tracking build).

## Two scorecards, never blended

| | Pipeline | Mindshare and self-serve |
| --- | --- | --- |
| Headline | Target-account stage movement, including within 30/60 days of a touch | Sign-ups or activations attributable to the channel |
| Supporting | Tier 1/2 accounts touched; meaningful conversations; buying-group coverage | Repeat engagement; inbound requests; content reach |

Volume metrics (traffic, sign-ups, leads) stay on as context, labelled as such.

## Health thresholds to hand to `abm-ops`
Name the thresholds that trigger action on a live programme: accounts stuck in a
stage more than N weeks, Tier 1 over its cap, Tier 1 accounts with no dated next
step, buying-group coverage below target at a stage, and tier flow (no promotions
or demotions in a month means the list has frozen).

## Common traps
- Two dashboards with different filters showing "conflicting" numbers. Fix the
  definitions, not the charts.
- Celebrating content by traffic when the top-traffic pieces moved no accounts.
- Treating unavailable data (no tracker, failed sync) as zero.
- A headline "deals" or "leads" metric dominated by self-serve volume.
