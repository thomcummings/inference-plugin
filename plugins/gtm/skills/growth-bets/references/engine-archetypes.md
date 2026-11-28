# Engine archetypes

The menu the **engine bet** role draws from. An engine is a growth loop: a closed
system where the output of one cohort is reinvested to produce the next, so growth
compounds rather than running linearly like a funnel. This library catalogues the
known loop types, the two fits that decide whether a loop can work for a given product,
and how to turn "we should grow through X" into a bet with a proof step.

It is a catalogue, not a set of opinions. The sharp calls (which engine fits this
company, what to bet first) belong in the skill and in `growth-model`. The job here is
to make sure the right archetype gets reached for and is described accurately.

## How to use it inside growth-bets

1. Name the **candidate loop** the engine bet is meant to prove or strengthen. If
   `growth-model` has set the engine, use that. If not, pick the most plausible
   archetype below and label it provisional.
2. Check both **fits** (product-channel, channel-model) before betting. A loop that
   fails a fit is not a bet, it is a wish.
3. State the loop's **preconditions** and the **cheapest proof** that one cycle can
   feed the next.
4. Instrument **loop health**: how many new inputs does one cohort's output generate,
   and is that ratio holding or decaying.

Two standing truths from the source material that shape every engine bet:

- **One or two loops, not ten.** The fastest-growing products run on one major loop
  early, layering a second only at scale. A wall of loops usually means many weak ones.
  Force the rank.
- **Every loop decays.** Acquisition loops broaden from the most qualified audience to
  the least over time, lifting CAC and lengthening payback. Build the decay watch in,
  do not be surprised by it.

## The four engine families (Racecar)

Most breakout growth comes from one of four engines, occasionally two layered:

- **Performance marketing** - paid acquisition (search, social, video) where revenue
  funds more ads.
- **Virality** - users bring users (word of mouth, invites, exposure).
- **Content** - content created by users or the company attracts more users (SEO,
  shareable media, newsletters).
- **Sales** - reps source and close, inbound or outbound.

Two further families exist but are rarer: **partnerships / integrations** and
**physical space** (retail, shelf). Note them, do not centre a bet on them without
specific reason. Lineage: Reforge / First Round, the Racecar framework.

## The loop taxonomy (what to bet on)

### Viral loops - users lead to more users
- **Word of mouth** - users rave and tell others directly. Driven by a remarkable
  product or strong emotion. Hard to instrument, real when it shows in survey and
  organic-share data.
- **Organic / inherent** - using the product naturally exposes or invites others
  (Slack, LinkedIn, WhatsApp, Airtable). The invite is part of the core action.
- **Casual contact** - usage exposes the brand indirectly to many non-users (Drift
  chatbot badge, a Lime scooter on the street, an email-signature "sent from").
- **Incentivized** - a give-get reward drives invites. Incentive is money (Uber
  credit), content (game items), or features (Robinhood free trades / early access).
- Precondition / constraint: the maths is **branching factor x response rate** within
  a user's network. Only a share of any network is a target, so a loop with a low
  branch or low response rate will not sustain. Fits low-ARPU, low-friction models.

### Content loops - usage creates content that attracts usage
- **UGC, user-distributed (UGC-UD)** - users create content through usage and share it
  on their own channels; non-users see it and join (Patreon creators promoting their
  page).
- **Company content, user-distributed (CGC-UD)** - the company makes content, users
  spread it (Gainsight-style insight reports shared into other companies).
- **Company content, company-distributed (CGC-CD)** - the company makes content and
  distributes it itself, usually via SEO; new revenue funds more content (WebMD, the
  HubSpot blog). The classic content-SEO engine.
- Precondition: a real reason content gets created at volume and a channel that indexes
  or surfaces it. UGC loops need motivation to contribute; CGC-CD needs durable search
  demand.

### Paid loops - revenue funds acquisition
- **Ad loop** - revenue from new customers is reinvested in ads (Headspace, Casper,
  Warby Parker). Scales only while payback stays short.
- **Integration loop** - capital funds integrations that partners and the platform then
  distribute (Zapier). Slower, more defensible.
- **Inbound sales loop** - a second loop (often content) generates leads that reps
  convert (HubSpot).
- **Outbound sales loop** - reps source their own leads and close (Salesforce,
  Palantir). Common for higher-ACV B2B.
- Precondition: unit economics that let revenue refill the loop faster than CAC rises.
  Maximum scope is capped by audience size and competitor imitation; the exception is
  categories with a high fresh supply of in-market buyers (autos, real estate).

## The two fits that gate any engine bet

A loop only works if the product and the model fit it. Bet against these, not just for
the loop's appeal.

- **Product-channel fit (Balfour).** Products are built to fit channels; channels do
  not mould to products, because you do not control the channel's rules. A UGC-SEO loop
  needs a product that throws off indexable pages; a paid loop needs quick time-to-value
  and a broad value prop; viral needs the invite inside the core action. If the product
  shape fights the channel, the loop fails no matter how good the product is.
- **Channel-model fit (Balfour).** Viable channels are set by your ARPU. Low ARPU forces
  low-CAC channels (virality, content, self-serve); high ARPU affords high-CAC channels
  (sales). The **danger zone** is the middle: ARPU too high for friction-free low-CAC
  channels, too low to fund sales. A bet that crosses this zone needs a model change,
  not just more effort.

When one fit changes, the others must change too. Pinterest survived Facebook killing
its channel only by re-moulding the product to UGC-SEO. Treat a fit break as a
strategic event, not a tactical one.

## Instrumenting loop health

For the engine bet's proof plan, measure the loop, not just the top of it:

- **Cycle ratio** - new inputs generated per cohort's output (k-factor for viral,
  leads-per-content-unit for content, payback-funded spend for paid).
- **Cycle time** - how long one turn of the loop takes; shorter compounds faster.
- **Decay** - is CAC rising or response rate falling as the audience broadens.

A loop is working when one cohort reliably produces a meaningful slice of the next at
holding or improving efficiency. That is the signal that promotes a cold-start play or
a learning bet into the company's real engine.

## Picking and sequencing

- Default to **one primary loop** now, with at most one secondary in view.
- Loops **transition** over time (a launch-fed start giving way to a content or viral
  engine). Name the expected transition rather than assuming today's loop is permanent.
- **Layering** a second engine is a scale-stage move, not an early one. Flag it as
  later unless the data already supports it.
- Hand route-to-market detail for a chosen loop to `channel-map`; hand the "is this even
  the right engine" question to `growth-model`.

## Method lineage

- Reforge (Brian Balfour, Casey Winters, Kevin Kwok, Andrew Chen): growth loops vs
  funnels, the loop taxonomy (viral / content / paid sub-types), macro vs micro loops.
- Brian Balfour: the Four Fits, product-channel fit, channel-model fit (ARPU-CAC
  spectrum).
- Reforge / First Round: the Racecar framework and the four growth engines.
- Andrew Chen: channel decay and the law of shitty clickthroughs (loops broadening to
  lower-intent audiences over time).
