---
name: debate-room
description: Convene a room of opinionated expert personas to debate a question and produce a multi-viewpoint answer that's sharper than any single perspective. Use this skill whenever the user wants to stress-test an idea, pressure-test a strategy, get multiple expert perspectives on a decision, run something past "the team," simulate a debate or war room, get devil's-advocate pushback alongside constructive input, or wants a more robust answer than a single viewpoint would give. Also trigger on phrases like "what would [a strategist / a skeptic / my team] say about this," "stress test this," "poke holes in this," "give me multiple perspectives on…," "debate this," "run this past the agency," "convene the room," or any request that implies wanting friction between viewpoints rather than a single synthesised take. Especially useful for positioning, naming, messaging, strategy, and high-stakes decisions where disagreement is productive.
---

# Debate Room

A framework for convening a room of opinionated expert personas, running them through an independent-briefing → tension-mapping → synthesis process, and producing an answer that's more robust than any single viewpoint.

## The core idea

Most "multi-perspective" answers collapse toward a single voice because all the perspectives share one context window. This skill deliberately breaks that: each persona is briefed *independently* as a separate subagent, so they can't anchor on each other. Only then does the orchestrator map tensions and synthesise. This is what turns "Claude wearing five hats" into something structurally more robust.

The value is in the **friction**, not the agreement. Personas are strong-voiced and opinionated on purpose. If the room comes back with polite consensus, the skill has failed.

## How to use this skill

1. **Read the user's question carefully.** What kind of question is it (positioning, naming, strategy, creative, messaging)? What would a *useful* answer look like?

2. **Pick a room.** Look in `rooms/` for a matching room config. Current rooms:
   - `marketing-agency.md` — positioning, naming, messaging, brand, creative, GTM narrative
   - `company-strategy.md` — high-altitude company decisions for businesses generally: pivots, market entry, build/buy/partner, org bets, capital allocation
   - `vc-backed-startup-strategy.md` — the venture-backed variant of `company-strategy`, with the investor seat in the default roster and the founder/investor tension as the load-bearing dynamic. Use when the company has institutional capital and the question turns on board dynamics, fundraising posture, or outcome-shape pressure.

   Read the matching room file. It tells you the default roster and when to deviate. If no room matches cleanly, compose a custom roster from `personas/` using the composition rule.

3. **Pick the roster.** The room gives you a default, but you're allowed (encouraged) to swap personas from the bench if the question calls for it. Enforce the composition rule: **at least 3 different axes represented, and at least 1 stance persona** (someone whose job is to create pressure regardless of content). This prevents echo chambers by construction.

4. **Run the phases in order.** Read each phase file when you get to it — they contain the actual instructions for that phase:
   - `phases/1-framing.md` — input sufficiency check, missing-perspective prompt, decide roster, emit visible roster card, write tailored briefs
   - `phases/2-perspectives.md` — dispatch independent subagents for each persona
   - `phases/2.5-rebuttal.md` — **default-on for decision questions** — personas see each other and concede / hold / sharpen, with conditional steelman of the losing option
   - `phases/3-tensions.md` — map agreements, disagreements, blind spots, and load-bearing assumptions
   - `phases/4-synthesis.md` — produce the final answer (TL;DR with lead condition + tensions + recommendation + assumptions + full transcript)

   Phase 2.5 is default-on. Skip only for quick gut-checks, genuine clean convergence in phase 2, or explicit user request. Two rounds of stress-testing showed rebuttal is consistently where the real decision forms.

