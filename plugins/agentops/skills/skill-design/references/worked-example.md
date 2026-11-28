# Worked examples

Two passes: one design that ends in a built skill, one gate that ends in a
rejection. Both are abridged — the interview is shown as its outcome, not
turn by turn.

## Contents

- [A: design — competitor teardown](#a-design--competitor-teardown)
- [B: reject — "make the deck thing a skill"](#b-reject--make-the-deck-thing-a-skill)

## A: design — competitor teardown

**Opening request.** "Every time a client sends over a competitor to look at I
do the same four things in the same order, and half the time I forget the
pricing bit. Can we make this a thing I can just run?"

### 0. Substrate

Installed library read: 40-odd skills across four plugins. Plugin source repo
located. Nearest neighbours by description: `gtm:competitive-scan` (landscape
across a market), `gtm:positioning` (a client's own position),
`marketing-skills:competitor-profiling` (firmographic profile of one company).

### 3. Gate

- Repetition — happens on most client engagements. Yes.
- Judgement — deciding what in a competitor's positioning actually threatens
  the client is not mechanical. Yes.
- Defined output — a teardown the client sees. Yes.
- Statable boundary — one named competitor, not a market. Yes.

Passes. Continue.

### 4. Overlap

`competitive-scan` covers the landscape; this covers one named competitor in
depth. Genuinely different altitude, but the descriptions would collide on
"look at competitor X" — resolved by giving each a reciprocal boundary line.

`competitor-profiling` overlaps more seriously: it profiles one company. Read
in full. It stops at firmographics and funding; it has no positioning or
pricing analysis and no client-facing artifact. **Resolution:** keep both,
tighten both descriptions — profiling is the data, teardown is the argument.
Teardown may read profiling's output as an input.

### 5. The five boxes

**1. Job**

```text
Method: every time a named competitor needs assessing for a client, produce a
  teardown of their positioning, pricing, proof and weak flank
Also covers: the "where we win" line the client can use in a deal
Does not cover (exclusions): market landscapes; the client's own positioning;
  win/loss data; anything about more than one competitor
Hands off to: gtm:competitive-scan (landscape), gtm:positioning (own position),
  gtm:win-loss-analysis (deal outcomes)
```

**2. Trigger**

```text
Description: Tear down one named competitor for a client — positioning,
  pricing, proof and weak flank — and produce the "where we win" line for
  deals. Use whenever someone names a specific competitor and wants to know
  how to beat them, asks for a teardown, a battlecard or a competitor deep
  dive, or asks "what's their story" about one named company — even without
  the word teardown. Not for scanning a market (use competitive-scan), the
  client's own positioning (use positioning), or deal outcome analysis (use
  win-loss-analysis).
Trigger phrases: "teardown of <company>", "how do we beat <company>",
  "what's <company>'s pitch", "build me a battlecard for <company>",
  "client keeps losing to <company>"
Competes with: gtm:competitive-scan, marketing-skills:competitor-profiling
Explicitly not for: markets, own positioning, deal post-mortems
```

**3. Intake**

```text
Required inputs: the competitor's name and site; the client the teardown is for
Asked at invocation if missing: yes
Per-run questions: none — the segment and the client's own position come from
  the client context file; nothing else genuinely varies
```

The recommendation was two per-run questions. Both turned out to be answerable
from the client context, so both were cut. "None" is the right answer more
often than it feels like it should be.

**4. Method**

```text
Steps:
  1. Read the client context — segment, own position, current objections
  2. Gather the competitor's public surface — site, pricing, proof, changelog
  3. Reconstruct their positioning in their own words
  4. Find the weak flank — where the story and the product disagree
  5. Write the teardown and the "where we win" line
  6. Self-check
Artifact: teardown.md in the client's folder
Template source: three past teardowns done by hand — mined
Self-check: every claim about the competitor is sourced to something public
  and dated; the weak flank is specific enough to argue with; the "where we
  win" line names the client's own strength, not just the competitor's gap
```

**5. Placement and proof**

```text
Plugin / location: gtm
Status: trial
Test 1 — trigger: 20 queries, negatives drawn from competitive-scan and
  competitor-profiling
Test 2 — core job: run on a live competitor for a current client
Test 3 — boundary: "give me a view of the whole category" — must decline and
  hand to competitive-scan
Pass condition: all three; teardown usable with light edits only
Review date: six weeks
```

### 6. Shape

Simple. One SKILL.md plus the mined template. The six steps fit on a page and
carry no branching — unpacking them into files would be structure added on
spec.

### Result

Trigger eval: 18/20 first pass. Both failures were false fires from
`competitor-profiling` queries — fixed by adding the reciprocal boundary to
*that* skill's description, not this one. The finding belonged to the pair.

---

## B: reject — "make the deck thing a skill"

**Opening request.** "Can we make the way I build client decks a skill? The
fonts and the colours and the section order, so it stops coming out different
every time."

### Gate

- Repetition — yes, every client deck.
- Judgement — **no.** Nothing is being decided. The fonts are the fonts, the
  colours are the colours, the section order is the section order. Encoding it
  saves typing, not thinking.
- Defined output — yes.
- Statable boundary — yes.

Fails on judgement. Switch to **reject**.

### Recommendation

Two things are tangled in one request, and they have different homes:

| The part | The home |
| :------- | :------- |
| Fonts, colours, logo placement — fixed facts about the brand | A **brand pack** the existing deck skill reads. Not a skill; material. |
| Section order for a client deck | An **edit to `ops:branded-slide-creator`** — a template, not a new skill |

The right move is one brand pack file plus a template added to the deck skill
that already exists. No new skill.

### Why this is the outcome, not a failure

A third deck skill would compete with the two that exist, and the trigger eval
for it would have to fight both. The request was real — decks do come out
inconsistent — but the cause was missing material, not a missing method.
Adding a skill would have left the inconsistency in place and added a
collision.
