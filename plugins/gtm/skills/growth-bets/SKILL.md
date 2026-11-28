---
name: growth-bets
description: >-
  Turn a growth model into a ranked portfolio of near-term growth bets. Use when the
  user asks what growth moves to make next, wants growth priorities, an experiment
  plan, a 30/60/90-style sequence, a proof plan, or a shortlist of bets to validate
  or accelerate a model. This skill owns what-to-do-next and in-what-order; hand the
  underlying how-should-we-grow question to growth-model and route-to-market detail
  to channel-map. Prefer running it after growth-model has set the engine and motion;
  if no model exists, infer a lightweight one first and label it. Produces a small,
  evidence-graded portfolio of bets with assumptions, proof steps, metrics,
  owner/capacity notes, stop criteria, and handoffs. Not for the growth model itself
  (growth-model), full channel maps (channel-map), single-channel execution, or broad
  marketing audits.
---

# Growth bets

This skill turns growth strategy into action.

`growth-model` says: "this is how the business should grow."

`growth-bets` says: "given that model, these are the best moves to prove or
accelerate it."

The output is not a brainstorm and not a list of tactics. It is a ranked portfolio of
bets, small enough to run, clear enough to judge, and tied to the growth model.

## Posture

Optimistic, selective, and practical. The skill should create momentum without
pretending every idea deserves oxygen.

If a requested idea is weak, do not just reject it. Reframe it into one of:

- a narrower test
- a better-timed later bet
- a different bet that tests the same underlying assumption
- a park decision with a reopen condition

## What counts as a growth bet

A growth bet is a meaningful move that either proves or improves the growth model. It
is bigger than a task and more grounded than an idea.

Good bets usually do one of these:

- prove the engine can work
- add fuel to the engine
- improve a lubricant: activation, conversion, retention, pricing, onboarding, sales
  efficiency, proof
- test whether a boost can become a repeatable system
- create a product or content surface that compounds
- clarify a buyer, use case, or adjacent user

Bad bets are usually:

- disconnected from the model
- just "do more marketing"
- a channel with no assumption or proof plan
- too large to learn from quickly
- a vanity metric in disguise
- an execution task pretending to be strategy

## Cold-start mode

If the company is just launched or chasing its first ~100 customers and the model has
no proven engine yet, load `references/cold-start-plays.md` and run in cold-start mode.
The frame below is unchanged, but a "bet" becomes a manual traction play whose job is
to *find a repeatable acquisition motion*, not just add volume. The reference supplies a
readiness gate to run first, a curated play library to rank from (do not run the menu),
five stances to push back with, and an exit test for when the scramble graduates into a
proper ranked bet. Default to 2-3 plays, each with a learning goal, graded
engine-candidate vs boost and honest vs grey.

## Inputs to read

Preferred input: a `growth-model` output.

Also read where available:

- ICP, positioning, messaging, channel-map, marketing audit or GTM plan
- current traction, retention, activation, source mix, sales/pipeline data
- founder/team capacity and appetite
- current roadmap and planned campaigns
- known constraints: budget, product surface, data visibility, sales capacity,
  brand/proof gaps

If no growth model exists, infer a lightweight one first (likely engine, fuel,
biggest lubricant, relevant boosts, motion, confidence), label it provisional, and
recommend `growth-model` if the uncertainty is load-bearing.

## Workflow

### 1. Lead with the portfolio call

Open with the recommendation in plain language:

- the one bet to run first
- why that bet first
- the main thing to stop or defer
- the key proof signal

Do this before listing the portfolio.

### 2. Restate the model baseline

In 3-6 bullets, name the model assumptions the bets are built on: engine, fuel,
motion, constraint, current pull signal, capacity. This stops the bet list becoming a
generic experiment backlog.

### 3. Generate candidate bets by role

Generate candidates across these roles, then cut hard:

