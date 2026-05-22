# Phase 1: Framing

Before dispatching any personas, do the following in the main context (you are the "agency founder" orchestrator).

## Step 0: Input sufficiency check (do this FIRST)

Before anything else, check whether you actually have enough to run a useful debate. Dispatching six subagents on an under-specified question is the most expensive way to produce a mediocre answer.

Ask yourself honestly:

- **Is the question clear?** Do you know what decision or output the user wants? "Help me with my positioning" is not a question; "here are three candidate taglines, which lands best for our ICP" is.
- **Is the context rich enough?** Do you know who the company is, what the product does, who the buyer is, what stage they're at, and what constraints matter? If personas would have to guess at the basics, they'll each guess differently and the debate will be noise.
- **Are the constraints known?** Budget, timeline, brand guardrails, must-not-cross lines, previous attempts. Debates that ignore real constraints produce recommendations the user can't use.
- **Is there a real tradeoff in the question?** The skill adds value where friction is productive. If the answer is obvious or single-dimensional, a debate wastes the user's time.

If any of the above is missing, **stop and ask clarifying questions before dispatching anything**. Aim for one round of clarification, not three — batch the questions, keep them specific, and explain why you're asking (so the user knows the questions will make the debate sharper, not just stall it).

**Skipping this step is the exception, not the default.** There are exactly three cases where it's correct to proceed without clarifying questions: (1) the user is running this as a quick gut-check, not a real decision; (2) the user has explicitly said "run it as-is" or is framing this as a skill test; (3) the question is already sufficiently framed that a clarifying round would just be stalling. If you find yourself about to skip and none of these apply, that's convergence-drift behaviour before the debate has even started — stop and ask. Running on an under-specified question almost always ends with a phase 4 deliverable that punts the real framing work back to the user as "open questions you need to answer," which is a polite way of saying the skill did half the job.

Only proceed to step 1 once the question, context, and constraints are clear enough that a smart expert could engage with them directly.

**Why this matters:** a well-framed question with rich context produces a sharp debate from a small roster. A poorly-framed question with thin context produces a mushy debate from any roster — and adding more seats makes it worse, not better. If you find yourself wanting to expand the roster "to cover all the angles," that's usually a signal the question is unclear, not that you need more personas.

## Step 1: Read the question properly

Actually read it. What is the user really asking? Positioning? Naming? Messaging? Strategy? A creative concept review? Sometimes the stated question and the real question differ — e.g. "is this a good name" is often really "is our positioning right."

## Step 2: Pick the room

Look in `rooms/` and pick the matching room file (e.g. `marketing-agency.md` for positioning/naming/messaging, `company-strategy.md` for high-altitude company decisions). Read it now. If no room matches cleanly, compose a custom roster using the composition rule in SKILL.md.

## Step 3: Decide the roster

**Before picking anyone, answer this one question in writing:** *"What is the single perspective that, if missing from this room, would make the recommendation wrong?"*

Answer it honestly before you look at the roster. For a landing-page question it's probably the actual buyer; for a pricing question it might be the CFO; for a naming question it might be the line-level copywriter; for a compliance-heavy question it might be a regulatory voice. Name the perspective in one sentence. Then check: does a shipped persona in the library actually cover it, or are you about to run the debate without the one voice that matters most?

This step exists because the orchestrator has a default bias toward the shipped library (it's right there, it's convenient) and under-triggers the invent-a-persona path. Forcing the "what would be missing" question *before* roster selection makes invention a deliberate decision rather than an afterthought.

Now start with the room's default roster. Then sanity-check it against the question:

- Does this question have a specific angle the default roster is missing? (e.g. naming question → consider copywriter bench sub; category creation → consider category-historian)
- Does the default roster satisfy the composition rule? (≥3 axes, ≥1 stance persona, no duplicates)
- Is anyone in the default roster dead weight for *this* question?
- **Is there a load-bearing seat the question is implicitly about?** If the question is "how do we compete against better-funded rivals," capital is the subject of the question and CFO is load-bearing — do not drop it because the question "feels strategic." If the question is about execution capacity, operator-COO is load-bearing. If the question is about category creation, category-historian is load-bearing. When doing swaps, ask: *"Which seat's worldview, if absent, would let the room skip the hardest version of this question?"* That seat is load-bearing and must stay in the roster regardless of how tempting it is to drop for a sexier swap.

