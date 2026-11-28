# Measurement frameworks — the baked-in apparatus

## North star selection

The north star is the single metric that best proxies the moment of value exchange — the
customer got the thing AND the business banked progress. Criteria: it leads revenue (not
revenue itself), it's influenceable by most teams, it resists gaming, it moves on a readable
cadence (weekly-ish). Classic shapes: usage-of-core-value (messages sent, reports run,
nights booked), value-delivered (orders fulfilled, candidates placed), engaged-capacity
(weekly active accounts doing the core action). Revenue and ARR are board metrics, not north
stars — they lag too far to steer by. Propose 2–3 candidates with trade-offs; choosing is a
visible judgement call.

## Driver trees (KPI trees)

The full formal spec (layer definitions, edge types, the tests each layer must pass) and
three worked archetype trees (PLG SaaS, sales-led B2B, services/consultancy) live in
`driver-trees.md` — that file is the canonical reference for building or auditing a tree.
The one-line version: north star at the root, 3–5 owned driver metrics with typed edges
(mathematical or causal-with-evidence-state), activity metrics beneath, three layers max,
everything without an upward edge cut.

## Leading vs lagging

Lagging metrics judge (revenue, churn, closed deals); leading metrics steer (demo requests,
activation rate, pipeline created, content output against plan). Every layer of a tree is
leading for the layer above and lagging for the layer below — the labels are relational, not
absolute. Failure modes: steering by lagging metrics (decisions arrive too late), or judging
by leading metrics (teams hit proxies while the outcome rots). A workstream needs one of
each at minimum.

## Input vs output metrics

Outputs are what you want (signups); inputs are what you control (publishing cadence,
outreach volume, response time). Teams commit to inputs and are judged on outputs over a
longer window. When a team misses an output target, the first question is whether the inputs
happened — if they did, the model is wrong; if they didn't, the execution is. These are
different problems with different fixes, and conflating them is the most common
plan-review error.

## Guardrail / counter-metrics

Every target teaches gaming. Pair each driver with the thing it most plausibly breaks:
acquisition volume ↔ activation or refund rate; content velocity ↔ organic CTR or quality
score; discount-led conversion ↔ ACV and margin; outbound volume ↔ reply sentiment /
unsubscribes / domain health. If you can't name what a metric's pursuit might break, you
haven't thought about it long enough to set a target on it.

## Vanity smell tests

A metric is vanity (for this decision) if: it can rise while the business stands still
(impressions, followers, raw traffic); nobody can say what they'd do differently if it
halved; it isn't connected by any edge to the tree; or it's reported because the platform
makes it prominent. The test isn't the metric, it's the decision: follower count is vanity
for a SaaS pipeline conversation and a real input for a creator business. Always offer the
nearest decision-bearing alternative rather than only striking things out.

## Stage-appropriate measurement

- **Pre-revenue / pre-launch:** measure learning, not performance — qualified conversations,
  waitlist→interview rate, retention of early users. One north star candidate, 3–4 inputs,
  a weekly 30-minute habit. No dashboards.
- **Early revenue:** the funnel exists; instrument it end to end before optimising anything.
  Attribution basics (UTM discipline, source fields populated) outrank any new metric.
- **Scaling:** full tree, owners, cadences, guardrails; experiments get their own
  pre-registered metrics; the board pack and the operating tree are explicitly different
  documents.
- **Post-incident / post-churn-shock:** resist the urge to instrument everything at once;
  find the 2–3 metrics that would have caught it early and add only those.

## Attribution honesty tiers

Tier the confidence and say the tier out loud: (1) **tracked** — UTM/CRM source field,
trustworthy if hygiene is real; (2) **correlated** — timing joins (spike followed the
campaign), honest as "consistent with", never "caused by"; (3) **claimed** — self-reported
"how did you hear about us" (add it everywhere; it's cheap and catches dark social); (4)
**believed** — founder memory and anecdote, which is evidence of *something* but bands as
unmeasured. Most B2B maps are mostly tiers 2–4; frameworks that pretend otherwise get
ignored within a quarter. The "blank/direct" bucket is a measurement debt marker, not a
channel.

## Time-to-signal

Before committing to a judging metric, state when it becomes readable: paid search reads in
weeks; SEO and AEO in months; brand and community in quarters. Mismatched patience kills
slow-compounding channels (judged too early) and protects bad fast channels (pivoted before
the verdict). Where the judging metric is slow, the leading indicators carry the interim —
and the checkpoint calendar should show both clocks. Sample-size sanity: at low volumes,
percentages lie; below ~30 events per cell, report counts and wait, don't compute rates.