| Role | What it does |
|---|---|
| Engine bet | Proves or accelerates the primary compounding mechanism. |
| Fuel bet | Creates more of the input the engine consumes. |
| Lubricant bet | Improves efficiency: activation, conversion, retention, pricing, onboarding, sales process or proof. |
| Boost bet | Creates a useful spike at an inflection point, clearly labelled as non-compounding unless proven otherwise. |
| Learning bet | Resolves a strategic uncertainty cheaply. |

Do not force one of each. The portfolio should reflect the actual model.

Three reference libraries deepen the roles when you need the menu and the grounding.
Pull the relevant one rather than re-deriving from memory:

- **Engine bet** -> `references/engine-archetypes.md`. The growth-loop taxonomy (viral,
  content, paid sub-types), the four engine families, and the two fits
  (product-channel, channel-model) that gate any engine bet.
- **Lubricant bet** -> `references/lubricant-levers.md`. Activation, retention and
  monetization levers, each with a bottleneck test and benchmarks, in Sean Ellis order
  of leverage.
- **Proof plan (step 6)** -> `references/experiment-patterns.md`. Fake door, concierge,
  Wizard of Oz, pre-sales and more, matched to the assumption, with signal benchmarks
  and the pre-committed decision rule.

(Automation / agentic opportunities — using agents to change the economics of a bet —
are their own analysis and out of scope here. Note the opportunity and hand it to the
dedicated agentic-opportunity skill rather than dressing it up as a growth bet.)

### 4. Gate, then score

Two pass/fail **gates** first. A bet that fails either is out, no matter how well it
scores on anything else — this is what stops a seductive but unrunnable or off-model
bet sneaking through on points:

- **Model-fit gate.** Does this bet prove or improve the chosen engine/model? If not,
  it's a distraction — cut it. (If the model *itself* is in doubt, that's a
  `growth-model` question, not a bet.)
- **Capacity-fit gate.** Can the actual team run it now? If not, it isn't "run now" —
  it's "instrument-first" or "hire-first" (see the verdicts below).

Then score only the survivors on these lenses. Numbers are optional; the reasoning
must be visible.

| Lens | Question |
|---|---|
| Evidence | What signal says this might work? |
| Prize | If it works, is the upside meaningful for this stage? |
| Speed to signal | How quickly can we learn something real? |
| Effort | What does it cost in money, time, attention and product work? |
| Reversibility | Can we stop or adapt without much damage? |
| Compounding potential | Does success make future growth easier? |
| Learning value | Will it answer a question that matters even if it fails? |

### 5. Rank into a small portfolio

Default to 3-5 bets. Fewer is fine. More is usually avoidance disguised as
thoroughness. Use this vocabulary:

- **Run first** — the lead bet. Best mix of prize, learning value, speed and effort
  among the gate-passers.
- **Run next** — strong, but depends on the first bet or capacity opening up.
- **Instrument first** — promising, but the team cannot see the result yet (failed the
  data side of capacity-fit).
- **Narrow and test** — too broad as proposed; run the smaller proof version.
- **Park** — not now; include the reopen condition.

### 6. Write a proof plan for each live bet

Each live bet needs: assumption tested, action, audience/segment, expected mechanism,
leading metric, decision threshold, duration or sequence marker, owner/capacity note,
double-down / adapt / stop criteria, handoff if needed. Use thresholds where the
evidence supports them; otherwise use directional signals and say they are
directional.

For the proof step, match the test to the assumption using
`references/experiment-patterns.md` and write the decision rule before the bet runs, not
after. The cheapest test that resolves the riskiest assumption wins.

### 7. Name what to stop

Stopping is part of the strategy. Name the activity, channel, campaign, project or
habit that should be paused to create capacity for the bets. If there is no clear
stop, say which capacity tradeoff the user must make.

### 8. Hand off to the right skill

