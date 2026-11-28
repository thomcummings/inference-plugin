# Experiment patterns

The toolkit for the **proof plan** every live bet needs (workflow step 6). A bet tests a
named assumption; this library gives the cheapest honest test for the *kind* of
assumption, plus the discipline that makes the result trustworthy. The point of a
cold-start play or a lubricant bet is to learn something real, fast, before spending
build or budget. The wrong test answers the wrong question.

It is a catalogue of known patterns, lightly framed for use inside growth-bets. The
opinion about which assumption is riskiest belongs in the bet itself; this file makes
sure the proof step is matched, sized and ungameable.

## Match the test to the assumption

| The assumption | Best test | Why |
|---|---|---|
| Is there demand for this at all? | Smoke test / landing page | Measures real intent at scale |
| Demand for one specific feature? | Fake door | Click is the data, inside a real product |
| What price will they pay? | Fake door + A/B on price | Test points against each other |
| Will the solution actually work? | Wizard of Oz | Tests the experience without building it |
| What do they really need? | Concierge | Deep generative discovery |
| Will they pay and commit? | Pre-sales / LOI | Money or signature beats opinion |

## The archetypes

### Smoke test (whole-concept demand)
A landing page or value-prop page for a product that does not exist yet; measure
clicks, signups or pre-orders. Set up in a weekend for under ~$500. Validates that the
core promise attracts and converts strangers. Lineage: Savoia (pretotyping), Ries.

### Fake door / painted door (single-feature demand)
A real-looking entry point (button, nav item, pricing tier) inside an existing product
that, when clicked, shows an honest "coming soon, want early access?" message. The click
is the demand signal. A **painted door** takes the user one or two steps into the flow
before revealing it is not ready, giving richer signal at the cost of more
disappointment. Validates interest, not utility or retention, so follow a pass with a
Wizard of Oz or concierge test.

### Concierge MVP (generative, user knows it is manual)
Deliver the outcome by hand for a few customers, openly. Wealthfront's pen-and-paper
financial plans, FoodOnTheTable's personal grocery shopping. Best when you do *not* yet
know what the solution should be: the human interaction is generative research. The
value prop is higher than the eventual product because a human is in the loop, so it is
the wrong tool for falsifying a specific solution.

### Wizard of Oz (evaluative, manual work hidden)
The user-facing experience looks real and automated, but humans do the work behind the
curtain. Zappos's founder fulfilling shoe orders by hand from local shops. Best when you
*do* have a clear solution hypothesis and want to test the experience and retention
without building the backend. Because the user does not know, it simulates the real
product closely (minus a slight delay).

### Pre-sales / letters of intent (commitment)
Ask buyers to commit money or a signature before the thing exists. The strongest signal
because it costs the buyer something. Three or more pre-orders or signed LOIs is real
demand.

## Sequencing: a funnel of confidence

Run the cheapest test that can resolve the assumption, and only escalate on a pass.
Increasing investment, decreasing uncertainty at each stage:

1. **Smoke test** the promise resonates.
2. **Fake door** to choose between feature directions.
3. **Concierge** with 5-10 converts to understand needs deeply.
4. **Wizard of Oz** to test the specific solution at scale.
5. **Pre-sell** to lock commitment, then build.

Any failed stage saves you the cost of the next one. You rarely run just one.

## Discipline (what makes the result trustworthy)

- **Decision rule before launch.** Write the hypothesis and the pass/fail threshold,
  name the audience, action, value and timeframe, and share it with someone before you
  run it. Defining success after seeing results is moving the goalposts. "If
  click-through > 5% we build; 2-5% we interview; < 2% we kill."
- **Size the sample.** For a binary click decision, a few hundred impressions usually
  separate "no demand" from "real demand"; plan 1,000+ for nuanced signal.
- **Ethical fake doors.** Always show an honest coming-soon message, never charge a card
  without delivering, capture emails so clickers become a research and beta list, and
  cap frequency so the same users are not repeatedly disappointed. The follow-up
  conversation with clickers is what turns a number into a decision.
- **Measure behaviour, not opinion.** Clicks, signups, payments and signatures, not
  "would you use this".

## Signal benchmarks (set thresholds, then read against them)

- **Landing-page / smoke conversion:** 2-5% cold traffic is typical for a compelling
  promise; below 1% is weak messaging or wrong audience; above 5% is a strong signal.
- **Fake door click-through:** below ~1% is no real demand (kill); 5-15% is solid (move
  to the next test); above 15% is strong (prioritise).
- **Waitlist to pre-order:** 10-15% is strong demand; below 5% means the interest was
  superficial.

Treat these as priors, not laws. The threshold you wrote down before the test beats any
benchmark after it.

## Prioritising which experiment to run

When several bets compete for the next test slot, score them rather than argue:

- **ICE (Sean Ellis):** Impact, Confidence, Ease, each 1-10. Fast and good enough early.
- **RICE:** Reach, Impact, Confidence, Effort, when you need reach weighted in.
- **High-tempo testing loop (Ellis):** analyse, ideate into a backlog, prioritise with
  ICE, test, document. Velocity of honest tests is itself the growth lever.

## Using patterns inside growth-bets

For each live bet's proof plan: name the riskiest assumption, pick the matching pattern,
write the decision threshold before running, size the sample, and choose the cheapest
test that resolves it. A bet without a matched, pre-committed proof step is a hope with
a metric attached.

## Method lineage

- Alberto Savoia: pretotyping (fake door, the build-the-right-it idea).
- Eric Ries: lean startup, validated learning, MVP as experiment.
- Tristan Kromer: the concierge-vs-Wizard-of-Oz distinction (generative vs evaluative,
  user awareness).
- Nick Swinmurn / Zappos and Wealthfront: the canonical Wizard of Oz and concierge
  cases.
- Sean Ellis: ICE prioritisation and high-tempo testing.
