# Filling context

How to get a team's existing material into the store without turning old
assumptions into the new truth. The job is curation, not accumulation: fewer,
better rows beat a mirror of every file. Bad context is worse than none,
because it gives agents confidence in the wrong things.

## Contents

- [Source trust order](#source-trust-order)
- [Gather](#gather)
- [Classify and route](#classify-and-route)
- [Interview for gaps](#interview-for-gaps)
- [Contradictions](#contradictions)
- [Write the rows](#write-the-rows)

## Source trust order

Weight sources in this order when they disagree:

1. Material the person hands over or confirms in this conversation.
2. Owned, structured documents in the knowledge base (Notion, Drive, a repo).
3. Decks and slides: often aspirational; treat audience and positioning claims
   in them as hypotheses.
4. Meeting notes and transcripts: good for customer language and decisions
   made out loud.
5. Chat (Slack, Teams): signal only. Use pinned messages, channel descriptions
   and leadership posts for language and recent news. Never copy threads.

The CRM, analytics and task tools are systems of record. Link to them; take
definitions from them into the glossary; never copy their records in.

## Gather

Work through each source the person can reach, focusing on the priority rows
from triage.

**Existing stores first.** Before reading content, look for anything that
already claims to be the source of truth: a CONTEXT.md, an older hub or wiki,
a messaging hub, an MCP server's context folder, or a condensed copy inside a
skill or agent prompt. List each with its date and what it covers. Propose
one store to keep and, for each of the others, archive, repoint to the new
store, or leave out of scope. Two live stores is worse than one stale one, and
agents reading the older one will quote dead positioning. Weigh the newest
owned store highest when they disagree, and record what it supersedes.

Then, for each source:

- **Files or a folder:** list every file with a one-line summary and a
  proposed destination. Confirm before going further.
- **Notion or Drive:** ask for a root page or folder rather than searching the
  whole workspace. Search for the terms each priority row needs (positioning,
  messaging, ICP, persona, competitor, battlecard, brand, voice, case study,
  pricing, funnel). List what was found and confirm what to include.
- **Chat:** extract the signal, not the text.

Connector searches have limits. If a workspace is too large to cover, say what
was searched and what was not, and fall back to the interview.

## Classify and route

Classify each fragment, then route it to a row. Do not write yet.

| Class | Signals | Routes to |
| --- | --- | --- |
| company | "about us", what we do, mission, model, funding, stage | `core/story/company-overview` |
| positioning | alternatives, differentiators, category, "unlike X" | `core/story/positioning-canvas` |
| product | product names, features, how it works, use cases, integrations | `core/messaging/product-houses/[product]` |
| audience | ICP, target customer, segment, buyer, JTBD | `core/audience/primary-icp`, `core/audience/personas/[role]` |
| messaging | value prop, pitch, tagline, pillars | `core/messaging/company-house` |
| voice | tone of voice, style guide, do and don't | `core/messaging/voice-content` |
| competitive | competitor names, "vs", alternatives, landscape, battlecard | `core/competitive/landscape-map`, `core/competitive/battlecards/[competitor]` |
| objection | "they always ask", pushback, concerns | `core/competitive/objections/[objection]` |
| proof | case study, testimonial, result, ROI, customer + metric | `core/proof/[type]/[name]` |
| operations | funnel, stages, channels, pricing, KPIs, process | `core/operations/[name]`, glossary terms |
| definition | a term with a calculation or threshold | `core/glossary/[term]` |
| standard | review checklists, examples marked good or bad, approved wording, banned words | `core/standards/[kind]/[name]` |
| decision | "we decided", "going forward", "we're not doing" | `memory/decisions/YYYY-MM-DD-[name]` at `proposed` |
| campaign or project | launch, campaign, Q1–Q4 initiative, experiment | Active work, if the team uses it; otherwise skip |
| market signal | trend, news, report, market size | A learning or the competitive landscape's Updates, dated |
| team | names and roles, org chart, who decides | `core/team/[name]` |
| engagement admin | a consultant's or agency's rates, cadence, invoices, scope, their own notes | Not in the store: it is not the company's context. Leave it where it is |
| other | none of the above | Ask the person; never discard silently |

Track where every fragment came from. The row's Source field and an inline
citation for any number or quote come from this list.

## Interview for gaps

For each priority row with no usable source, ask three to five questions, then
route the answers the same way. Seeds:

- **Personas:** Describe the customer you wish you had a hundred of. Their
  role? The problem? What did they try before you?
- **Positioning:** What would customers use if you didn't exist? What can you
  do that those alternatives can't?
- **Competitive:** When you lose, who to? When you win, what do buyers say
  decided it?
- **Messaging:** Ten seconds with your ideal customer: what do you say?
- **Proof:** Your best customer result, the one you'd put on a billboard? Are
  you allowed to say it publicly?
- **Standards:** What do you keep correcting in AI output? Show one piece you
  were proud of and one you'd never publish.

An interview answer is the person's view on that date. Record it as the
source (`interview, YYYY-MM-DD, [name]`) and keep the row at `working`.

## Contradictions

Before writing, compare everything routed to the same row, and rows that must
agree with each other (ICP and personas, positioning and messaging, proof and
claims).

| Type | Look for | Severity |
| --- | --- | --- |
| Audience contradiction | Different documents targeting different segments | Blocking |
| Positioning conflict | Contradictory value props, categories or differentiators | Blocking |
| Stage or model mismatch | Content implying different stages, prices or business models | High |
| Proof conflict | Stats or claims that disagree, or a claim with no proof | High |
| Persona overlap | Two descriptions of the same person that differ | Medium |
| Voice inconsistency | Formal and casual registers side by side | Low |
| Stale signal | Specific market or competitor claims older than six months | Low |

- **Blocking:** settle with the owner before writing that row.
- **High:** recommend settling; proceed only with an explicit warning in the
  row and the report.
- **Medium and low:** list in the report and proceed.

Write each one in this shape, so the owner can answer in a word:

```
### [Short label]
Severity: blocking | high | medium | low
Found in: [source A] vs [source B]
The conflict: [one sentence]

A) [a concrete resolution]
B) [a different concrete resolution]
C) Your own answer
```

A settled contradiction is a decision. Record it in Decisions at `proposed`
with the owner as decider, so it is not reopened next quarter.

## Write the rows

- Synthesise; do not paste. Each row opens with its TL;DR, uses its required
  headings, and reads on its own without "see the other doc".
- Every row lands at `working` (or `stub` if there is nothing yet), with
  slug, owner, author, last reviewed and source filled.
- Write in priority order, so if the work stops partway the most useful rows
  exist.
- Keep each row under about 2,000 tokens. Split long material into a single
  document plus collection rows.
- Mark anything uncertain inline as "Not yet known" rather than smoothing it
  over.
