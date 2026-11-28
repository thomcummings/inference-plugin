# KPI driver trees — formal spec and archetype trees

## The formal spec

A driver tree is a three-layer causal model. Each layer has a definition and a test; a
metric that fails its layer's test doesn't belong in that layer (and possibly not in the
tree).

### Layer 1 — North star (exactly one)

**Definition:** the single metric that best proxies the moment of value exchange — the
customer received the core value AND the business banked durable progress.

**Tests it must pass:**
- *Exchange test*: does it capture customer value received, not just business value
  extracted? (Revenue fails; "weekly accounts running automated AP" passes.)
- *Steering test*: does it move on a readable cadence (weekly-ish) so the team can steer
  by it? (ARR fails — too slow, too lagging.)
- *Gaming test*: can it be inflated while the business stands still? (Signups fail —
  inflatable by junk acquisition. Signups *doing the core action* pass.)
- *Breadth test*: can most teams influence it? (A metric only one team can move is a
  driver, not a north star.)

### Layer 2 — Driver metrics (3–5)

**Definition:** the controllable quantities that move the north star, connected by edges.

**Edge types — always labelled:**
- *Mathematical*: the drivers compose the north star by arithmetic (north star =
  new activations × activation rate + retained base − churn). Prefer these where they
  exist; they can't be argued with, only measured badly.
