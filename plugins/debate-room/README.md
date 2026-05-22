# Debate Room

A Claude Code plugin that convenes a room of opinionated expert personas to stress-test a question and produce a multi-viewpoint answer sharper than any single take.

Built on the idea that most "multi-perspective" answers collapse into a single voice because all the perspectives share one context window. Debate Room deliberately breaks that: each persona is briefed *independently* as an isolated subagent, so they can't anchor on each other. Only after every voice has been heard does the orchestrator map tensions and synthesise.

## What it does

You give it a question — a positioning call, a strategic bet, a naming decision, a messaging dilemma. It convenes the right room of personas, runs them through a five-phase debate, and gives you back a synthesised answer with the full transcript underneath. You see who said what, where they clashed, and what the orchestrator chose to weight.

The value is in the **friction**, not the agreement. Personas are strong-voiced and opinionated by design. If the room comes back with polite consensus, the skill has failed.

## Why a structured debate and not one prompt

Ask Claude "give me five perspectives on X" and you'll get five paragraphs in the same voice wearing different hats. That's because the perspectives share a context window — each new persona anchors on the ones before it, and the result is a harmonised version of a single voice in costume.

Debate Room fights this structurally:

- **Phase 2 (Perspectives)** dispatches each persona as an independent subagent — they don't see each other's responses
- **Phase 2.5 (Rebuttal)** then lets them see each other and either concede, hold, or sharpen — with concede framed as the exception, not the default
- **Phase 3 (Tensions)** maps irreducible disagreements before any synthesis is allowed
- **Phase 4 (Synthesis)** produces a recommendation that has to carry the tensions through, not round them off

The separation is the quality mechanism. You see the working, not just the conclusion.

## Installation

The plugin ships as a standard Claude Code plugin. Install it via your preferred mechanism:

- From a marketplace: `/plugin install debate-room`
- From a local directory: `/plugin marketplace add /path/to/debate-room-plugin` then `/plugin install debate-room`
- From a git repository: follow your marketplace's pattern

Once installed, the skill auto-triggers on phrases like "stress test this," "poke holes in this," "what would my team say about this," "debate this," "convene the room," or any request that implies wanting friction between viewpoints.

## Usage

Just ask Claude to stress-test something:

```
Stress-test this positioning: "the calm CRM for small teams"
```

```
What would the team say about renaming the product to Atlas?
```

```
Convene the room on whether we should raise a Series A now or wait six months
```

The skill picks a matching room, assembles the roster, runs the phases in order, and produces the final deliverable.

## Rooms

The skill ships with three rooms — each one is a default roster plus guidance for when to deviate. Rosters are composable: the orchestrator can swap personas from the bench (or invent new ones on the fly) to match the question.

- **`marketing-agency`** — positioning, naming, messaging, brand, creative, GTM narrative
- **`company-strategy`** — high-altitude company decisions: pivots, market entry, build/buy/partner, capital allocation
- **`vc-backed-startup-strategy`** — the venture-backed variant, with investor and founder seats and board dynamics as the load-bearing tension

If no room matches cleanly, the orchestrator composes a custom roster from the persona library, enforcing the composition rule: **at least 3 different axes represented, and at least 1 stance persona** to guarantee productive pressure.

## Personas

Personas come in two libraries that merge at runtime:

1. **Shipped library** (`personas/` inside the plugin) — the curated, versioned set everyone gets
2. **Personal library** (`~/.claude/debate-room/personas/`) — your own hand-written personas and overrides, persistent across skill updates

On name conflicts, your library wins. You can sharpen the shipped contrarian-skeptic for your own taste without forking the plugin.

The shipped library currently includes brand strategists, product marketers, creative directors, CFOs, COOs, investors, founders, contrarians, first-principles thinkers, category historians, and end customers. Each one has a stated worldview, the things they care about, the things they refuse to entertain, their verbal tics, and — critically — their blind spots, so the synthesis phase can discount their input where appropriate.

### Inventing personas on the fly

The library is a starting point, not a ceiling. If a question calls for a perspective no existing persona covers — a regulatory expert for a compliance question, a community manager for a brand-in-public question, a named archetype like "a cynical tech journalist" — the orchestrator can invent one for the session.

Invented personas are ephemeral by default. At the end of synthesis, if one earned its seat, you'll be asked whether to save it to your personal library for future rooms.

## The five phases

1. **Framing** — input sufficiency check, missing-perspective prompt, roster selection, tailored briefs per persona
2. **Perspectives** — independent subagent dispatch, one per persona, no shared context
3. **Rebuttal** (default-on for decision questions) — personas see each other and concede, hold, or sharpen; concede requires a specific justification sentence
4. **Tensions** — map agreements, disagreements, blind spots, and load-bearing assumptions; at least one irreducible disagreement is mandatory
5. **Synthesis** — TL;DR with lead condition + tensions + recommendation + assumptions + full transcript

You always get both the synthesised answer up top and the full transcript underneath.

## Convergence drift — the central failure mode

The skill produces value through friction between viewpoints. When that friction is fake, the value is fake. **Convergence drift** is the name for the failure mode where the room *appears* to agree but the agreement is an artefact of the generation process, not a discovery about the question.

A confidently-synthesised single-voice answer in multi-voice drag is worse than a single-voice answer, because the user trusts it more. The skill has explicit structural defences against this (independent dispatch, concession justification, mandatory irreducible disagreement, single-voice self-audit before the TL;DR) and the orchestrator flags drift honestly when it can't be eliminated.

## When NOT to use this skill

- Simple factual questions (just answer them)
- Questions where you clearly want one specific viewpoint, not a debate
- Questions where there's an obvious right answer and friction would just add noise

When in doubt, the skill will ask whether you want the full room or a quicker take.

## Architecture

### Independent subagent dispatch

Phase 2 dispatches each persona as a fresh subagent via the Task tool (or equivalent in other runtimes). Each persona gets only its own brief — it does not see the question's full context, the room's other personas, or any prior responses. This is the single most important structural defence against convergence drift.

If no subagent-dispatch tool is available, the skill labels the run as "single-context approximation mode" in the transcript header so you know the friction is degraded.

### File-based state, no infrastructure

Everything works against the skill's own bundle and your local home folder. No databases, no auth, no deployment overhead. The shipped persona library and rooms are versioned with the plugin; your personal personas live in `~/.claude/debate-room/personas/` and survive skill updates.

## Credits and philosophy

Built on the principle that good answers to hard questions come from real disagreement between people who think differently — not from a single advisor playing every role. The skill is an attempt to reproduce, structurally, what a senior team or a well-run war room does when a decision matters: convene the right people, let them disagree in good faith, and force the synthesis to carry the tensions through rather than round them off.

## Licence

(Add your preferred licence here.)
