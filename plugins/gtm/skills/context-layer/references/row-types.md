# Row types

Fields, slugs, required headings and review views for every row type. Field
names are a recommendation; keep them identical across row types, because
agents query by name. `platforms.md` maps each field type onto Notion, git
frontmatter and Drive.

Shorthand: `select(a|b)`, `multi(a|b)`, `link → type`, `person`, `date`,
`text`, `url`, `checkbox`.

## Contents

- [Shared fields](#shared-fields)
- [01 Context](#01-context)
- [02 Memory](#02-memory)
- [03 Agent Ops (light)](#03-agent-ops-light)
- [04 Manual](#04-manual)
- [Review views](#review-views)

## Shared fields

Every 01 Context row:

| Field | Type | Notes |
| --- | --- | --- |
| Name | text | |
| Slug | text | Permanent, path-style ID. Never changes |
| Status | select(canonical\|working\|stub\|archived) | Trust. Only the section owner sets `canonical` or `archived` |
| Owner | person | Or `[NEEDS DECISION]` |
| Author | text | A person, or `ai-agent:[agent-id]` |
| Last reviewed | date | Bump only on a material refresh |
| Source | text | Where the content came from: document, interview date, link |
| Function | multi | From Vocabulary |
| Product | multi | Optional; add once there is more than one product |

Every dated 02 Memory row carries Name, Slug, Author, Function and a Stage
select.

## 01 Context

### Library (single documents)

- Shared fields, plus Section select(story|audience|messaging|competitive|foundations|operations|team).
- Slug: `core/[section]/[name]`.
- Every body opens with a two- or three-sentence TL;DR: what this row is and
  when to use it. Keep a row under about 2,000 tokens; split it if it passes
  3,000. Agents load only what a task needs.
- Typical headings:
  - Company overview: What we do; Who for; Stage and model; Products; What we are not
  - Positioning canvas: Competitive alternatives; Unique attributes; Value; Best-fit customers; Market category; Relevant trends
  - Primary ICP: Firmographics; Technographics; Triggers; Disqualifiers; Target-account criteria and tiers; Buying committee
  - Messaging house: Positioning statement; Pillars; Proof per pillar; Product messages
  - Voice: Principles; Do and don't; Vocabulary; Examples; Overrides to house writing rules
- Freshness: 180 days.

### Personas

- Shared fields, plus Role (text), Seniority (select).
- Slug: `core/audience/personas/[role]`. Name by role, never by number.
- Body: Who they are; Jobs to be done; Pain; Trust triggers; Language they use; Objections; Messaging altitude.
- Freshness: 180 days.

### Competitors

- Shared fields, plus Tier select(primary|secondary|adjacent), Website (url).
- Slug: `core/competitive/battlecards/[competitor]`.
- Body: What they do; Who they target; Pricing; Funding and team; Where they win; Where they lose; Talk tracks; Objections they raise about us; Tracking signals; Updates (dated, newest first). Raw research goes in a child page or file `research-YYYY-MM-DD`.
- Freshness: 90 days. A canonical battlecard older than this drops to `working`.

### Objections

- Shared fields, plus Competitor (link → Competitors), Persona (link → Personas).
- Slug: `core/competitive/objections/[objection]`.
- Body: Objection in full; What is underneath; Best answer (2 to 4 sentences); Supporting proof; What does not work.
- Freshness: 180 days.

### Proof

- Shared fields, plus Type select(case-study|testimonial|stat|demo), Usage rights select(published|internal-only|pending-approval), Expires (date), Customer (text).
- Slug: `core/proof/[type]/[name]`.
- Body by type: case study (Summary; Before; Solution; Outcome; Quote; Related assets), testimonial (Quote; Context; Related assets), stat (Stat in full; Methodology; Caveats), demo (What it shows; How to use it; Caveats; Related assets).
- Freshness: 365 days, or Expires, whichever comes first.
- Required view: **Safe to use externally** = Usage rights `published` and Status `canonical`.

### Glossary

- Shared fields, plus Source system (text), Calculated in (text).
- Slug: `core/glossary/[term]`.
- Body: Definition; How it is calculated; Includes and excludes; Example; Related terms.
- Freshness: 180 days.

### Standards

What "good" looks like, so agents can check their own work and people stop
correcting the same thing.

- Shared fields, plus Kind select(rubric|example-good|example-bad|approved-claim|banned-phrase), Applies to (multi: channel or output type).
- Slug: `core/standards/[kind]/[name]`.
- Body by kind: rubric (What it judges; Criteria; How to score; Examples), good or bad example (The output; Why it works or fails; What to copy or avoid), approved claim (Claim exactly as approved; Proof row; Where it may be used; Expires), banned phrase (Phrase; Why; Use instead).
- Freshness: 180 days. Approved claims follow their proof row's expiry.

## 02 Memory

### Decisions

| Field | Type |
| --- | --- |
| Name | `YYYY-MM-DD short-name` |
| Slug | `memory/decisions/YYYY-MM-DD-[name]` |
| Date | date |
| Stage | select(proposed\|active\|superseded) |
| Decider | person |
| Author | text |
| Supersedes / Superseded by | link → Decisions |
| Revisit by | date |
| Function, Tags | multi |

Body: Decision; Context; Options considered; Rationale; Implications; Revisit trigger.
Never edit an active decision into a different one. Write a new row and link it with Supersedes.

### Learnings

| Field | Type |
| --- | --- |
| Name | the theme |
| Slug | `memory/learnings/[theme]` |
| Confidence | select(speculative\|growing\|strong\|settled) |
| Stage | select(active\|superseded\|archived) |
| First observed, Last reviewed | date |
| Owner, Author, Function | |

Body: Claim; Evidence; Confidence rationale; Implications; Counter-evidence; History.
One row per theme, not per date. `settled` needs three or more independent sources, and only a person sets it. Recurring corrections captured by refresh land here.

### Reports

| Field | Type |
| --- | --- |
| Name | `YYYY-MM-DD report-type` (date = last day covered) |
| Slug | `memory/reports/YYYY-MM-DD-[report-type]` |
| Report type | select (from Vocabulary) |
| Period start, Period end | date |
| Stage | select(draft\|final) |
| Produced by | text: routine, agent or person |
| Author, Function | |

Body: Period summary; What changed; Details; Decisions and actions; Open questions.
Weekly or less often. Never overwrite an earlier report. Setup, refresh and audit reports from this skill go here.

### Runs

One short note per execution of a scheduled routine or agent.

| Field | Type |
| --- | --- |
| Name | `YYYY-MM-DD HH:mm [routine-or-agent]` |
| Started | datetime |
| Routine or agent | link → Registry |
| Result | select(success\|partial\|failed\|blocked) |
| Output type | select(report\|digest\|alert\|data-update\|no-change) |
| Summary | text: the one or two lines chat gets |
| Output link | url |
| Notes | text: errors, blockers, what needs a person |

Body: the full output of the run. A no-change run still writes a note and posts nothing to chat. A blocked run records the reason and stops.

## 03 Agent Ops (light)

### Registry

One row per agent, skill or routine the team uses, whatever runs it. The
template is `templates/registry.md`.

| Field | Type | Notes |
| --- | --- | --- |
| Name | text | kebab-case, permanent: things load it by name |
| Kind | select(agent\|skill\|routine) | |
| What it does | text | One line, for a person |
| Owner | person | The accountable person, or `[NEEDS DECISION]` |
| Status | select(draft\|trial\|active\|degraded\|dormant\|retired) | New rows enter at `trial` |
| Review date | date | Required at `trial` |
| Where it runs | text | Surface and runtime, for example "Claude Cowork, a marketer's laptop" or "GitHub Actions, Mon 08:00 Europe/London" |
| Reads | text | Slugs, always starting `infra/start-here` |
| Writes | text | Where its output goes. Routines always include Runs |
| Instructions live in | text | One place: the skill file, the agent card or the row body |
| Uses | text | For routines: the one skill it runs. For agents: its skills |

A trial past its review date with no review becomes `dormant`. A routine on a
personal laptop is recorded honestly, because a laptop job writes no run notes
and its silence proves nothing.

### Backlog

| Field | Type |
| --- | --- |
| Idea | text |
| Likely kind | select(agent\|routine + skill\|skill\|local job\|not sure). A guess; the design decides |
| Stage | select(idea\|queued\|in design\|built\|rejected) |
| Owner | person |
| Notes | text |

## 04 Manual

- **Conventions, Agent guidelines, Vocabulary:** pages from `templates/`.
- **Ownership:** Section, Covers, Accountable, Responsible, Consulted, Informed. One row per section. The store owner is accountable for 04.
- **Changelog:** Title, Date, Kind select(content|structure|vocabulary|definitions), Affects (slugs or pages), Author. Run notes never go here.

## Review views

Every platform needs these, as saved views, generated index pages or filtered
Sheet tabs:

- **Needs review:** Status `working` and Author starts `ai-agent:`.
- **Needs ratification:** Decisions at `proposed`.
- **Drafts to review:** Reports at `draft`.
- **Stale first:** past the freshness window, oldest first. A row with no date counts as stale.
- **Trials due:** registry rows at `trial` past their review date.
- **Default:** hides `archived`. Agents read through it so archived rows stay out.