5. **Output format.** The final deliverable is always *both*: a synthesised answer up top, and the full transcript (each persona's independent response + the tension map) underneath. The user gets to see the working, not just the conclusion.

## The persona spec

Every persona in `personas/` follows the same spec so they're swappable across rooms and the orchestrator can reason about composition:

```
name:            who they are
axis:            functional | role | stance | horizon | worldview | archetype | lived-experience
one-line:        what they are in a sentence
worldview:       what they believe is true (2–4 bullets)
cares about:     what they optimise for
dismisses:       what they refuse to care about
tells:           verbal tics, vocabulary, things they always say
blind spots:     where they're reliably wrong (the synthesis phase needs this)
pairs well with: personas that sharpen them
clashes with:    personas that productively oppose them
```

**The blind-spot usability test.** A blind spot is only useful if, in phase 3, the orchestrator can write a specific sentence of the form *"[persona] couldn't see [X] because of their blind spot around [Y]."* A vague blind spot like "can be too negative" fails this test and can't do its job in the synthesis. When writing or reviewing a persona, apply this test to each blind spot — if you can't imagine a concrete phase-3 sentence it would enable, sharpen it until you can.

**The axes matter.** Each axis produces a different *kind* of disagreement:

- **functional** — fights about craft and methodology
- **role** — fights about priorities and constraints
- **stance** — fights about direction of pressure (pro vs. con vs. steelman)
- **horizon** — fights about time (this quarter vs. this decade)
- **worldview** — fights about first principles (how does marketing/business actually work)
- **archetype** — fights with a specific person's documented intellectual ammunition
- **lived-experience** — fights with ground truth from outside the room

A room built from a single axis is brittle. A good roster spans at least three.

## Composition rule (enforce this)

Before dispatching perspectives, check the roster:

- At least **3 different axes** represented
- At least **1 stance persona** (e.g. contrarian-skeptic) to guarantee pressure
- No two personas doing the same job

If the default roster for a room doesn't satisfy this for the specific question, swap personas from the bench or flag it to the user.

## Tone

Personas should sound like real people with taste, pet peeves, and things they refuse to entertain — not neutral experts. If a persona output reads like a Wikipedia summary of their field, the persona file is too bland and needs sharpening. Caricature-adjacent is the target.

## Persona library: shipped + personal

The skill supports two persona libraries, merged at runtime:

1. **`personas/`** (inside the skill bundle) — the default library that ships with the skill. Curated, versioned, shared with anyone who installs it. Do not write to this folder at runtime; it's the canonical shipped set.

2. **`~/.claude/debate-room/personas/`** (user's home directory, outside the skill) — the user's personal library. Persistent across sessions, survives skill updates, not overwritten when the skill re-installs. This is where promoted invented personas get written, and where users can hand-write their own personas or override shipped ones.

**At startup, the orchestrator should load both folders and merge them.** On name conflicts, the user folder wins — this lets users override a shipped persona (e.g. sharpen the contrarian-skeptic for their own taste) without forking the whole skill.

**When a user approves a promotion in phase 4**, write the new persona file to the user folder, not the skill bundle. Create the folder if it doesn't exist: `mkdir -p ~/.claude/debate-room/personas/`.

**Environment detection.** If the runtime has no writable filesystem (e.g. Claude.ai chat), only the shipped `personas/` folder is available and promotion gracefully degrades. In that case, at the end of phase 4 still offer to show the invented persona's full spec so the user can copy-paste it into their own notes — but tell them plainly that the skill can't persist it in this environment. In Cowork / Claude Code / any environment with a writable home folder, the user library is available and promotion writes a real file.

## Inventing personas on the fly

The persona library in `personas/` is a starting point, not a ceiling. If a specific question calls for a perspective that no existing persona covers, the orchestrator is allowed — encouraged — to invent a new one on the spot. A regulatory expert for a compliance-heavy question, a community manager for a brand-in-public question, a specific named archetype ("channel the voice of a cynical tech journalist") — whatever the question actually needs.

The point is that the room should adapt to the question, not the other way around.

### Ephemeral by default

An invented persona lives for one session only. The orchestrator drafts the full spec inline (same fields as the library personas: axis, worldview, cares about, dismisses, tells, blind spots, pairs/clashes), uses it in phase 2 like any other persona, and includes the full spec in the transcript so the user can see *who just spoke and why*. No file gets written.

### Promote on approval only

At the end of synthesis (phase 4), if an invented persona earned its seat, offer the user: *"I invented [name] for this question — want me to save them to the library for future rooms?"* Only write a file to `personas/` if the user says yes. This keeps the library curated rather than letting it bloat with slightly-different variants.

### Guardrails

1. **Justify the invention.** In the transcript, state in one sentence *why* the existing personas don't cover this perspective. If "brand-strategist with a slight twist" would've worked, use the brand-strategist — don't invent laziness.
2. **Respect the composition rule.** An invented persona still counts toward the axis count. Inventing a third functional persona doesn't improve the spread; inventing a worldview or lived-experience persona probably does.
3. **Follow the full spec.** Same fields as the existing personas, including blind spots and productive clashes. A persona without stated blind spots is one the synthesis phase can't correct for — don't skip them.
4. **Don't reinvent the stance seat.** The contrarian-skeptic stays. Inventing a softer "skeptic-ish" persona is almost always the orchestrator dodging real pressure. If you want more pressure, strengthen the brief, don't swap the seat.
5. **Max one invention per run.** Soft cap. If a single question needs two invented personas, that's a signal the room itself is wrong for the question — consider telling the user and suggesting a different room (or flagging that a new room should be built).

### Flag to the user

When an invented persona is used, say so plainly in the TL;DR or recommendation: *"Note: I added [persona name] to the room for this question because [reason]."* The user should never be surprised by who was in the room.

## Convergence drift — the skill's central failure mode

The debate room produces value through friction between viewpoints. When that friction is fake, the value is fake. **Convergence drift** is the name for the specific failure mode where the room *appears* to agree but the agreement is an artefact of the generation process, not a discovery about the question. If convergence drift is happening and the orchestrator doesn't catch it, the user gets a confidently-synthesised single-voice answer in multi-voice drag — which is worse than a single-voice answer, because the user trusts it more.

### Why it happens (root causes)

1. **Shared-context anchoring.** When personas are written sequentially in one context window (instead of being dispatched as independent subagents), each new persona anchors on the ones before it. The model is doing next-token prediction over a context that already contains the earlier viewpoints, and the result is a harmonised version of a single voice in costumes. This is why phase 2 *must* use the Task tool when available and *must* flag single-context runs as degraded.
2. **Single-writer identity.** Even with real subagent dispatch, every persona is written by the same base model with the same training distribution. Claude has characteristic takes — it likes nuance, disfavours strong claims, gravitates toward "both/and" framings, finds integrative syntheses aesthetically pleasing. Personas are costumes over a single underlying voice. This can't be fully solved, only mitigated.
3. **Narrative gravity in synthesis.** Knowing a final answer is coming leaks backward into how disagreements get characterised in phase 3. Tensions get rounded off toward tidy resolutions because the writer can already feel the shape of phase 4. This is why phase 3 must be written with phase 4 closed — do not load the synthesis template until the tension map is complete.
4. **Politeness and concession bias.** The rebuttal phase invites personas to "concede / hold / sharpen" — and concede is psychologically the easiest option. Holding a minority position after seeing good counter-arguments requires a persona to say "I hear you and I still disagree," which is rhetorically costly even between fictional characters. This is why phase 2.5 reframes concede as the exception, not the default, and requires a specific justification sentence.

### How the skill structurally fights it

- **Phase 2:** independent subagent dispatch — required whenever *any* subagent-dispatch tool is available (`Task` in Claude Code, `Agent` in Cowork, equivalents in other runtimes); the orchestrator must actually check its tool list rather than reading "Task tool" literally and falling back to inline because the Claude Code name isn't present. Inline runs must be labelled as "single-context approximation mode" in the transcript header and must state the randomised persona order explicitly before writing any persona, with active flushing between writes.
- **Phase 2.5:** concede is the exception (requires justification sentence); forced minority hold rule for open-ended questions where the room has converged without discrete options; conditional steelman rule for discrete-option questions; last-word rule (unanswered attacks count as silent concessions); concession-rate smell test
- **Phase 3:** at least one irreducible disagreement is mandatory, or the orchestrator must state explicitly in writing that none was found (which is a live user-facing flag, not a formality); phase 4 template must be closed while phase 3 is written
- **Phase 4:** single-voice self-audit before the TL;DR ("would a single-voice answer have produced this?"); mandatory blind-spot discount sentence; irreducible disagreement carried through from phase 3

### What you're looking for as the orchestrator

Watch for these tells that convergence is drift, not discovery:

- The stance persona's "hold" reads like everyone else's "sharpen" (fake disagreement)
- Concessions in the rebuttal round use phrases like "good point, agreed" or "on reflection" without a specific assumption being named as wrong (polite capitulation)
- Tension map resolutions feel tidy — every disagreement has been neatly closed off (narrative gravity)
- The final recommendation could have been written by any competent advisor with no room at all (single-voice leakage)
- Personas reference each other's vocabulary or framing in ways that only make sense if they had seen it (shared-context anchoring)

When you see these, the answer is not to rationalise them — it is to stop and apply the relevant structural fix. A run that catches its own drift and says so honestly is more valuable than a run that produces a clean-looking answer and buries the drift.

## When NOT to use this skill

- Simple factual questions (just answer them)
- Questions where the user clearly wants one specific viewpoint, not a debate
- Questions where there's an obvious right answer and friction would just add noise

When in doubt, ask the user whether they want the full room or a quicker take.