**Target 4–6 seats.** Four is the floor for genuine axis diversity; six is the ceiling before the orchestrator's ability to track and cross-reference everyone in the tension-mapping phase degrades. If you find yourself wanting more than six, **go back to step 0** — you're probably compensating for an unclear question by adding seats. Narrow the question instead of expanding the roster.

Make swaps from the bench if needed. Write down the final roster and *why you chose it* — this goes into the transcript.

**Consider inventing a persona.** If the question calls for a perspective no existing persona (library or bench) actually covers, draft a new one inline using the full spec (axis, worldview, cares about, dismisses, tells, blind spots, pairs/clashes). See the "Inventing personas on the fly" section in SKILL.md for the rules — ephemeral by default, justify why existing personas don't fit, respect the composition rule, don't replace the stance seat, max one invention per run. An invented persona is treated identically to a library persona from here on.

## Step 4: Write tailored briefs

**This is the single most important step in the framing phase.** Each persona gets a *different* brief. Not the same prompt sent to five people.

Each brief should:

1. **Restate the user's question in the terms *that persona* would actually engage with.** A brand strategist hears "should we call it X or Y" as "what category entry point are we trying to own." A product marketer hears it as "which name lets the AE explain this in ten seconds." Frame the question so the persona has something real to bite into.

2. **Include only the context that persona needs.** Don't dump the whole user prompt onto everyone. The end customer doesn't need the founder's backstory; the founder-ceo-proxy doesn't need a competitor feature matrix.

3. **Match briefing depth to persona type.** Different personas need different kinds of stimulus to do their job well — this isn't a rigid table, it's a judgement call, but here's the principle:

   - **Lived-experience personas** (end-customer and similar) need *concrete stimuli*. Paste the actual options, the actual words, the actual page copy. They react to specifics, not abstractions. If you summarise, you kill the signal.
   - **Craft-led functional personas** (copywriter, creative-director) also need *the actual artefacts* — the specific lines, names, or visuals under discussion. They work at the syllable/shape level and can't engage with summaries.
   - **Strategic functional personas** (brand-strategist, product-marketer) need the *decision frame* — the question, the alternatives, the stakes. They don't need every word of the source material, but they do need to know what choice is actually being made.
   - **Stance personas** (contrarian-skeptic and similar) need the *argument structure* — the case for the leading option, the reasoning behind it, the assumptions being made. Their job is to attack the logic, so give them the logic.
   - **Role personas** (founder-ceo-proxy, sales-leader) need the *context of consequences* — who has to live with this decision, what commitments it implies, what it says about the company.

   Err on the side of more specificity, less meta-commentary. Personas react better to raw material than to your interpretation of it.

4. Tell them explicitly: "You are [persona]. Respond in character. Be opinionated. If you disagree with the premise of the question, say so. Do not try to be balanced — your job is to give your view, sharply. Other experts will give theirs separately."

5. Ask for structured output:
   - **Position** (1–3 sentences: what do you think)
   - **Reasoning** (the actual argument)
   - **Key assumptions** (what would have to be true for you to be right)
   - **What would change your mind**
   - **What you think the other experts in the room will miss**

The last field is gold for the tension-mapping phase.

## Step 5: Emit the roster card (visible to the user)

Before dispatching anyone, emit a visible roster card to the user. This is a short markdown table with one row per persona. The columns are:

| Persona | Axis | Role in this room | One-line brief |

Also state, right after the table: the "missing perspective" answer from step 3, the composition-rule check (axes count, stance seat present, no duplicates), and — if an invented persona is in the roster — a one-sentence justification for the invention.

**The roster card is non-blocking visibility, not gated approval.** Emit the card, tell the user plainly: *"Dispatching the room now — interrupt if you want to swap or add anyone before I spend the tokens."* Then proceed immediately to phase 2. Most runs will proceed without interruption; the value of the card is that the user *could* interrupt if the roster is wrong, and that the orchestrator has committed to a roster in writing (which improves the orchestrator's own reasoning).

**One exception — block briefly if you invented a persona.** Invented personas are higher-risk than shipped ones, and a bad invention will burn the whole run. If the roster includes an invented persona, pause after the card with: *"I invented [name] for this run because [reason] — ok to proceed, or want to adjust the roster first?"* Wait for a short acknowledgement before dispatching. This is a one-line pause, not a full approval gate.

## Step 6: Record the plan

Before moving to phase 2, write down (in the transcript you're building for the user):

- The question as you're interpreting it
- The "missing perspective" answer from step 3
- The final roster and why
- A one-line summary of each persona's brief
- Any clarifying questions you asked in step 0 and the user's answers

Then proceed to phase 2.
