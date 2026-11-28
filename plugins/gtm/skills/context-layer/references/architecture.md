# Architecture

The standard tree, what each part holds, the small and full layouts, and how to
adapt them. Names in square brackets are the team's own.

## Contents

- [The tree](#the-tree)
- [Section contracts](#section-contracts)
- [Single documents vs collections](#single-documents-vs-collections)
- [Small and full layouts](#small-and-full-layouts)
- [Optional areas](#optional-areas)
- [Adapting the tree](#adapting-the-tree)
- [Placement and access](#placement-and-access)

## The tree

```
[Company] GTM context
├── 00 Start here         The map: sections, common questions → where, how to read a row
│
├── 01 Context            What we know and agree            [owners write; agents propose]
│   ├── Library           One row per single document (positioning canvas, primary ICP, voice, messaging house…)
│   ├── Personas          Collection
│   ├── Competitors       Collection (battlecards)
│   ├── Objections        Collection
│   ├── Proof             Collection (case studies, testimonials, stats, demos) with usage rights
│   ├── Glossary          Collection (business terms: MQL, activated account…)
│   └── Standards         Collection (rubrics, good and bad examples, approved claims, banned phrases)
│
├── 02 Memory             What happened and why             [agents draft; people ratify; append-only]
│   ├── Decisions         One row per decision, YYYY-MM-DD short-name
│   ├── Learnings         One row per theme, evolves with evidence
│   ├── Reports           Weekly-or-less write-ups, YYYY-MM-DD report-type
│   └── Runs              One short note per scheduled run, including no-change
│
├── 03 Agent Ops (light)  What exists and who owns it
│   ├── Registry          Agents, skills and routines: owner, status, review date, where it runs, rows it reads
│   └── Backlog           Ideas waiting for a design decision
│
└── 04 Manual             How the store works               [store owner]
    ├── Conventions       Sections, status and stage, slugs, names, dates, freshness, headings, writing rules
    ├── Agent guidelines  May do alone / ask first / never
    ├── Vocabulary        Controlled lists (adding a value is a human decision)
    ├── Ownership         One accountable person per section
    └── Changelog         Every material and structural change, newest first

Linked systems (data stays outside the store)
├── [CRM]                 Accounts and deals
├── [Task tool]           Tasks and follow-ups
└── [Analytics]           Product and web usage
```

Keep the numbers. "00–04" orders the sidebar or folder list and gives agents a
stable map. In a git/markdown store the folders are `00-start-here/`,
`01-context/`, `02-memory/`, `03-agent-ops/`, `04-manual/`.

## Section contracts

| Section | Question it answers | Changes | Written by | Agent rights |
| --- | --- | --- | --- | --- |
| 01 Context | What do we know and agree? | Slowly | Section owners | Add rows at `working`; comment on `canonical` rows; never edit canonical bodies |
| 02 Memory | What happened? | Append-only | Agents draft, people ratify | Decisions at `proposed`, reports at `draft`, run notes freely |
| 03 Agent Ops | What exists? | When agents, skills or routines change | Row owners, through the design skills | Propose only |
| 04 Manual | How does the store work? | Rarely | Store owner | None, apart from changelog rows for their own material changes |

Marking 01 as "no agent content" in its landing page signals that agent drafts
belong in a report or at `working` until an owner files them. This is what
stops the context layer getting sloppy.

Every section landing page uses the same four headings: What this section
holds; How to use it; Who writes here; What does not belong here.

## Single documents vs collections

- A **single document** is something there is exactly one of. Each is one row
  in the Library. Never create a second row for one: revise it, or archive it
  and replace it with a new slug.
- A **collection** is many of a kind. Each gets its own collection.
- A new collection needs repeated items with shared fields that someone
  filters by. If not, it is a page, a property or a section in an existing
  body. Teams often want a collection per initiative; that is usually a
  mistake.

Library sections: `story`, `audience`, `messaging`, `competitive`,
`foundations`, `operations`, `team`.

Typical priority single documents:

- `core/story/company-overview`
- `core/story/positioning-canvas`
- `core/audience/primary-icp` (including target-account criteria)
- `core/messaging/company-house`
- `core/messaging/voice-content`
- `core/messaging/product-houses/[product]` (one per product, if needed)
- `core/competitive/landscape-map`
- `core/operations/funnel-stages`
- `core/operations/data-sources`

## Small and full layouts

Recommend at triage and say why.

| Signal | Layout |
| --- | --- |
| One product; few enough personas, competitors and proof items to embed in single documents; "I just want Claude to know the company" | Small |
| More than one product, or enough personas, competitors or proof items that someone needs to filter them | Full |

Decide by how much there is, not by headcount: a team of ten with one
product and six case studies still fits the small layout. Running agents
decide whether to add light Agent Ops, not which layout to use.

**Small layout**

- 00 Start here.
- 01 Context as the Library only. Personas, competitors, proof and glossary
  terms live as sections inside single documents (`core/audience/personas`,
  `core/competitive/landscape-map` with a battlecard section per competitor,
  `core/proof/proof-index`, `core/glossary/terms`) until there are enough of
  them to filter.
- 02 Memory: Decisions and Reports. Learnings and Runs when needed.
- 03 Agent Ops: left out until something runs on a schedule.
- 04 Manual: Conventions and Agent guidelines; vocabulary, ownership and
  changelog as sections of Conventions.

Minimum viable store: company overview, messaging house, voice, and one
persona. If time is short, build those and stub the rest.

**Full layout:** everything in the tree. Large teams or several product lines
add a Product field to every Context and Memory row type and per-product
messaging rows. Keep one store with filtered views rather than one per team.

**Growing small into full:** each embedded section becomes a collection row
with the same slug path plus a name (`core/audience/personas` → one row per
role under `core/audience/personas/[role]`). Archive the embedded version and
log the move in the changelog.

## Optional areas

Two optional areas sit inside 01 Context when a team needs them:

- **Active work:** projects and experiments in flight, each with an area tag,
  so an agent working on one function can filter to its work. Projects change
  weekly; they never rewrite core rows.
- **Function pointers:** one thin page per function (content, growth, paid…)
  that indexes the rows that function uses. Add one only when a function needs
  it.

## Adapting the tree

- **Rename freely, separate strictly.** "Knowledge / Log / Automation / Rules"
  works too, as long as the five separations in `concepts.md` hold.
- **No chat tool:** "chat" stands in for Slack or Teams throughout. The rule is
  the same: summary and link only.
- **Keep the numbers and the slugs** whatever the names become.

## Placement and access

- Put the store where the whole GTM team can see it. A store in a personal
  space never gets used.
- Give agents access to the store root only, not the whole workspace.
- Mark the root as work in progress, with named contacts, until the priority
  rows are canonical.
- Write in the team's house language, recorded in Conventions.
