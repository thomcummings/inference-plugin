# Phase 2: Independent perspectives

Now dispatch each persona as a **separate subagent** using whatever subagent-dispatch tool your runtime exposes. Tool names vary by environment: it's called **`Task`** in Claude Code, **`Agent`** in Cowork mode, and is generally unavailable in Claude.ai chat and the raw API. **Use whichever one is present.** Do not assume "Task tool" literally — if you have `Agent`, that is the tool, and running inline because "Task isn't available" when `Agent` is sitting right there is the single most common way this skill silently degrades into a single-voice answer. Check your actual tool list before concluding you're in degraded mode.

This is the structural move that makes the whole skill work — independent context windows mean the personas can't anchor on each other, which is the only way you get genuinely different viewpoints instead of five variations of the same answer.

**This is the single most load-bearing requirement in the entire skill.** The whole value proposition rests on real independence. If the personas are written sequentially in the same context window, each persona will anchor on the ones before it — the model is literally doing next-token prediction over a context that already contains the other viewpoints, and the result is a polite harmonised version of a single voice in costumes. That failure mode is silent: the output still *looks* like a debate. It just isn't one.

## Dispatch rules

1. **One subagent per persona, dispatched via whichever subagent tool your runtime provides** (`Task` / `Agent` / equivalent). Do not put two personas in one subagent. Do not "simulate" the personas in the main context window if a subagent tool is available — that defeats the entire point. Before concluding you're in degraded mode, actually check your tool list for *any* subagent-dispatch capability.

2. **If no subagent-dispatch tool is available**, you are running in **single-context approximation mode**. This is a meaningfully weaker version of the skill. You must:
   - State it plainly in the transcript header: *"⚠️ This run was executed in single-context approximation mode (no subagent-dispatch tool available in this runtime). Personas were written sequentially in one context, which means later personas may have anchored on earlier ones. The real skill dispatches personas as independent subagents. Treat the convergence in this run with extra skepticism."*
   - **Write personas in randomised order**, not the order listed in the room file. **Before writing any persona, state the randomised order you will use, in writing, in the transcript.** The order must visibly differ from the room-file default order; if by chance your shuffle produces the default order, re-shuffle. Stating the order up front makes the randomisation auditable — an unverifiable claim to have randomised is worse than no claim, because it looks like the drift defence is working when it isn't.
   - **Before writing each new persona, actively flush.** Re-read only the tailored brief and the persona file. Do not re-read the previous personas' responses. Your job is to enter the next persona's head cold, not to harmonise them.
   - **After all personas are written, run the whole-room variance check below with the anchoring question explicit**: did this persona's vocabulary or framing echo the previous ones in ways that suggest anchoring rather than independent reasoning? If yes, re-write the anchored persona with a sharper mandate.

3. **Launch them in parallel** (single message, multiple Task tool calls) so the whole room runs at once.

4. **Each subagent gets:**
   - The persona file contents (read `personas/<persona>.md` and include the full spec in the prompt)
   - The *tailored* brief you wrote in phase 1 (not the raw user question)
   - The structured output format from phase 1
   - An explicit instruction: "You have not seen what any other expert said. Answer from your own perspective only. Do not try to be balanced or cover other angles."

5. **Do not share persona outputs between personas.** Phase 2 is fully independent by design. (Phase 2.5, the rebuttal round, is when they see each other — not now.)

## Subagent prompt template

