# Essence Craft — Process Reference

The detailed methodology for Phases 1, 2, 4, and 6 of the essence-craft skill. Phases 3 and 5 have their own reference files (`craft-tests.md`, `personas.md`).

---

## Phase 1 — Source-mine (verbatim raid)

**The premise.** A great essence usually already exists in someone's mouth. The founder said it on a call. A customer said it in a sales conversation. An employee said it on Slack. The raw phrase is somewhere in the source material — the job is to find it, not invent it. This is the phase that most essence work skips, and skipping it is the most common reason essences come out feeling engineered.

**What to mine.** Pull verbatim language from:

- **Founder/CEO** — recorded calls, internal memos, podcast appearances, fundraising decks, all-hands talks, Slack messages they wrote themselves. The founder's own language carries more brand DNA than anyone else's.
- **Customers** — sales call transcripts, support tickets, NPS comments, customer-quote slides, case study interviews. Look for the words customers use about the product, *not* the words salespeople use to describe it.
- **Sales conversations** — recorded discovery and demo calls. The phrases that land and get repeated. The phrases that come out of customer mouths unprompted.
- **Internal documents** — product overview decks, brand guidelines, audit synthesis, prior brand work, internal wiki entries. Often contain phrases that never made it to the website.
- **Cultural references the brand orbits** — books the founder cites, brands they reference, manifestos they admire. These show the language register the founder reaches for naturally.

**What you're looking for.** Three types of raw material:

1. **Found phrases** — complete or near-complete phrases that already work. *"Belong Anywhere" came from Brian Chesky himself. "Just Do It" came from a death-row inmate's last words. "Think Different" came from a long internal manifesto. Found phrases are gold.*
2. **Claimed words** — single words used repeatedly with conviction. The word the brand keeps reaching for. Sometimes a competitor uses the same word generically; that's fine — the brand still claims it through usage.
3. **Cultural tensions** — language that names a tension or fight the brand is in. *"Craft" vs "admin." "Small firms" vs "national chains." "Getting paid" vs "getting by."*

**The output of Phase 1: a word bank.** Markdown document with three sections. The example below is for a fictional brand, job and invoicing software for independent tradespeople:

```markdown
## Phrases (verbatim)
- "I didn't start a business to do paperwork at 11pm" — founder, podcast appearance
- "The van is the office" — founder, kickoff workshop
- "Paid before the paint dries" — customer interview
- "Small firms, big standards" — founder, brief
- "Proper work" — founder, recurring
- [continue, 20-30 entries]

## Claimed words (single words, with usage examples)
- "proper" — the founder's recurring frame: proper work, proper pay
- "finish" — the founder and customers both use it for a job done well
- "trade" — founder, sales team, customers
- [continue, 10-15 entries]

## Cultural tensions (the fights the brand is in)
- Craft vs admin — the founder's explicit frame: the job is the work, not the paperwork
- Independent trades vs national chains — small firms held to big standards
- Getting paid vs getting by — cash flow as the real constraint
- [continue, 4-8 entries]
```

**Time check.** Phase 1 should take 20–40% of the total run. If you spend less than that, you have not done the work. If a user pushes to skip it — push back. Phase 1 is the differentiator between this skill and "generate me ten options."

**Gap check.** If the user does not have source material — no transcripts, no internal docs, no recorded calls — stop. Do not proceed to Phase 2. Tell the user what you need, why, and what they can do to gather it. Generating in the absence of source material is what produced the engineered options that triggered this skill in the first place.

---

## Phase 2 — Diverge wide

**The premise.** Volume and range, not quality. The point of Phase 2 is to flood the field with candidates so the cull in Phase 3 has something to work with. Annotation kills divergence; do not annotate during this phase.

**Generate 60–80 candidates.** Yes, that many. Not 10 with annotation. Not 15 with a rubric. 60–80 fast, with no commentary.

**Cover these eight families** (aim for 8–10 candidates per family — the families exist to prevent monoculture):

