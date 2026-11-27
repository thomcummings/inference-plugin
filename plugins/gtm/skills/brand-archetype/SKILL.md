---
name: brand-archetype
description: "Translate a company's business strategy into a brand archetype recommendation using the 12 Jungian/Pearson archetypes (Innocent, Citizen, Hero, Caregiver, Explorer, Lover, Rebel, Creator, Magician, Ruler, Sage, Jester). Trigger whenever the user mentions brand archetype, brand personality, 'which archetype fits', 'is this brand a Hero or Rebel', Jung, Pearson, Mark & Pearson 'Hero and the Outlaw', or wants to make brand strategy legible to non-marketers (founders, ops, board) by mapping it to a recognisable character. Also trigger on symptoms like teams using different tones for the same brand, leadership unable to describe how the brand should feel, copywriters guessing at voice, or strategy clear on paper but vague in execution. Produces a scored ranking of all 12 archetypes against the context, with strategic, verbal, visual, and risk analysis for the top 3. Sits downstream of positioning and business strategy, upstream of brand foundations, messaging, and visual identity."
---

# Brand Archetype

A skill for matching a company's strategic context to one (or two) of the 12 brand archetypes — the character types that turn strategy from a paper artefact into something a marketing team, a copywriter, a designer, or a non-marketer can feel and act on.

The archetype is the bridge between "what we're trying to do as a business" and "what we sound, look, and behave like as a brand." It's especially useful when non-marketers (founders, engineers, ops, board members) need a quick handle on what the brand is supposed to be — saying "we're a Rebel" or "we're a Sage" compresses a lot of strategy into one shared mental model.

## Relationship to other skills

```
[Positioning]            "What are we, for whom, against what?"
       ↓
[Brand Architecture]     "How is the brand structured?"
       ↓
[BRAND ARCHETYPE] ←──    THIS SKILL
       ↓                 "What character does this brand embody?"
       ↓                 "What does that imply for voice, look, and behaviour?"
       ↓
[Brand Foundations]      Purpose / vision / mission / pillars / personality
[Messaging Framework]    How the brand actually speaks
[Visual Identity]        How the brand actually looks
```

Archetype work pairs naturally with the personality layer of `brand-architecture` (Phase 2: Foundations). If the user is doing a full brand strategy run, archetype work either feeds *into* the personality section of the foundations document, or — more often — it's the *first* personality move, because it's faster to align on "we're a Sage" than to write a personality manifesto from scratch.

If the user has positioning output (for example a positioning canvas) or any strategic narrative, that's the richest possible input. If they don't, the skill can still work from much less — even just a description of what the company does and who it's for — but the recommendation will be more tentative and should be flagged as such.

## What this skill is for, and what it isn't

**Use it when:**
- The user wants an archetype recommendation grounded in their actual strategy (not a quiz).
- A brand needs a shared character that internal teams (especially non-marketers) can rally around.
- Voice, tone, and visual direction need a north star but the strategy work hasn't translated into anything tactical yet.
- Two or more archetypes are in tension and the user needs help choosing.
- The user wants to pressure-test a hunch ("we're definitely a Rebel, right?").

**Don't use it for:**
- Writing the actual copy or visual system. The archetype is the *brief* for those. Other skills (`messaging-framework`, `brand-asset-renderer`, `essence-craft`) execute against it.
- Replacing positioning work. If the company doesn't know who it's for or what it does, an archetype won't fix that — surface the gap and route to `positioning` first.
- Deciding the archetype based on what feels nice. The point is to derive it from the strategy. Be willing to recommend something the user might not love if that's what the strategy implies.

## The 12 archetypes at a glance

Grouped by core human motivation. The full descriptions, mottos, brand examples, voice cues, and failure modes live in `references/archetypes.md` — read that file when scoring, not before.

**Seek Paradise** (transcendence, optimism, freedom)
- **Innocent** — "Life is good." Purity, simplicity, trust. (Dove, Coca-Cola)
- **Sage** — "To know is to grow." Wisdom, expertise, truth. (CNN, Mayo Clinic)
- **Explorer** — "Live adventurously." Frontier, independence, discovery. (Patagonia, Jeep)