- *Causal*: believed influence (review volume → conversion rate). Every causal edge
  carries an evidence state: **evidenced here** (this client's data), **industry prior**
  (believed from pattern, not yet shown here), or **hypothesis** (asserted, needs a test).
  An unlabelled causal edge is how superstition gets institutionalised.

**Tests:** each driver must be (a) controllable — some team's actions move it within a
quarter; (b) attached — its upward edge stated and typed; (c) owned — exactly one owner;
(d) guarded — paired with the counter-metric its pursuit most plausibly breaks.

### Layer 3 — Activity metrics

**Definition:** what teams touch week to week — publishing cadence, outreach volume,
webinar registrations, listing views. Mostly *input* metrics (fully controllable) and
*leading* for the driver above.

**Tests:** each activity metric feeds exactly one named driver; anyone on the team can say
what decision changes when it moves ("registrations low at T-2 weeks → push promotion" —
that sentence earns the metric its place).

### Global rules

- **Three layers, no more.** A fourth layer is a dashboard, not a model; detail below
  activities belongs in channel tooling.
- **Every metric has an upward edge.** No edge → cut. This is the vanity-metric defence,
  applied structurally rather than metric-by-metric.
- **The tree is versioned.** Edges change state (hypothesis → evidenced) and branches get
  added/pruned at each re-plan; date it like any other living document.
- **The tree arbitrates.** "Should we measure X?" = "which driver does X feed?" — the
  answer is the tree's, not the loudest stakeholder's.

---

## Archetype trees

Start from the nearest archetype and adapt. The deviations from archetype are diagnostic
gold — where a business's tree differs from its motion's standard shape is where its model
is most distinctive (or most confused). All example numbers are illustrative.

### Archetype 1 — PLG / self-serve SaaS

**North star:** weekly accounts performing the core value action (e.g. "teams shipping
returns through the platform each week"). Passes exchange (they got value), steering
(weekly), gaming (junk signups don't perform the action), breadth (product, marketing,
lifecycle all move it).

**Drivers** (edges mostly mathematical — this motion's funnel composes):
1. **New activated accounts/mo** = signups × activation rate — *mathematical*. Guardrail:
   ICP share of signups (volume is inflatable with junk).
2. **Activation rate** (signup → core action within 14 days) — *mathematical*. Owner:
   lifecycle/onboarding. Guardrail: time-to-value not gamed by shrinking the definition.
3. **Retained active base** (logo/usage retention) — *mathematical*. Guardrail: support
   load per account.
4. **Expansion rate** (free→paid, tier upgrades) — *mathematical*. Guardrail: refund/
   downgrade rate.
5. **Referral/WOM coefficient** (invites, referred signups) — *causal, often industry
   prior until instrumented*.

**Activities feeding them:** organic/AEO traffic → D1; marketplace listing views →
D1; onboarding email engagement → D2; in-app prompt interactions → D2/D4; review volume →
D1 (*causal: industry prior*); integration adoption → D3 (*causal: usually evidenced —
integrated accounts churn less*).

**Classic mistakes this tree catches:** judging content by traffic (no edge to D1 unless
traffic converts); celebrating signups while activation rots; paid spend scaling against
a leaky D2.

### Archetype 2 — Sales-led / sales-assisted B2B

**North star:** qualified pipeline created (£/mo) — *not* closed revenue (lags a quarter+
behind the marketing that caused it; unsteerable) and *not* MQLs (gameable, no exchange).
Some practices prefer "sales-accepted opportunities/mo" — either passes the tests; the
choice is a visible judgement call.

**Drivers** (edges split mathematical/causal — this motion is trust-led, so causality
matters more and is murkier):
1. **Demo/meeting requests/mo** — *mathematical* (pipeline = requests × accept rate ×
   ACV). Guardrail: ICP share of requests.
2. **Request→opportunity conversion** — *mathematical*. Owner: sales, influenced by
   marketing qualification. Guardrail: sales-cycle length (don't fill the top with slow
   maybes).
3. **Referral/advocacy flow** (referred requests/mo) — *causal, usually evidenced in
   mature accounts, uninstrumented in young ones* — the classic gap: "half our deals" in
   founder memory, absent from the CRM.
4. **Founder/brand surface** (branded search, direct requests) — *causal, industry
   prior*. The proxy for trust-led motions; failure mode: polluted by PR spikes.
   Triangulate with "how did you hear about us".
5. **Win rate** — shared with sales; marketing's edge is proof assets and competitive
   positioning (*causal: hypothesis until win-loss work shows it*).

**Activities:** webinar registrations/attendance → D1; event conversations → D1;
outbound replies (sentiment-guarded) → D1; case studies shipped → D5 (*hypothesis until
win-loss evidence*); founder LinkedIn cadence → D4; review-site presence → D2.

**Classic mistakes:** reporting MQLs nobody accepts; measuring founder LinkedIn by
impressions (feeds nothing) instead of sourced requests at 90 days; leaving the referral
driver uninstrumented because it "just happens".

### Archetype 3 — Services / consultancy / agency

**North star:** qualified conversations with right-fit buyers per month. At services
economics (low volume, high value, lumpy demand) this is the largest number that still
passes the steering test; win rate and ACV matter but move too slowly to steer by.

**Drivers** (edges mostly causal — services demand is reputation-shaped):
1. **Referral & alumni flow** — *causal, usually evidenced*: conversations sourced to
   past clients and network. Guardrail: fit quality (referrals drift off-ICP as the
   network ages). Activities: systematic asks, staying-visible touches, alumni notes.
2. **Founder reputation surface** — *causal, industry prior*: conversations sourced to
   LinkedIn/essays/talks/guesting. Time-to-signal: quarters, not weeks — say so or the
   channel gets killed at week 6. Activities: publishing cadence (input metric), guesting
   bookings, talk submissions.
3. **Authority content engine** — *causal, hypothesis→evidenced over time*: conversations
   citing the newsletter/POV work. Guardrail: production time per piece vs delivery
   capacity (the guardrail *is* the business model).
4. **Partnership flow** — *causal*: conversations from adjacent practices. Activities:
   active partner relationships, co-marketing moments.

**Guardrail on the whole tree:** utilisation. Marketing that succeeds while delivery is
full creates conversations that go stale — services trees need a capacity valve
(waitlist, pricing) rather than a bigger top of funnel.

**Classic mistakes:** measuring the newsletter by subscribers (feeds nothing unless
subscribers become conversations); chasing SEO volume in a trust-shaped market; founder
reputation work judged on a paid-search clock.

---

## Using the archetypes

- In FRAMEWORK mode: start from the nearest archetype, adapt, and *write down the
  deviations* — "unlike the standard sales-led tree, this client's D3 referral edge is
  evidenced and dominant, so it gets the biggest driver share" is exactly the sentence a
  client pays for.
- In ADVISOR mode with no client tree: scaffold the answer on the nearest archetype,
  label it provisional, and offer FRAMEWORK mode.
- Hybrid motions (PLG with sales assist): take the dominant motion's tree and graft the
  1–2 drivers the secondary motion demands; don't run two full trees against one north
  star.