```
You are roleplaying a specific expert persona in a structured debate room.
Your job is to give YOUR view, sharply and in character. You are not trying
to be balanced. Other experts will give their views separately.

=== YOUR PERSONA ===
<paste full contents of personas/<persona>.md>

=== THE QUESTION (framed for you) ===
<the tailored brief from phase 1>

=== GROUND RULES ===
- Answer from what you have. Do NOT ask for more information, more context,
  or more source material. If you feel you'd need more to be fully rigorous,
  answer anyway from what you can see — your job in this room is a sharp
  opinion, not a complete analysis. Caveat your answer if you must, but
  commit to a position.
- Stay in character throughout. Use your persona's voice, tells, and biases.
- If you disagree with the premise of the question itself, say so and
  explain why — but still commit to an answer.
- Do not try to be balanced. Other experts are being briefed separately to
  hold other positions. Your job is *your* view.
- **Ground claims in evidence or name them as assumptions.** This rule is
  non-negotiable and exists because the single biggest failure mode of
  in-character personas is confidently-asserted numbers that the model
  invented. If you make a specific empirical claim — a revenue figure,
  a market size, a growth rate, a customer count, a unit-economics
  number, an exit multiple, a percentage — you must do one of three
  things with it:
    1. Cite it to information in the user's question or provided context
       ("per the brief, they're at ~$X ARR")
    2. Mark it explicitly as an estimate or assumption ("ballpark, I'd
       put this at $X — unverified, flagging for the tension map")
    3. Refuse to commit to a number at all and talk in directional terms
       ("the shape is small-and-profitable, not big-and-burning — I
       don't have a specific ARR figure and won't fabricate one")
  Confidently stating "they're at $30–50M ARR" when you have no basis for
  it is the failure mode. Personas that do this bias the whole room
  toward conclusions built on invented foundations, and the skeptic seat
  is especially prone to it because "tough numbers" feel like rigour.
  Tough numbers without sources are the *opposite* of rigour — they are
  rigour-theatre. If you notice yourself about to write a number, ask:
  *"Where did I get this? Can I cite it or am I inventing it?"* If
  you're inventing it, mark it or drop it.

=== OUTPUT FORMAT ===
Respond in character using exactly these sections:

**Position**
(1–3 sentences: what you actually think)

**Reasoning**
(Your actual argument. Use your voice. Reference your worldview and tells.
Be specific. Cite examples if relevant. Do not hedge.)

**Key assumptions**
(What would have to be true for you to be right? List them honestly.)

**What would change your mind**
(Be concrete. What evidence or argument would move you?)

**What the other experts in the room will miss**
(Your prediction about the blind spots of the rest of the roster.
This is the most important field — it's what the orchestrator uses to
surface real tensions later.)
```

**Why the "answer from what you have" rule matters:** the most common phase-2 failure mode is a persona (especially a stance persona like the skeptic) dodging the question by saying "I need to read the full document" or "I need more context." That's skepticism masquerading as rigour. Pre-empt it in the brief so you don't have to re-dispatch.

## When subagents return

Collect each response verbatim. Do not edit or "clean them up" — voice and sharpness are the whole point, and sanitising them flattens the output. Preserve them for the transcript.

### Per-persona sanity check

If any *individual* response comes back bland, generic, or too balanced, re-dispatch that persona with an explicit note: "Your previous response was too neutral. You are [persona]. Be opinionated. Pick a side. Other experts will take other positions — your job is yours."

### Whole-room variance check (do this before moving on)

Now look at the room as a whole. Did the personas actually disagree, or did they all land in roughly the same place with slightly different vocabulary?

Ask yourself:

- **Do the headline positions actually differ?** If four out of six personas are recommending the same option with different reasoning, that might be genuine convergence — or it might mean the briefs were leading. Check the briefs: did you frame the question in a way that implied a preferred answer?
- **Did the stance persona actually push back?** If the contrarian-skeptic wrote something that could have come from any of the functional personas, the brief was wrong or the persona isn't being used properly. Re-dispatch with a sharper attack mandate.
- **Are the disagreements about substance, or just about framing?** Substance disagreements ("option A is right because X; option B is right because Y") are gold. Framing disagreements ("we should think about this differently") are weaker signal.

**If the room converged too cleanly:** stop and decide which of these is true:

1. **The question genuinely has an obvious answer** — fine, proceed to phase 3 and let the synthesis say so plainly. Not every debate produces drama.
2. **The briefs were leading** — re-brief with tighter neutral framing and re-dispatch. Don't proceed on a false-consensus round.
3. **The personas weren't opinionated enough** — re-dispatch with sharper character instructions.

A false-consensus round is worse than a no-debate round because it produces a confident-sounding synthesis that the user will trust. Catch it here.

Once you're satisfied the room actually did its job, proceed to phase 3 — or, if you plan to run a rebuttal round, note that and proceed to phase 2.5.
