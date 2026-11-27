---
name: essence-craft
description: "High-craft brand essence, tagline, and signature-phrase work — the small handful of words that define a brand. Use when an essence, tagline, claimed word, manifesto opening line, or signature phrase needs to land with inevitability. Trigger when the user requires lines with more craft, a copywriter or creative director, or wants wordsmithing-class output. Sits downstream of positioning and brand foundations, upstream of messaging frameworks. Do NOT use for body copy, long-form messaging, positioning statements, value props, or general brand strategy."
---

# Essence Craft

The skill for the small handful of words that define a brand. The kind of work where five words can be worth fifty pages — and where a generated list of fifteen options is a sign the work has not yet begun.

## What this skill is for

This skill handles short-form, high-craft brand language:

- **Brand essence** — the central idea (≤5 words, ideally 2–3). *Belong Anywhere. Think Different. Live Más.*
- **Taglines** — the consumer-facing signature line. *Just Do It. Impossible Is Nothing.*
- **Signature phrases** — recurring brand-owned language used across surfaces. *For Those Who Do. The Ultimate Driving Machine.*
- **Claimed words** — the single word the brand owns. *Different. Belong. Do. Refresh.*
- **Manifesto first lines** — the opening that earns the next 200 words. *Here's to the crazy ones.*
- **Category names** — when claiming a new market frame (rare but consequential). *Digital employee. Halloween costume for adults.*

The unifying property: short, ownable, sonic, generative. Not body copy. Not value props. Not messaging frameworks. Not positioning statements. Those are different disciplines and have their own skills (`messaging-framework`, `positioning`, `language-market-fit`).

## Where this sits in the stack

```
[Positioning]  →  [Brand Architecture & Foundations]  →  [Essence Craft]  →  [Messaging Framework]  →  [Language-Market Fit]
                                                            ↑
                                              "What 2-5 words encode the
                                              whole brand idea?"
```

Essence craft sits *between* foundations (what does the brand believe?) and messaging (what does the brand say?). Without an essence, messaging fragments. With one, every downstream surface compounds.

**Inputs this skill needs:**
- Some positioning clarity (a positioning canvas or informal)
- Some brand foundations (purpose, archetype, worldview)
- Access to source material — founder transcripts, customer interviews, sales calls, internal docs, prior brand work