1. **Found language** — straight pulls from the word bank, used as-is or near-as-is. *"Proper Work", "The Van Is the Office", "Paid Before the Paint Dries"*.
2. **Claimed verb** — short phrases built around a verb the brand wants to own. *"Built to Finish", "Made to Last", "Back to the Job"*.
3. **Claimed noun** — phrases built around a noun the brand wants to own. *"Trade Pride", "The Owner's Hour", "Maker's Margin"*.
4. **Sonic / rhythmic** — phrases chosen for music, not meaning-first. Alliteration, assonance, rhythm. *"Fix, Bill, Banked", "Proper Pay, Properly"*.
5. **Double meaning / pun / layer** — phrases with two readings, one obvious and one earned. *"Job Done", "Square Up", "On the Level"*.
6. **Surprising verb** — verbs the category never uses. The category uses *help, assist, optimise, scale, automate*; what does it never use? *Own, back, befriend, raise, anchor, hold, vouch.*
7. **Cultural-tension phrase** — phrases that name the fight the brand is in. *"For the Proper Trades", "Small Firms, Big Standards", "Beyond the Spreadsheet"*.
8. **Inverted / contrarian** — phrases that flip a category expectation. The category says X; this brand says not-X. *"Quiet Power", "Slow Software", "Make Less, Make Better"*.

**Format the output as a flat list.** No headers between families. No annotation. No "this option works because…". Just the phrases.

```
1. Built to Finish
2. Made to Last
3. Proper Work
4. Trade Pride
5. Paid Before the Paint Dries
6. Job Done
7. [continues to 60–80]
```

**Push past the obvious.** The first 20 candidates will be obvious. The next 20 will be derivative. The interesting ones are usually in the last 20–40 — the ones generated when the obvious territory is exhausted and the model has to reach. Do not stop at 30. Keep going.

**Reach for the word bank constantly.** Every 5–10 candidates, re-read the word bank. Use a phrase verbatim. Combine two phrases. Cut a phrase in half. Found language is the unfair advantage Phase 1 gave you — use it.

**Time check.** Phase 2 should take 10–15% of the total run. It should feel like brainstorming, not like writing.

---

## Phase 3 — Cull ruthlessly

**See `references/craft-tests.md` for the seven craft gates.** Phase 3 applies them in a single pass and kills 90% of the candidates. You should arrive at 5–8 survivors.

If you find yourself sparing more than 8 candidates, you are being too generous. Kill more. The skill's whole premise is that one or two candidates with conviction beat ten with annotations.

---

## Phase 4 — Develop survivors deep

**The premise.** Take the survivors from Phase 3. Default is **3–5 survivors** — pick the ones with the most distinct worldviews so the user is choosing between genuine alternatives, not variations of the same idea. If the user explicitly asked for a single recommendation, narrow to three and Phase 5 will pick one. For each survivor, do the deep development work that proves the candidate can carry a brand.

For each survivor, produce:

### 1. The 200-word case
A short prose argument for why this is the brand's essence. Should reference:
- The worldview it encodes (not the feature, not the differentiator — the *belief about how the world should work*).
- The customer it serves and how it lands for them.
- The single word it's claiming (call it out explicitly).
- What it does that the alternatives don't.
- Why it survives the craft tests in `craft-tests.md`.

Keep it to 200 words. Discipline. A 400-word case is the writer hedging.

### 2. Three derivative sketches
Prove the candidate is *generative* — that it spawns downstream work — by sketching three concrete uses:

1. **A headline** (10 words max) for the homepage or a major launch.
2. **A sub-brand product name** — what would the freemium / pro / new product be called, with this essence as the parent?
3. **A manifesto opening line** — the first sentence of a 200-word manifesto that would feel earned given the essence.

If you can't write all three within 5 minutes, the candidate isn't generative enough. Kill it and bring up an alternate from the Phase 3 survivors.

### 3. The failure mode
Write the honest failure mode. Not "could be misunderstood as…". *"The risk with this essence is X, and the way it goes wrong is Y."* Specific and named. Every essence has a failure mode; if you can't find one, you haven't looked.

Examples of honest failure modes:
- *"'Built to Finish' lands as cold if paired with the wrong visual register. It needs warm, human execution everywhere else, or it reads like a hardware brand."*
- *"'Trade Pride' relies on the customer self-identifying with a trade. It lands for the plumber and the electrician, but the owner of a ten-person cleaning firm will read it as not-for-them."*
- *"'For the Proper Trades' takes a side. It will alienate larger firms who don't think of themselves as 'proper trades'. The brand has to be willing to lose those prospects."*

