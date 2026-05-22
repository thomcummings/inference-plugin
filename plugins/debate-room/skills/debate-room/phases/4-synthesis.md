# Phase 4: Synthesis

Produce the final deliverable. The user sees **both** a synthesised answer *and* the full transcript — no exceptions. The synthesis without the transcript hides the working; the transcript without the synthesis is a lot to wade through. Both together is the point.

## Before you write anything: the single-voice self-audit

Before drafting the TL;DR, answer this question honestly to yourself: **"If I had been asked this exact question with no debate room — just a single-voice response — would I have produced something materially similar to the recommendation I am about to write?"**

- If **no**, the room earned its cost. Proceed.
- If **yes**, the room did not earn its cost. You must say so in the synthesis itself, up front, in a dedicated line: *"Honesty flag: a single-voice answer to this question would likely have reached a similar recommendation. The room's contribution was [specific thing the debate added — sharper framing, a surfaced blind spot, a load-bearing assumption, nothing]. If 'nothing,' the user should treat this run as low-value."*
- If **you can't tell**, assume yes and include the flag. The skill's job is to be honest about when it didn't earn its cost, not to rationalise every run as valuable.

This self-audit is not optional. It is the skill's only defence against producing confident-sounding single-voice answers in multi-voice drag. Skip it and the skill silently degrades into a more elaborate way of generating the same answer the model would have given anyway.

## Output structure (use this exact template)

```
# [Question, restated in one line]

## TL;DR
(3–5 sentences. The actual answer. Not a summary of what the room discussed
— the *conclusion* the room reached, with the sharpest version of it first.
If there's a clean recommendation, lead with it. If the honest answer is
"it depends on X," say that and name X.)

**Lead with the load-bearing condition.** If the recommendation depends on
a specific assertion being true (e.g. "this plan only works if the buyer
panel confirms they currently treat this as a replacement for an existing
tool, not a new line item"), that condition goes in the FIRST paragraph,
not halfway down a bullet list. The user has to see the thing-that-has-
to-be-true before they see the plan built on top of it — otherwise they
act on the plan without checking the condition, and if the condition
fails the plan fails silently. The most important sentence in the
synthesis is often the condition, not the recommendation itself.

*If an invented persona was used, note it here: "Note: I added [persona]
to the room for this question because [reason]."*

## The core tensions
(2–4 short paragraphs. The real disagreements the room surfaced, stated
plainly. This is where you preserve the productive friction rather than
smoothing it over. For each tension, say which way you'd lean and why —
but don't pretend a tension doesn't exist just to sound decisive.)

## Recommendation
(What you'd actually do if this were your call. Be specific. Include:
- The call itself
- The reasoning in two or three sentences
- The key risk (the strongest counterargument you're knowingly accepting)
- What you'd watch for that would make you change your mind)

## Assumptions the recommendation depends on
(Pull this from the load-bearing-assumptions section of the phase 3
tension map. List every assertion the plan rests on that the room
*couldn't verify* from the question alone. For each one: name the
claim in one sentence, note which persona asserted it, and mark it
as unverified. These are the things the user should check before
committing. This section is not optional and is not a hedge — a
sharp recommendation resting on named, auditable assumptions is
more useful than a hedged recommendation that hides them. If any
assumption looks easily verifiable in minutes, flag it for the user
explicitly.)

## Blind-spot corrections applied
(This section is mandatory and must contain at least one concrete sentence
of the form: *"Because [persona] has a blind spot around [X], I'm
discounting their [specific contribution] on [specific point] in this
synthesis."* This is the one place where the phase 3 blind-spot sweep
actually gets used to shift the recommendation — otherwise it's just
decoration. If no blind spot meaningfully shifted the synthesis, you
must state that explicitly: *"No blind spot in the roster meaningfully
shifted this recommendation. I noted the blind spots in phase 3 but
none of them changed my lean."* Do not leave this section empty and
do not paper over it.)

## Irreducible disagreement
(Pull this from the phase 3 tension map. At least one tension the
synthesis is NOT resolving — named, with both positions stated fairly,
and with the user told explicitly that this is a call they have to
make based on a belief the room cannot verify for them. If phase 3's
mandatory sentence was "the room produced no irreducible disagreement,"
repeat that sentence here verbatim so the user sees the honesty flag.)

## What the room couldn't answer
(Honest list of things the debate exposed as open questions — things that
need more info, more research, or a decision only the user can make.
Short and concrete. This is where you flag unknowns rather than paper
over them.)

---

## Full transcript

### Room composition
- Room: [room name]
- Roster: [list of personas]
- Why this roster: [one or two sentences]
- Clarifying questions asked at intake (if any): [list with user answers]

### The briefs
(One or two lines per persona summarising how the question was framed for them.)

### Round 1: Independent perspectives
(Each persona's full response, verbatim, in order. Do not edit or clean
them up. Voice is the point.)

### Round 2: Rebuttal (if run)
(Each persona's rebuttal response, verbatim. Include the movement map:
who conceded, who held, who sharpened.)

### Tension map
(The full tension map from phase 3, unedited.)
```

## Rules for writing the synthesis

1. **Preserve disagreement where it's real.** If the brand strategist and the product marketer fundamentally disagree and it matters for the user's decision, the synthesis should say so — not pretend they agreed. "The strategist and the product marketer pull in opposite directions here, and the call depends on X" is a more useful answer than "balance long-term brand with short-term clarity."

2. **Have a point of view.** The orchestrator (you) is not a neutral referee. You've read every response, you've mapped the tensions, you've seen the blind spots. You are allowed — required — to lean. Say which way and why. Hedging everything is the failure mode.

3. **Don't average the personas.** An averaged answer is weaker than any single persona's answer. If the honest synthesis is "the creative director is basically right and the product marketer is over-indexing on this-quarter," say that.

4. **Use the blind-spot sweep.** If the whole room collectively missed something (because their combined blind spots line up), the synthesis is where you add it. This is the orchestrator's unique value — you can see what no individual persona could.

5. **If a rebuttal round was run, reflect room movement, not just your interpretation.** This is a meaningful distinction. Without rebuttal, the synthesis is *the orchestrator's read* of N independent voices. With rebuttal, the synthesis should reflect *where the room actually moved to* — persona movement (concede / hold / sharpen) is data, not noise. If the brand strategist conceded to the copywriter on a specific point, that concession carries more weight in the synthesis than if the orchestrator had simply decided the copywriter was right. The room did some of the work for you; let it show.

6. **Keep the user's voice in mind.** The user asked a real question about their real situation. The final answer has to be actionable for *them*, not a lecture on marketing theory.

7. **Do not sanitise the transcript.** The whole point of showing the working is that the user gets to see the sharp, opinionated, possibly-rude persona voices. Cleaning them up into professional-speak defeats the purpose.

## After delivering

Offer the user follow-ups they can pick from:

- Re-run the room with a different roster (e.g. swap in performance-marketer, or add copywriter)
- **If phase 2.5 was skipped and the user wants more rigour:** offer to run a rebuttal round now. (Phase 2.5 is default-on in v1.2, so this offer only applies to the rare skip case.)
- **If an invented persona was used this run:** offer to save it to the user's personal library — *"I invented [name] for this question. Want me to save them to your personal persona library for future rooms?"* Only write the file (to the user personas folder — see SKILL.md) if the user says yes. If they say no or don't answer, the persona dies with the session.

Don't run these automatically — let the user decide whether the output was enough.
