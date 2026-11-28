# Tiering & target-account selection

## The target-account list (TAL) is an ICP job
Don't invent a new scoring system here. `icp` defines and scores the ideal
*account* and produces a fit-scoring rubric; this skill consumes that to build
and rank the TAL. If the ICP is missing or stale, run `icp` first. Then apply the
account-based overlay below.

The economic shift that makes broad TALs viable: mapping the whole addressable
market into the CRM used to be too expensive in time and money; it no longer is.
So a modern TAL can be the full ICP-qualified universe, *tiered*, rather than a
hand-picked 100.

## The three tiers
Classic, stable doctrine (ITSMA lineage). Tiers differ by coverage ratio,
personalisation depth, and cost per account.

| Tier | Coverage | Accounts (typical) | Personalisation | Cost/effort |
|---|---|---|---|---|
| **1:1** | One programme per account | single strategic accounts (units–low tens) | Deep, bespoke per account | Highest |
| **1:few** | One programme per cluster | 5–50 lookalikes per cluster, grouped by vertical/problem/trigger | Reusable assets, light tailoring per cluster | Medium |
| **1:many** | One programme across many | hundreds–thousands of ICP accounts | Dynamic ads, web/email personalisation, intent-triggered outreach | Lowest per account |

Numeric bands vary by source (1:few is variously 5–50 or 5–100) — size to the
client's capacity, not to a rule.

The 1:few tier is where most programmes get their leverage: tight enough to feel
relevant, broad enough to reuse. A useful default bias for smaller teams is to
run a strong 1:few programme plus a light 1:many layer, and reserve 1:1 for a
genuine handful.

## The four selection / assignment inputs
Assign each account to a tier on a composite of:

1. **Account value** — potential ACV / strategic worth. Bigger prize justifies
   more bespoke effort (toward 1:1).
2. **Buying stage** — where the account is in its journey (cold → in-market →
   active evaluation). In-market accounts earn more intensive treatment now.
3. **Intent signals** — observable in-market behaviour (see `references/signals.md`).
   A spike can promote an account temporarily.
4. **Sales capacity** — how many accounts sales can genuinely work at each depth.
   This is the hard constraint that caps 1:1 and 1:few counts. Tier to capacity,
   not to ambition.

## Dynamic tiering (not a static list)
Tiers are not a one-time allocation. Define **promotion / demotion triggers** so
accounts move as reality changes:

- **Promote** on: intent spike, buying-group engagement crossing a threshold,
  a champion arriving, deal progression, a trigger event (funding, hire, reorg).
- **Demote** on: sustained non-engagement, disqualifying fit change, deal death,
  capacity pressure elsewhere.

Name the triggers and roughly who/what watches them, even when the client can't
yet automate it. A static TAL that never re-tiers is a common decay mode.

## Evidence-thin vs evidence-rich
- **Evidence-rich:** build the TAL from the `icp` rubric applied to real CRM /
  usage / closed-won data; tier on live intent; set real promotion thresholds.
- **Evidence-thin:** priors-led list from firmographic fit and named triggers;
  tiers assigned on judgement; promotion triggers defined but manual. Mark it as
  hypothesis and name what data would upgrade it.

## Readiness and the fit × readiness matrix
The four inputs collapse into two axes that a team can see and argue about on one
board:

- **Fit:** the `icp` fit score, plus account value.
- **Readiness:** where the account is now, its stage in `funnel-stages.md`, plus
  recent signals. A strong-fit account that's Unaware is a different job from one
  that's Evaluating.

Plot every candidate with fit on one axis and readiness on the other. Two
adjustable split lines give three tiers:

| Tier | Region | Motion | Treatment |
| --- | --- | --- | --- |
| Tier 1: 1:1 | High fit, high readiness | Bespoke | Each account gets its own plan, owner, next step and date |
| Tier 2: 1:few | High fit, lower readiness | Cluster programs | Worked through programs built for a cluster of similar accounts |
| Tier 3: 1:many | Lower fit | Always-on | Ads, content and product-led motion; promoted when signals appear |

Sales capacity still caps the counts.

## Cap Tier 1, and write the criteria down
- **Cap Tier 1** at what the team can genuinely work one-to-one. For a small team
  that's often 8–15 accounts. Past the cap, Tier 1 stops meaning anything; "too
  many Tier 1s with no ranking" is the most common tiering failure.
- Within Tier 1, keep a **"this quarter's wins"** focus: the handful the company
  expects to close this quarter.
- One starting shape for a first list: around 100 accounts, roughly 15 / 35 / 50
  across the tiers. Expand Tier 3 from the ICP score once the motion works. Size
  to the client, not to this example.
- Existing customers can be on the list as expansion targets.
- **Write down the Tier 1 vs Tier 2 criteria** the same day they're decided.
  Whiteboard tiering that nobody writes up can't be maintained.
- Don't let a 1:1 play quietly broaden into a cluster program, or the other way
  round.

## Clusters and segments
- Group Tier 2 (and Tier 1) accounts into **4–6 clusters** that share a problem
  and a buyer. Clusters drive 1:few content and programs. Keep an explicit "not
  sorted yet" cluster rather than forcing a fit.
- If the company sells into two very different markets, tag each account with a
  **segment** and filter by segment and cluster everywhere.
- A shift of focus between sub-segments after the first tiering is normal and
  healthy. Record it as a decision with a date.

Keeping the list in one source of truth and syncing it outward is `abm-setup`
(`references/list-source-and-sync.md`). The monthly re-tier and quarterly re-score
are `abm-ops`.