### 4. The single word being claimed
Call it out explicitly. *"This essence claims the word OWN."* This is the discipline of the Bates USP doctrine and Marty Neumeier's brand-as-meme idea — every great brand owns one word in the customer's head.

---

## Phase 5 — Stress with legends

**See `references/personas.md` for the five legendary CD personas.** Phase 5 dispatches each persona to interrogate the three survivors and kills the weakest two.

---

## Phase 6 — Deliver

**The premise.** Default is a **range of 3–5 candidates**, each with a developed case, organised by territory or worldview so the comparison is between distinct alternatives rather than variations on a single line. Flag a recommendation if one stands out. The discipline that protects this from generated-list disease is that *each candidate has earned its developed case* — claimed word, 150–200 word argument, derivative sketch, honest failure mode. A list of fifteen with thin annotations is not a range; it's a dump.

If the user asks for "one with conviction" or "just the recommendation", switch modes: deliver a single candidate with full case + an alternate + the cuttings room. The methodology is the same; only the output format changes.

### Output structure (range mode — default)

```markdown
# [Brand] — Brand Essence Options
**Date:** YYYY-MM-DD
**Methodology:** essence-craft skill, full six-phase run

## The range

[2–3 sentences framing the choice. What territory the candidates collectively cover. What the user is being asked to decide between.]

## Territory 1: [name of worldview]

### [Candidate]
**Claimed word:** [single word]
[150–200 word case]
**Headline sketch:** [10-word headline showing the essence generates downstream work]
**Failure mode:** [honest, named]

### [Candidate]
[same structure]

## Territory 2: [name of worldview]

[same]

## Territory 3: [name of worldview]

[same]

## My read

[2–3 paragraphs naming which I'd push if forced, and why. Explicit about the trade-off: territory 1 says X about the brand, territory 2 says Y. The user is picking a brand temperament, not just a phrase.]

## The cuttings room

[5–10 killed candidates with one-line reasons]

## What the legends said

[Summary of Phase 5 stress test — which candidates each persona backed/killed and why]
```

### Output structure (single-recommendation mode — on request)

```markdown
# [Brand] — Brand Essence
**Date:** YYYY-MM-DD
**Prepared by:** [Claude / consultant name]

## The recommendation

# [The essence, large, alone on the line]

**Claimed word:** [single word]

[2–3 paragraphs of conviction — why this is the brand's essence]

## Why this

[The 200-word case from Phase 4, polished]

## How it lives

**Headline:** [the derivative headline]
**Sub-brand sketch:** [the derivative product name]
**Manifesto opens:** *[the derivative opening line]*

## The failure mode

[The honest failure mode from Phase 4]

## The alternate

If the room can't get behind the recommendation, the alternate is:

# [Second candidate]

[1 paragraph on why this is the alternate — what it does that the recommendation doesn't, and what it gives up.]

## The cuttings room

The 5–10 candidates that didn't make the cut, with one-line notes:

- *[Candidate]* — [one-line reason for kill]
- *[Candidate]* — [one-line reason for kill]
- […]

## What the legends said

[2–3 paragraph summary of the Phase 5 stress test — which persona pushed hardest in which direction, what was killed, what survived.]
```

### The five-candidate cap (range mode)

In range mode, three to five candidates is the cap. The discipline is the *developed case* — every candidate must earn its place with claimed word + 150–200 word case + derivative sketch + honest failure mode. Resist the urge to present six or seven; resist harder the urge to drop the development work and present a grid. The skill's value is high-craft developed candidates, not a wide net.

### The single-candidate variant (on request)

If the user asks for conviction over range — *"give me the recommendation"*, *"one with no alternates"*, *"just tell me"* — present one candidate with full case + the cuttings room. The methodology is identical; only the output framing changes.

### What not to include

- A scoring grid. The grids belong in the working files, not the deliverable.
- A rubric. The user does not need to see the rubric — they need to feel the conviction.
- "Pros and cons" for each candidate. If a candidate has cons that justify presenting it, it was kept for the wrong reason.
- Hedging language. *"This could potentially work because…"* No. *"This is the brand's essence because…"*

### Save and link

Save the deliverable as markdown in the user's working folder. Use the date-prefix convention if they use one. Provide a `computer://` link in chat.
