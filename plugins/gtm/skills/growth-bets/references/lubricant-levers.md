# Lubricant levers

The menu the **lubricant bet** role draws from. Lubricants do not create growth on their
own; they make the engine run more efficiently, so a small lubricant gain multiplies
across every cohort the engine brings in. This library catalogues the high-leverage
levers inside the three lubricant areas (activation, retention, monetization), the test
for whether each is actually your bottleneck, and the benchmarks that say what good
looks like.

It is a catalogue, lightly framed. The opinionated calls (which lubricant to fix first
for this company) sit in the skill. The job here is accurate levers and honest
bottleneck tests, so growth-bets does not optimise a lubricant that is not the
constraint.

## Two organising ideas

- **Order of leverage (Sean Ellis).** For most products the impact order is
  activation, then retention, then revenue, then referral, then acquisition. Retention
  drives growth; acquisition spend cannot save a product users do not come back to.
  Diagnose in that order unless the data says otherwise.
- **Motions x levers (Elena Verna).** Every company eventually plays all three levers
  (acquisition, monetization, retention) across all three motions (product-led,
  marketing-led, sales-led). The question is not *if* but *when*. Use this to spot the
  empty square a competitor could exploit.

Before picking any lever, run its **bottleneck test**. Optimising a lubricant that is
not the constraint is motion without progress.

## Activation - getting users to first value

The single highest-leverage area for most early products: you are keeping users who
already showed up, not buying new ones.

**Levers**
- **Find the real aha moment.** Not the founder's 2018-deck guess. Cohort users by
  signup week, segment by whether they took a candidate action in week 1, plot day-7,
  14 and 30 retention for each. The action whose retention curves spread widest, and
  that at least ~30% of users reach, is your aha moment.
- **Shorten time-to-value.** Median time from signup to aha is the most predictive
  activation metric. Under ~10 minutes is great, under an hour is workable, over 24
  hours and most users never return.
- **Triage onboarding friction.** Sort every step into essential (needed for the
  product to work), deferrable (real but can wait until after value, e.g. billing,
  profile, team setup), and removable. Move deferrable steps after the aha moment,
  delete removable ones. Keep friction that filters genuinely bad-fit users.
- **Instrument the path to aha** as a short sequence of steps (sign up, setup, first
  core action, the aha action, habit) so you can see where users stall.

**Bottleneck test:** are signups failing to reach first value? Look at activation rate
and median time-to-value. If they are healthy and users still leave, the constraint is
retention, not activation.

**Benchmarks (Lenny Rachitsky and Yuriy Timen, "What is a good activation rate",
Lenny's Newsletter, Oct 2022, survey of 500+ products):** SaaS activation median ~30%;
good is the 60th percentile, great the 80th. B2B enterprise SaaS median ~33%, good
~40%, great ~65%. Survey data from 2022, so treat as a rough guide.

## Retention - keeping and re-engaging users

Retention is where the engine's efficiency is won or lost, and where compounding lives.

**Levers**
- **Flatten the retention curve.** A healthy product's retention curve flattens into a
  stable plateau (the "smile" when resurrection lifts it later). A curve that decays to
  zero is a product or fit problem, not a lifecycle-email problem; route it to
  `growth-model`.
- **Feature adoption, two ways (Verna).** Top-down: list the 5-10 features you believe
  deliver core value; if adoption is low, you have a discovery or feature-bloat
  problem. Bottom-up: find the features your most-retained users rely on and drive
  adoption of those among comparable users.
- **Build a habit / trigger.** Tie the core action to a recurring internal or external
  trigger so return visits do not depend on memory.
- **Resurrect churned users (Verna).** Often cheaper than new acquisition. Segment the
  churned base: still-active free users are candidates for a trial restart on your next
  big launch (let the product talk); truly inactive users get a careful, spaced drip
  showing what changed since they left. Churned users carry an outdated picture of the
  product, that gap is the opportunity.

**Bottleneck test:** does the retention curve plateau or decay to zero? Is the drop at
activation (never retained) or later (retained then lost)? Early drop is an activation
problem; late drop is an engagement or value problem.

## Monetization - capturing value efficiently

The most avoided lubricant, and one of the most powerful. Treat it as a living system,
not a spreadsheet revisited every three years. Companies that refine pricing regularly
grow materially faster.

**Levers**
- **Value metric.** What customers pay for as they grow. The best ones map to a budget
  line buyers already track (seats to headcount, volume to transaction cost) and scale
  with the value received. Getting this wrong is the costly mistake; change it last
  because it is hardest.
- **Packaging and tiers.** Two to four tiers, gated so needs outgrow the plan as the
  customer grows. Watch plan distribution: everyone on the lowest tier means upgrade
  triggers or higher tiers are mispriced; everyone on the highest means money left on
  the table.
- **Expansion / net revenue retention.** Upgrades that happen without a sales call are
  packaging working. Near-zero expansion MRR means the upgrade path is broken.
- **Paywall timing and awareness.** When and how the model is presented in-product.
- **Freemium as investment, not charity (Verna).** Evaluate free tiers as an engine for
  acquisition, activation and conversion, not a subsidy.
- **Sequence the work (Verna).** Start with monetization *awareness* (how the model is
  presented: paywalls, messaging), then *conversion friction* (pricing-page clarity,
  checkout), and experiment with the *value metric* last.

**Bottleneck test:** is revenue per customer flat while usage grows (value-metric or
expansion problem), or are trials not converting (awareness or friction problem)? Fix
awareness and friction before touching the value metric.

**Benchmarks (Lenny Rachitsky, "What is a good payback period?", Lenny's Newsletter,
Dec 2021, consensus of 16 growth advisers):** payback period for SMB B2B, under 6 months great, 12 good, 18
ok; for enterprise, under 12 great, 18 good, 24 ok. Healthy product-led businesses see
a meaningful share of growth from expansion, not just new logos.

## Using levers inside growth-bets

1. Diagnose which lubricant is the **actual constraint** (activation rate, retention
   curve shape, expansion rate), in Sean Ellis order.
2. Pick **one lever** in that area and make it a bet with a named assumption and a
   leading metric, not a vague "improve onboarding".
3. Set the **decision threshold** against the benchmark, not against hope.
4. Hand experiment design to `references/experiment-patterns.md`; hand a retention curve
   that decays to zero back to `growth-model` (it is a fit problem, not a lubricant).

## Method lineage

- Sean Ellis: aha moment, time-to-value, must-have / PMF survey, order of leverage,
  ICE, high-tempo testing.
- Elena Verna: motions-x-levers growth matrix, retention levers (feature adoption,
  resurrection), monetization as a living system.
- Reforge / Casey Winters: retention curves, engagement loops.
- Lenny Rachitsky: activation, retention and payback benchmarks.
- Stripe / OpenView: SaaS pricing-and-packaging mechanics (value metric, tiers,
  expansion).