**Output this skill produces:**
- One or two distilled essence (or tagline) candidates with full case
- Each with: derivative sketches (a headline, a product name, a manifesto opening) to test generative power
- Honest failure mode for each candidate
- The cuttings room (5–10 candidates that didn't make the cut, briefly noted, so the user can see what was killed)

## Why this skill exists

Most attempts at brand essence work fail in one of two ways:

**Failure mode 1: strategy-tier output.** Options are generated against a strategic rubric (differentiation, scaling, rally) and look fine on a scorecard but feel engineered when read aloud. They sound generated, not discovered. The reader's response is "that's reasonable" rather than "that's it." The work has not done its job until the response is "that's it."

**Failure mode 2: generated-list disease.** Ten or fifteen options presented in a grid with annotations. This is what an LLM does by default. It is not what a creative director does. A creative director brings two candidates and defends them. A list of fifteen is a sign that the work of culling has been outsourced to the client.

This skill exists to do the work between "we have a strategy" and "we have a line." That work is craft, not strategy, and it has its own discipline.

## The methodology

Six phases, run in order. Each phase has a reference file with the detail.

### Phase 1 — Source-mine (verbatim raid)
**Reference:** `references/process.md` § 1

Before generating anything, pull verbatim phrases from the founder, customers, sales calls, internal docs, prior brand work. Build a *word bank* of phrases that already carry meaning in this brand's world. Great essences often already exist in someone's mouth — the job is to find them, not invent them. Skipping this phase is the most common reason essence work fails.

### Phase 2 — Diverge wide
**Reference:** `references/process.md` § 2

Generate 60–80 candidates fast. No annotation. No rubric. Mix literal, lateral, found-language (from the word bank), wordplay, sonic, double-meaning, claimed-word, surprising-verb. Volume and range, not quality.

### Phase 3 — Cull ruthlessly (craft tests)
**Reference:** `references/craft-tests.md`

Apply the craft gates — not strategy gates. Kill 90% in one pass. The seven craft tests are: inevitability, claimed word, music, layer, surprise, generative power, mouth test. These are different from the strategy tests (differentiation, scaling, rally) and catch different failure modes.

### Phase 4 — Develop survivors deep
**Reference:** `references/process.md` § 4

Take 3–5 survivors (default 5; fewer if the user has asked for a single recommendation). For each, write a 150–200-word case, sketch derivatives (a headline, optionally a sub-brand product name, optionally a manifesto opening line), find the failure mode honestly, and identify what word is being claimed.

### Phase 5 — Stress with legends
**Reference:** `references/personas.md`

Convene a room of five creative-director personas — Hegarty, Neumeier, Abbott, Gallop, Wieden — to attack and defend each survivor. Borrows the `debate-room` mechanic. The room's job is to surface the strongest case and the strongest critique for each candidate — not to kill down to one unless the user has requested a single recommendation.

### Phase 6 — Deliver the range
**Reference:** `references/process.md` § 6

Deliver 3–5 candidates with developed cases, organised by worldview or territory so the user can see the genuine choice between them. Flag a recommendation if one stands out, but make clear the user can pick a different candidate. Not fifteen with grids. The discipline is that each candidate has earned its developed case; the breadth is in the worldviews represented, not in option count. Include the cuttings room (5–10 killed candidates, one-line each) so the user can see what was considered and rejected.

**Output mode override:** If the user explicitly asks for "one with conviction" or "the recommendation, no alternates", deliver a single candidate with full case + the cuttings room. Default is range.

## Routing logic

1. **If the user has a positioning + brand foundations but no essence** → run all six phases.
2. **If the user has draft essence options that aren't landing** → start at Phase 1 (source-mine — almost certainly skipped), then run 2–6. Do not start at "improve these options."
3. **If the user wants a tagline (not an essence)** → same six phases. Tagline craft is essence craft with different output conventions (more product-y, more permission to be consumer-facing).
4. **If the user wants a single product name or category name** → run Phases 1–3 only. Phases 4–6 are for ideas big enough to need stress-testing.
5. **If the user is mid-flow and an existing essence "doesn't sing"** → don't tweak. Re-run from Phase 1. The lack of sing is a symptom; the cause is upstream.

## The reference canon

`references/creative-canon.md` collects 12–15 great essences and signature phrases (Airbnb, Nike, Apple, BMW, Honda, Tesco, Avis, Volvo, Patagonia, Innocent, Mailchimp, Liquid Death, Oatly), with a short analysis of what makes each work. Load it during Phases 2 and 3 to keep the bar visible.

## Common failure modes (watch for these)

- **Skipping Phase 1.** The single most common failure. Everything that follows generates *about* the brand instead of *from* it. Symptom: candidates feel engineered.
- **Annotating during Phase 2.** Annotation kills divergence. Generate first, judge later.
- **Using strategy tests in Phase 3.** Strategy tests catch positioning failures, not craft failures. A candidate can be strategically differentiated and still feel dead.
- **Producing fifteen final candidates with thin annotations.** Five is the cap on the default range output. Each candidate must have a developed case (not a one-line note). A list of fifteen with grids has lost the discipline of the cull and become generated-list disease.
- **Single-voice synthesis.** If every persona in Phase 5 agrees, the room has failed. The skill's value is the friction. Re-read `debate-room`'s convergence-drift section.
- **Trying to be brave when the brand is timid.** The essence has to fit the company that will use it. A brave essence wasted on a timid org is worse than a competent one used well.

## What this skill is NOT for

- Body copy or long-form messaging → use `messaging-framework` or `language-market-fit`
- Positioning statements → use `positioning`
- Brand architecture decisions → use `brand-architecture`
- Visual identity → out of scope for any of these skills
- Slogans for campaigns (different discipline — campaign creative is downstream)
- Internal team-rallying language that doesn't need to scale outside the company

## Output conventions

Deliverables from this skill should always include:

1. **The candidate(s)** — the line itself, in display formatting (large, alone).
2. **The claimed word** — the single word the brand is claiming as its own.
3. **The 200-word case** — why this, with reference to the worldview and the customer.
4. **The derivative sketches** — three downstream uses to prove generative power.
5. **The failure mode** — written honestly, not buried.
6. **The cuttings room** — 5–10 killed candidates with one-line notes, so the user can see what was considered.

Save outputs as markdown in the user's working folder. Use the date-prefix convention if they have one.

## Working with incomplete information

If the source material for Phase 1 is missing or thin, do not proceed. Flag the gap. Ask for transcripts, customer interviews, or founder language. Generating without source material is what produces engineered-sounding work. The skill is allowed — encouraged — to refuse to start until the inputs exist.

If the user has prior rounds of essence work that didn't land, treat those rounds as *evidence about what's missing*, not as a starting point. Read them, note what they over-indexed on, but generate fresh from Phase 1.
