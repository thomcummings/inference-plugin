# The content audience profile — and why it isn't the ICP

The single most common reason a piece of content is competent and ignored: it was
aimed at the person the client wants to *sell* to, using a profile built to decide who
to sell to. That profile answers a different question, and it answers it well. It just
can't tell you what will make someone stop scrolling.

This file defines the second profile — the reader-side one — and how to capture it
without inventing it.

## Contents
1. The two profiles, and what each is for
2. Where it lives (on the persona)
3. The profile shape
4. Capturing it
5. Honesty rules
6. How it gets used downstream

---

## 1. The two profiles, and what each is for

|  | ICP / buying persona | Content audience |
|---|---|---|
| Answers | Who should we sell to? | Who are we trying to make *react*? |
| Judged by | Fit, deal size, win rate | Attention, agreement, forwarding |
| Population | The buying group | The buying group **plus** peers, operators, talent, press, investors — usually wider |
| A "trigger" means | A buying trigger: funding round, new VP, contract expiry | A content trigger: an argument that reliably gets a reaction |
| Owned by | `icp` | this skill |

Both are real and neither replaces the other. A client selling compliance software to
Heads of Risk has an ICP of maybe four thousand companies and a content audience that
includes every risk practitioner, consultant and regulator-watcher who will never buy
but will absolutely decide whether the client is worth listening to. Content aimed only
at the four thousand reaches almost nobody; content aimed only at the crowd sells
nothing. The profile has to say which it is.

**The wider-than-the-ICP point is the one to hold.** When a client says "our audience is
our ICP", that is usually a statement about who they wish were reading, not who is. Ask
who shares their stuff today. The answer is nearly always broader, and the gap is where
the reach has been hiding.

## 2. Where it lives (on the persona)

A content audience is a person, so it lives with the personas the team already keeps
(see `icp`), as an additional `## As a reader` section. Enrich the standing persona;
never fork a parallel copy.

- **The audience is already a buying persona** → add the `## As a reader` section to that
  persona.
- **The audience is not a buyer** (the peer crowd, the talent pool, the press) → create a
  new persona for them whose `## As a reader` section records `In the ICP: no` and says
  why they matter anyway.

Keep it a section, not a separate document type. If per-audience content facts ever
outgrow a section on a persona, that is the moment to split them out — not before.

## 3. The profile shape

Append to the persona body. Every heading is required; where the material genuinely isn't
there, write `Not captured yet` rather than filling it in plausibly.

```markdown
## As a reader
**In the ICP:** yes / no — [if no, why they matter: they amplify, they hire, they advise buyers]

### How they see themselves
[The identity they would claim, in their words. "A builder, not a manager." "The only
adult in a room full of hype." Content that flatters or threatens a live identity
travels; content addressed to a job title does not.]

### Sophistication
[How much they already know about the subject. This sets the altitude — what you can
assume without explaining, and what would read as condescending. An audience three years
into a problem does not want the 101, and being given it is a reason to unfollow.]

### What they want to be seen agreeing with
[The positions they would share because sharing says something about them. Distinct from
what they privately believe — this is about the public act. It is the strongest single
predictor of whether a piece travels.]

### What reliably gets a reaction
[Arguments, framings and subjects that have visibly landed with this audience. Say where
you saw it, so a later reader can weigh it.]

### What makes them switch off
[The anti-triggers: claims they distrust, words that read as marketing, formats they have
seen too often, the register that makes them assume nobody serious wrote it. Usually
sharper and more useful than the triggers, and usually easier for a client to answer.]

### When and where they read
[The actual moment — commuting, between meetings, deliberately researching a purchase,
in a group chat someone forwarded it to. Bounds length and format more than any style
rule does.]

### Who they already trust
[Named people, publications, podcasts, communities. Two jobs: it says which register they
already accept as credible, and it says what they are already saturated with — a shape
they see five times a week from voices they trust is a shape the client cannot win on.]

### Their words for it
[Verbatim language this audience uses for the problem — theirs, not the client's. If the
client calls it "revenue orchestration" and the audience calls it "the handover mess",
the profile records both and content uses the second.]
```

## 4. Capturing it

Three ways in, and one rule: the client is the source, you are the scribe.

- **From what's written down first.** The personas, the ICP, any point-of-view
  storylines, and whatever the client has already said about who reads them. A good
  deal of this is often already lying around in unstructured form.
- **From evidence they have.** Whatever they can actually see: who engages, who replies,
  who forwards, which posts got shared into other people's networks, what the sales team
  hears repeated back. If they have none of this, say so in the profile rather than
  reasoning it out from the category.
- **By asking, when there's nothing else.** The four questions that produce the most per
  minute: *Who shares your stuff — and is it who you expected?* *What do you believe that
  this audience would argue with?* *What makes you close a post from someone in your
  field?* *Whose writing in your space do they take seriously?*

The last two populate **What makes them switch off** and **Who they already trust**, which
are the two sections clients answer fastest and the two most often skipped.

**Refresh it, don't file it.** An audience profile written once and never revisited is
worse than none, because it gets trusted. Revisit when the content stops landing, when
the client moves upmarket or into a new segment, or when the answer to "who shares this?"
changes — and replace the old version with a dated new one rather than editing in
place, so the drift is visible.

## 5. Honesty rules

- **Never invent an audience.** `Not captured yet` is a real answer and a useful one. An
  invented trigger becomes a drafting instruction three weeks later and nobody remembers
  it was a guess.
- **Distinguish what they said from what you observed from what you reckon.** A trigger
  the client watched land is different from one you inferred from the category, and the
  profile should show which is which.
- **Don't flatter the client's idea of their audience.** If they describe a sophisticated
  practitioner audience and the evidence shows their reach is mostly peers and job
  seekers, that gap is the most valuable line in the profile. Say it plainly.
- **No invented statistics.** Engagement figures, audience sizes and demographics come
  from something the client can see, or they don't go in.

## 6. How it gets used downstream

- **Whoever drafts the content** reads it before writing, so a draft is pitched at the
  right sophistication, opens on a live identity, and avoids the anti-triggers.
- **Angle generation** reads it too, and uses the anti-triggers and the saturation read
  as rejection criteria — an angle the audience is already
  drowning in fails on novelty however well made it is.
- **Phase 1 of this skill** uses it to make the funnel × segment × medium map real: the
  "when and where they read" section is what turns a medium choice from a preference into
  a decision.
- **It does not decide who to sell to.** That stays with `icp`. If capturing this profile
  surfaces something that changes the buying picture — a segment nobody had noticed, a
  buyer who is not the reader — hand that to `icp` rather than quietly rewriting the ICP
  from content evidence.
