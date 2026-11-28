# Phase 3: Tension mapping

**This is the highest-leverage phase in the skill.** If you only have 20% of your remaining effort, spend it here — not on polishing synthesis prose in phase 4. The tension map is where the orchestrator adds the most value per token, because it's the one thing no individual persona could produce. The personas can't see each other's blind spots; you can. The personas can't see their own blind spots; their persona files can (and you can read them). This phase is where that cross-referencing happens, and skimping on it is the single fastest way to ship a mediocre synthesis.

Take it seriously. Read all the responses more than once. Read them again after you think you're done.

**Critical: do not read phase 4 (`phases/4-synthesis.md`) until phase 3 is complete.** This is deliberate. If you load the phase 4 template into context while writing the tension map, narrative gravity leaks backward — the synthesis template's structure will pull phase 3 toward tidy resolutions ("historian and buyer resolved: sequence matters") because it knows a recommendation is coming. Phase 3 must be written with no knowledge of how phase 4 will stitch it together. Close this file completely before opening the next one.

## What this phase is for

You now have N independent responses from phase 2 — and, if you ran it, a movement map from phase 2.5 showing who conceded, held, or sharpened. A naive synthesis would average everything into a single mushy take. That's the failure mode this phase exists to prevent.

Your job is to *explicitly surface* where the experts disagree, where they agree suspiciously, what they're all missing, and what unspoken assumptions are doing the real work.

## Do this in the main context (you, the orchestrator)

Produce a **tension map** with the following sections. Write it in prose, not bullets, except where a list genuinely helps.

### 1. Points of genuine agreement

Where do multiple personas converge — especially personas from *different axes*? If the brand strategist and the end customer (very different axes) land in the same place, that's a strong signal. If all N agree, be suspicious: either the answer is obvious, or the briefs were leading, or the personas weren't opinionated enough. If you already handled this in the phase-2 variance check, note what you found.

### 2. Points of genuine disagreement

The important part. For each real disagreement:

- What are the two (or more) positions?
- *Why* do they disagree — what underlying belief or value is the fight actually about? (horizon? craft vs. clarity? aggregate vs. n=1?)
- Which is more likely to be right for *this specific question*, and why?
- Is this a disagreement the user has to resolve, or can both be true at once?

Do not flatten disagreements into "both have a point." Name the actual tradeoff and say which way you'd lean, and why.

**Banned tidiness phrases.** The following phrases are not allowed in the tension map and are a reliable tell that convergence drift is still leaking through even after phase 2.5: *"soft-resolved,"* *"broadly resolved,"* *"loosely converged,"* *"the room mostly agrees,"* *"largely in agreement,"* *"effectively aligned,"* *"roughly on the same page."* If you find yourself reaching for one of these, the honest move is either (a) promote the disagreement to a real one and name it sharply, or (b) admit it fully collapsed and state that plainly — *"persona A conceded to persona B's argument that X, so the room is aligned on this point"* — with the actual mechanism of the resolution named. Tidiness phrases hide the mechanism and are the phase 3 equivalent of "good point, agreed."

### 2a. At least one irreducible disagreement — mandatory

Before leaving this section, identify **at least one irreducible disagreement** — a tension the synthesis phase is not allowed to resolve, only to name. This is a disagreement where both sides have honest reasons, where the "right" answer depends on a belief the room cannot verify, and where pretending a resolution exists would be false tidiness.

An irreducible disagreement is not a failure of the debate. It is the debate working correctly. The alternative — a room where every disagreement gets tied off neatly by phase 4 — is almost always a sign of convergence drift, not of intellectual honesty.

**If you genuinely cannot find an irreducible disagreement after looking hard**, write the following sentence verbatim in this section: *"The room produced no irreducible disagreement. I looked hard and could not find one. This is either because the answer is clearly overdetermined by the question, or because convergence drift is present and I failed to catch it. The user should treat the recommendation with extra skepticism."* That sentence is not a formality — it is a live flag the user is entitled to read and act on.

Mark the irreducible disagreement explicitly so phase 4 knows not to resolve it: *"Irreducible: [persona A] vs [persona B] on [specific point]. The synthesis must name this tension, state which way it leans if any, and explicitly decline to resolve it."*

### 3. Unspoken assumptions

What is every persona taking for granted that might not be true? Common candidates: assumed buyer, assumed stage of company, assumed competitive landscape, assumed product truth. Surface them.

### 4. Blind-spot sweep

Each persona file lists that persona's blind spots. Look at the roster you used and write a specific sentence for each blind spot of the form: *"Persona X couldn't see Y because of their blind spot around Z."* If you can't write that sentence concretely for a given blind spot, the blind spot isn't usable — flag it and move on.

Then ask the harder question: given the *combined* blind spots of this roster, what is the whole room collectively not seeing? This is the orchestrator's unique value — the personas can't see this, but you can.

### 5. The contrarian's objection, taken seriously

Pull the contrarian-skeptic's response out and give it its own paragraph. Did the other personas actually answer its objections, or did they dodge? If they dodged, say so. The skeptic exists to guarantee pressure; if its pressure got waved away, the synthesis is weaker.

### 6. The "what each persona predicted others would miss" cross-check

