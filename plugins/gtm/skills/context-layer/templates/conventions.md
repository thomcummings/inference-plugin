# Conventions

Slug: `infra/conventions`. How this store is organised and named. Written for
people; agents follow it too. Fill the `[placeholders]` with the team.

## The sections

| Section | Question it answers | Changes | Written by |
| --- | --- | --- | --- |
| 01 Context | What do we know and agree? | Slowly | Section owners; agents may draft |
| 02 Memory | What happened? | Append-only | Agents draft; people ratify |
| 03 Agent Ops | What agents, skills and routines exist? | When they change | The owner of each row |
| 04 Manual | How does the store work? | Rarely | Store owner: [name] |

Linked, never copied: [accounts and deals (CRM)], [tasks (task tool)],
[usage (analytics)].

## Single documents and collections

- A single document is something there is exactly one of, such as the
  positioning canvas. It is one row in the Library.
- A collection is many of a kind, such as personas or competitors.
- Never create a second row for a single document. Revise it, or archive it
  and create a replacement with a new slug.

## Status and stage

Status is trust: how far you can rely on a row.

| Status | Meaning | Who sets it |
| --- | --- | --- |
| `canonical` | Ratified. Safe to cite externally | Section owner only |
| `working` | Draft or hypothesis. Internal use; present it as current thinking | Anyone |
| `stub` | Empty scaffold. Don't cite | Anyone |
| `archived` | Superseded. Hidden from default views and agents | Section owner |

Stage is lifecycle, only where something moves through steps: Decisions
(`proposed`, `active`, `superseded`), Learnings (`active`, `superseded`,
`archived`), Reports (`draft`, `final`). Never mix the two.

## Slugs

Every Context and Memory row has a slug: a permanent, path-style ID used to
cite it. Titles and URLs change; slugs never do. Lowercase kebab-case.

| Where | Pattern |
| --- | --- |
| Library | `core/[section]/[name]` |
| Personas | `core/audience/personas/[role]` |
| Competitors | `core/competitive/battlecards/[competitor]` |
| Objections | `core/competitive/objections/[objection]` |
| Proof | `core/proof/[case-study\|testimonial\|stat\|demo]/[name]` |
| Glossary | `core/glossary/[term]` |
| Standards | `core/standards/[kind]/[name]` |
| Decisions | `memory/decisions/YYYY-MM-DD-[name]` |
| Learnings | `memory/learnings/[theme]` |
| Reports | `memory/reports/YYYY-MM-DD-[report-type]` |
| Run notes | `memory/runs/YYYY-MM-DD-HHmm-[name]` |
| Registry | `ops/registry/[name]` |
| Manual pages | `infra/[page]` |

Registry names are the kebab-case name things load. Never rename one casually.

## Names and dates

- Dated items are titled `YYYY-MM-DD short-name` and never renamed. Supersede
  rather than edit.
- A report's date is the last day it covers.
- Dates are absolute and ISO. Convert "last week" to a date before saving.

## Freshness

Last reviewed is the one freshness date. Bump it only on a material refresh,
not a typo fix.

| Row type | Window |
| --- | --- |
| Competitors | 90 days; a canonical battlecard older than this drops to `working` |
| Market signals, active work, operations | 90 days |
| Library, personas, objections, glossary, standards | 180 days |
| Foundations | 365 days |
| Proof | 365 days, or Expires if sooner |

## Required headings

Each row type has fixed body headings. Fill sections; don't invent new ones.

| Row type | Body headings |
| --- | --- |
| [Each row type this store uses, with its headings, filled at setup] | |

 If a section has nothing yet,
keep the heading and write "Not yet known." Every Library row opens with a
short TL;DR and stays under about 2,000 tokens.

## House writing rules

These apply to every page, whoever wrote it.

- [House language, for example UK English].
- Plain, specific and short. Front-load the point.
- [Punctuation and style rules.]
- Links as `[label](url)`, never bare.
- Canonical documents are written in the third person ("[Company] does").
- Never invent numbers, quotes, customers or competitor facts. Write "Not yet
  known".

Overrides to these rules live in `core/messaging/voice-content` and nowhere
else.