- `channel-map` for route-to-market detail on a bet.
- `growth-model` if the bets depend on a model assumption that is still unclear.
- `icp` if the bet depends on buyer clarity.
- metrics / measurement work if the first blocker is visibility.
- PMM / launch skills if the bet is a launch, narrative or announcement.
- org-design / hiring work if capacity or ownership is the constraint.

## Output template

Adapt, but keep the order.

```markdown
# Growth bets - [company]

> Lead: run [bet] first because [reason]. Stop/defer [thing]. The proof signal is [metric/signal].

## Model baseline
- Engine: ...
- Fuel: ...
- Motion: ...
- Constraint: ...
- Pull signal: ...
- Capacity: ...
- Confidence: ...

## Gates (pass/fail before ranking)
- Model-fit: [which candidates passed / what was cut and why]
- Capacity-fit: [which can be run now / which are instrument-first or hire-first]

## Ranked portfolio
| Rank | Bet | Role | Verdict | Why |
|---|---|---|---|---|
| 1 | ... | Engine / Fuel / Lubricant / Boost / Learning | Run first | ... |
| 2 | ... | ... | Run next | ... |
| 3 | ... | ... | Narrow and test | ... |

## Bet cards
### 1. [Bet name] - [verdict]
- Assumption tested: ...
- Action: ...
- Audience / segment: ...
- Expected mechanism: ...
- Leading metric: ...
- Decision threshold: ...
- Owner / capacity: ...
- Double-down if: ...
- Adapt if: ...
- Stop if: ...
- Handoff: ...

### 2. [Bet name] - [verdict]
- ...

## Sequence
1. First: ...
2. Then: ...
3. Later / only if proven: ...

## What to stop or park
- Stop: ...
- Park: ... Reopen if ...

## Instrumentation / evidence needed
- ...

## Handoffs
- channel-map: ...
- growth-model: ...
- icp / metrics / PMM / org-design: ...
```

## Quality rules

1. Lead with the recommended first bet.
2. Keep the portfolio small. Default 3-5, not 12.
3. Every bet ties back to the model baseline.
4. Apply the two gates before ranking; a bet that fails model-fit or capacity-fit does
   not get ranked on the other lenses.
5. Every live bet tests a named assumption and has a metric or proof signal.
6. Do not confuse a task, channel, or campaign with a bet.
7. Label boosts as boosts. They may still be worth doing.
8. Be honest about capacity. If no owner exists, the bet is not ready to run.
9. Include a stop/park list.
10. End with handoffs, especially to `channel-map` where route detail is needed.

## Common failure modes to avoid

- Producing a generic experiment backlog.
- Recommending every plausible channel.
- Treating "do content" as a bet without a mechanism.
- Using traffic, impressions or signups as proof when the model needs activation,
  qualified pipeline, revenue, retention or expansion.
- Ranking a high-scoring bet that quietly failed the model-fit or capacity-fit gate.
- Hiding uncertainty. Mark it, then design the proof step.

## Method lineage

Use these as lineage, not as copy:

- Reforge / Brian Balfour: growth loops, racecar, product-channel fit, channel-model
  fit, engines versus boosts.
- Sean Ellis / Rahul Vohra: must-have signal, high-expectation customers, PMF before
  scale.
- Andrew Chen: adjacent users and channel decay.
- Lenny / OpenView / Growth Unhinged: B2B growth channels, PLG realities, product-led
  marketing, product-led sales, growth hiring, and stage-aware scaling.
- Inference doctrine: strategy before tactics, visible assumptions, and clear
  recommendations a team can actually run.
- Cold-start specifically: Paul Graham / YC ("Do Things That Don't Scale", launch
  repeatedly), and field practice on early-traction distribution, scrubbed to the
  honest, compounding versions. See `references/cold-start-plays.md`.
- Engine, lubricant and proof libraries carry their own lineage (Balfour / Reforge
  loops and four fits, Sean Ellis activation and ICE, Elena Verna motions-x-levers,
  Savoia / Ries experiment patterns, Lenny benchmarks). See the three reference files.