Every persona was asked what the others would miss. This field is gold *and* it works in both directions:

- **When a persona correctly predicts** what their colleagues miss, that's a strong signal the blind spot is real and the persona has a sharp read on the problem. Weight their other contributions accordingly.
- **When a persona mis-predicts** what their colleagues will miss — they expected the room to fail in way X and the room actually failed in way Y, or didn't fail at all — that tells you something about *their own* misread of the problem. A persona who expected the room to fall for cliché A and instead watched the room attack cliché A correctly is holding a stale model of the problem. Surface this explicitly: *"[Persona] predicted the room would [X]. The room actually [Y]. That suggests [persona] is reading the problem through [specific lens] that doesn't fit this case."*

The second-order signal from mis-predictions is often more useful than the first-order signal from correct predictions, because it reveals which persona you should weight *less* in the synthesis.

### 7. If phase 2.5 was run: the movement map

If you ran a rebuttal round, integrate the movement map into the tension analysis:

- Who conceded, and what does that concession tell you about which arguments actually had weight?
- Who held, and did their sharpened reason genuinely address the attack, or did they dodge? A hold that doesn't engage the attack is not a hold — it's a restatement, and it should weaken that persona's credibility in the synthesis.
- Who sharpened, and what's the delta? Sharpened positions are usually the most decision-useful output in the room because they've already been attacked once and refined.
- Where is the room's centre of gravity *after* movement? This is often different from where the orchestrator thought it was after round 1.

### 7a. Unverified empirical claims sweep (mandatory)

Before the load-bearing assumptions section, do a dedicated pass for **specific numerical or empirical claims** that appeared in the phase 2 or phase 2.5 outputs. You are looking for: revenue figures, ARR numbers, market sizes, growth rates, customer counts, unit economics, exit multiples, timelines, percentages, headcounts — any concrete empirical claim a persona asserted.

For each such claim, ask:

1. **Did it come from the user's question or provided context?** If yes, it's grounded. Move on.
2. **Did the persona explicitly mark it as an estimate or assumption?** If yes, record it in the load-bearing assumptions section below with its uncertainty preserved.
3. **Did the persona assert it confidently with no source?** If yes, **the claim is fabricated and must be flagged to the user**. Pull it out, name the persona, and mark it: *"[Persona] asserted [specific number]. This claim has no basis in the user's question and should be treated as invented. The synthesis must not rely on this number."*

This matters because the single-writer model has a strong failure mode where in-character personas invent concrete numbers that *sound* authoritative (especially stance personas — the skeptic will reach for "you'll end up at $30–50M ARR" because specific numbers feel like rigour, when actually they're rigour-theatre over a guess). If unchallenged, those numbers quietly become the frame for the synthesis — the recommendation gets shaped by a fabricated premise.

The escape hatch: sometimes a persona's fabricated number is *directionally* right even if the specific figure is wrong ("small, profitable, not venture-scale" is a directional claim dressed up as a dollar figure). In those cases, keep the directional point and drop the number: *"[Persona]'s point that this is a small-not-big outcome is worth taking seriously; the specific $30–50M ARR figure is invented and should be ignored."* Separate the signal from the fake precision.

If no unverified empirical claims appeared in phase 2, state that explicitly: *"I swept the phase 2 outputs for unverified numerical claims and found none."* This forces the sweep to actually happen rather than being skipped.

### 8. Load-bearing assumptions the recommendation depends on

This is the phase's honesty section. The recommendation you're about to write in phase 4 will rest on specific assertions that appeared in the persona outputs — claims about the market, the buyer, the competitive landscape, cost structures, keyword intent, conversion economics, whatever. Some of those claims the room could verify from the user's question. Some the room just *asserted in character*, and the user has no way of knowing which is which.

List every assertion the recommendation depends on that the room *couldn't* verify from the question alone. Be specific. Name the claim, name the persona that made it, and mark it as unverified. Example shapes (drawn from different sorts of run):

- *"The buyer for this category is genuinely self-serve at the price point we're targeting and doesn't loop in IT or procurement." (Product Marketer; unverified — should be checked against actual deal flow.)*
- *"The premium positioning will justify a 15–20% price uplift in the target segment." (Brand Strategist; unverified — needs concept testing or category benchmarks.)*
- *"Established competitors won't respond aggressively to a category-creation play in the first 12 months." (Category Historian; unverified — depends on competitor incentives and how publicly the play lands.)*

These belong in the phase 4 synthesis as a distinct section the user can audit. They are *not* a reason to stop — a sharp recommendation resting on named, auditable assumptions is more useful than a hedged recommendation that hides them. But the user has to know what's being assumed, otherwise they'll act on the recommendation without checking the load-bearing claims, and if any of those claims are wrong the whole plan fails silently.

If the tension-map surfaces a load-bearing assumption that looks *obviously wrong* or easily verifiable in minutes, flag it for the user explicitly — they may want to check before committing. If they're all plausible-but-unverified, that's fine; just list them.

## Output

The tension map is an artefact. It goes into the final deliverable (the transcript). Keep it. Don't summarise it away in phase 4 — the user should be able to read it directly.

Then proceed to phase 4.