**Leave a Mark** (impact, change, mastery)
- **Rebel** — "Rules are made to be broken." Disruption, defiance. (Harley-Davidson, Apple-era-Think-Different)
- **Magician** — "Make dreams come true." Transformation, vision. (Disney, TED)
- **Hero** — "Where there's a will, there's a way." Courage, achievement. (Nike, U.S. Army)

**Connect with Others** (belonging, intimacy, joy)
- **Lover** — "Follow your bliss." Passion, sensuality, beauty. (Victoria's Secret, BMW)
- **Jester** — "Have fun." Play, wit, levity. (Ben & Jerry's, Skittles)
- **Citizen / Everyman** — "All for one and one for all." Belonging, equality. (Target, IKEA)

**Provide Structure** (order, control, care)
- **Caregiver** — "Love your neighbour as yourself." Compassion, service. (Johnson & Johnson, TOMS)
- **Ruler** — "Control is power." Authority, prestige, order. (Rolex, Louis Vuitton)
- **Creator** — "Imagine the possibilities." Originality, craft, vision. (Lego, Adobe)

## How to run the skill

### Step 1 — Gather context (working folder first, then ask)

The quality of the recommendation depends entirely on how much real strategic context is on the table. Don't skip this.

1. **Read the working folder first.** Look for: positioning docs, brand foundations, mission/vision/purpose statements, manifestos, About pages, audience definitions, competitor lists, strategic narratives. Common filenames: `brand-system.md`, `brand-foundations.md`, `positioning.md`, `messaging.md`, `manifesto.md`, `about.md`, `strategy.md`, `CONTEXT.md`, `AGENTS.md`.
2. **Summarise what you found** so the user can confirm you've got the right picture.
3. **Identify gaps.** The minimum useful input is: what the company does, who it's for, what makes it different, and how it wants the customer to feel. If any of those are missing, ask with `AskUserQuestion` — but only for what's genuinely missing. Don't re-ask things the working folder already answers.
4. **One more move that's worth the cost:** ask the user what the brand *isn't*. People are often more articulate about what a brand should never be ("not corporate", "not snobby", "not earnest") than what it should be. This is gold for eliminating archetypes.

If the user explicitly says "just take a shot with what's here", do that — but flag at the top of the output that the recommendation is provisional pending strategic clarification.

### Step 2 — Score all 12 archetypes

Read `references/archetypes.md` for the full archetype data, then score each archetype 1–10 against the strategic context. Be honest. Most companies will have one or two genuinely strong matches, three or four near-misses, and the rest will be wrong — that's expected and useful.

For each archetype, write a one-sentence rationale for the score. The rationale should reference something specific from the strategic context, not generic archetype properties. "Score 8: their commitment to 'making invisible work visible' maps directly to the Magician's transformation motif" is useful. "Score 8: they're transformative" is not.

### Step 3 — Deep-dive the top 3

For the top 3 scoring archetypes, produce four things, briefly:

1. **Strategic rationale + business implications.** Why this archetype fits, and what choosing it commits the business to. Be willing to surface uncomfortable implications ("if you're really a Rebel, you have to be willing to lose risk-averse buyers — are you?").
2. **Voice, tone, and messaging implications.** How this archetype talks. Words and phrases to lean into, ones to avoid. Concrete enough to brief a copywriter.
3. **Visual and brand-world implications.** Aesthetic mood, design cues, the *feeling* of the brand world. Don't over-specify — gesture at the territory.
4. **Comparable brands + risks / anti-patterns.** Two or three brands that play this archetype well (and *why* they work). One or two ways this archetype tends to fail when overdone or done lazily (e.g. Lover → kitsch; Sage → boring; Rebel → cosplay).

Keep each section short — one paragraph each is plenty. The point is comprehension speed, especially for non-marketers.

### Step 4 — Make a recommendation

Don't just present the ranking and back away. Take a position. Recommend the single primary archetype (and optionally a secondary "accent" archetype if the top two are genuinely close and complementary). Explain the call in one paragraph. Note what was rejected and why — that's often as instructive as the pick.

The strongest brands embody one primary archetype clearly. Two is sometimes useful as a primary + accent. Three or more dilutes into "we're a bit of everything", which is the failure mode of archetype work.

### Step 5 — Write the markdown file

Save the output to the working folder using the template in **Output format** below. Suggested filename: `brand-archetype-analysis.md` or `<company>-brand-archetype.md` if a company name is in play.

After writing, briefly summarise the recommendation in chat (just the headline pick + one-line "why") and link the file. Don't recapitulate the whole document — the file exists for that.

## Working with sparse or contradictory context

- **Sparse context:** Make the recommendation more provisional and the asks more pointed. State explicitly what you'd need to be more confident.
- **Contradictory signals:** Name the contradiction. "The mission talks like a Sage but the founder talks like a Rebel — which is right?" is more useful than averaging them.
- **Multiple stakeholders with different visions:** Score the archetypes against the *strategy*, not the loudest voice. If the founder's instincts contradict the strategy, flag it and let them decide.
- **Brand new company with no docs:** Lean heavily on what the founder is trying to build and who they want to attract. The archetype here is closer to "what character does the founder want this company to be" than "what character is this company already living out".

## Output format

Save to the working folder as a markdown file. Structure:

```markdown
# Brand Archetype Analysis — [Company]

> One-paragraph summary: the strategic context as understood, the recommended primary archetype, and the one sentence on why.

## Strategic context (as understood)

[3-6 bullets summarising the inputs the analysis is based on. If anything is provisional or assumed, flag it explicitly.]

## Recommendation

**Primary: The [Archetype].** [One paragraph on why.]
**Secondary / accent (optional): The [Archetype].** [One sentence on why this nuances the primary.]

## Top 3 archetypes — deep dive

### 1. The [Archetype] (score X/10)

**Strategic rationale.** [One paragraph.]
**Voice & messaging.** [One paragraph. Include 3-5 words/phrases to lean into and 2-3 to avoid.]
**Visual & brand-world.** [One paragraph gesturing at the aesthetic territory.]
**Comparable brands + risks.** [2-3 brand examples with one-line reasons. 1-2 failure modes.]

### 2. The [Archetype] (score X/10)
[Same structure as #1.]

### 3. The [Archetype] (score X/10)
[Same structure as #1.]

## Full ranking (all 12)

| Rank | Archetype | Score | One-line rationale |
|------|-----------|-------|---------------------|
| 1 | [Name] | X/10 | [Specific to this company's context] |
| 2 | ... | ... | ... |
| ... | ... | ... | ... |
| 12 | [Name] | X/10 | [Specific to this company's context] |

## What was rejected and why

[Short prose paragraph on the archetypes that were close but didn't make the top, and the ones that were obviously wrong. The "obviously wrong" notes are often the most useful part of the document for the team — they make the recommendation feel earned.]

## How to use this

[2-3 bullets on what to do next — typically: feed the primary archetype into brand foundations / personality, hand the voice cues to whoever writes copy, share with the team to align on the character before any execution work.]
```

## Writing style for the output

The audience for the output document is often non-marketers. Match that:

- Use brand examples liberally. "Think Patagonia, not REI" is worth ten lines of abstract description.
- Avoid jargon. If you need a term like "verbal identity" or "category entry point", define it briefly.
- Be willing to be opinionated. Hedging everything ("could be a Hero or could be a Rebel — depends!") wastes the user's time. They came here for a call.
- Keep sections short. The full document should be readable in 5–10 minutes.
- Make implications tangible. "More Sage than Magician" means nothing without "so the homepage should sound more like the Mayo Clinic than like Disney."

## When to *not* recommend an archetype

Occasionally the strategic context is genuinely ambiguous, or the company is at a real inflection point where the archetype is about to change. In those cases, don't force a pick:

- Surface the ambiguity clearly.
- Offer two scenarios ("if you're committing to the new strategy, you're a Magician; if you're protecting the existing business, you're a Ruler — those are different brands, and the company needs to choose which one it's building").
- Ask the user to resolve the strategy question before the archetype question.

This is rare. Default to making a recommendation. But the option exists.

## Method lineage

- Margaret Mark and Carol S. Pearson, *The Hero and the Outlaw* (2001): the twelve
  archetypes, which build on Carl Jung's work on archetypes.
- Inference doctrine: derive the archetype from the strategy, not from taste.
