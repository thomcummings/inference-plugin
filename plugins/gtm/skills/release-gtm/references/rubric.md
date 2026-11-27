# Rubric — score → tier

> v1 draft, to calibrate against real releases. Score each dimension 0–3 against the
> anchors, multiply by weight, sum. Then apply the caps, then the roadmap ranking pass.
> The absolute score **proposes** a tier; the roadmap pass **disposes**.

The rubric exists to take the tier decision *off* the person shipping the release. Show
the scoring so it's legible and arguable — but the number picks the tier, not the
enthusiasm in the room.

## Scoring dimensions

| Dimension | 0 | 1 | 2 | 3 | ×wt |
|---|---|---|---|---|---|
| **Strategic / narrative weight** — does it advance the positioning / POV we're trying to own? | Off-narrative or contradicts it | Neutral, no story role | Supports an existing storyline | Central proof point for the story | ×3 |
| **Commercial impact** — revenue, pipeline, or market created | None | Indirect / soft support | Aids retention/expansion, *or* opens a proven-adjacent segment | Drives net-new revenue, *or* credibly opens a new market | ×3 |
| **Newness / innovation** | Fix or maintenance | Parity / catch-up | Meaningful advance | New-to-world | ×2 |
| **Audience reach** | Internal / tiny segment | One narrow segment | Existing base broadly | Whole market + prospects | ×2 |
| **Competitive pressure** — does announcing change the game? | Irrelevant | Minor talking point | Neutralises a competitor claim | Unlocks / unblocks deals | ×1 |
| **Customer pull** — how loudly was it asked for? | Nobody asked | Occasional ask | Frequently requested | Most-requested / waited-for | ×1 |

Max raw = 3 × (3 + 3 + 2 + 2 + 1 + 1) = **36**.

**Grade the inputs, not just the output.** For each dimension, note whether the score
rests on evidence (usage data, pipeline, a real request count) or on assumption. A
release scored high on "customer pull" from a gut feeling is weaker than the same score
from a tagged feature-request backlog. Thin evidence caps confidence in the tier; say so.

**Market-creation is a real commercial path — and it's evidence-graded, not free.** A
release whose commercial role is to *open or expand a market* (demand-gen, category
creation, a new segment) scores on **the evidence that the new market is real and
reachable**, not on revenue booked at launch. Grade it honestly, or the dimension just
rewards optimism:

- **1** — the new market is a founder thesis with no external signal yet (a trend bet).
- **2** — a proven-adjacent segment, or early real pull (waitlist that converts, inbound
  from the new segment, a comparable competitor's traction).
- **3** — demonstrated pull from the new market (paying pilots, qualified pipeline, a
  validated wedge).

This stops a market-expansion release being structurally under-scored (it *is* commercial)
while stopping a pure hope being over-scored (thin evidence stays a 1). If the release's
whole point is to *find out* whether the market exists, that's legitimate — but say so,
score the commercial line a 1, and make the launch's **objective** validated learning
(see the SKILL's objective step), not revenue.

## Score → proposed tier

| Score | Proposed tier |
|---|---|
| 28–36 | T1 |
| 18–27 | T2 |
| 9–17 | T3 |
| 0–8 | T4 |

## Caps and gates (applied after scoring, before ranking)

These are the teeth. A release can score its way to a tier and still be capped below it.

- **Proof-readiness cap.** Not demonstrable with a credible proof point at launch →
  **cap at T2**. Unfinished / risky / likely to slip → **cap at T3**. Plan for the best
  case, back up for the roadblock; beta is the listening stage that de-risks this.
- **Off-narrative cap.** Strategic weight = 0 → **cannot be T1** regardless of score.
  Flag it as a possible distraction — a commercially loud release that pulls against the
  story blurs the brand.
- **Parity floor.** Newness ≤ 1 **and** customer pull ≤ 1 → **cannot exceed T3**, however
  high it scores on reach. This stops a "technically high-reach" parity fix buying a
  moment it doesn't deserve.

Record which cap fired (if any) in the output, so the tier call is auditable.

## Roadmap ranking pass (relative — the anti-inflation engine)

Absolute scores will over-produce T1s; attention and cadence are finite. After scoring
the release, score (or at least place) the other releases queued this period and rank
them against each other.

- **Cadence guardrail (default, tunable): ≤1 T1 per period, 2–3 T2s.** If several clear
  the T1 threshold, rank them and either bump the losers down a tier or **bundle** them
  under one theme so they compound instead of competing.
- This is where ownership returns to the user. The skill presents the ranking and the
  forced trade-off; **the user makes the call** on what gets the moment. Don't quietly
  resolve it — make the finite-attention choice unavoidable and visible.

"Period" is whatever the team's cadence unit is — a sprint, a month, a quarter. Match it
to how often they actually launch, not the calendar.

## Worked example (illustrative, not a template to copy)

A "SSO for enterprise" feature:

- Strategic weight 2 (supports the "enterprise-ready" storyline) ×3 = 6
- Commercial 3 (unblocks named enterprise deals) ×3 = 9
- Newness 1 (parity — competitors have it) ×2 = 2
- Reach 1 (narrow: enterprise buyers only) ×2 = 2
- Competitive 3 (unblocks deals) ×1 = 3
- Pull 3 (most-requested by the sales team's pipeline) ×1 = 3
- **Raw = 25 → proposes T2.**

Parity floor check: newness 1, but pull is 3 → floor does **not** apply (needs both ≤1).
Proof-readiness: shippable and demonstrable → no cap. Lands a **T2**. Note the story role
is only "supporting", so it's a strong expansion launch, not a category moment — even
though commercially it's the quarter's most valuable ship. That gap between *commercial
weight* and *tier* is exactly the conversation the rubric is designed to force.
