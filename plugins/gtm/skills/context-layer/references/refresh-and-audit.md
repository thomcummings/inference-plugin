# Refresh and audit

A store decays without upkeep. Refresh brings it up to date; audit checks it
against its own rules. Context is tended like a garden, not built once like a
building.

## Contents

- [Refresh](#refresh)
- [Freshness windows](#freshness-windows)
- [The feedback question](#the-feedback-question)
- [Audit checks](#audit-checks)
- [Tier, route and report](#tier-route-and-report)
- [What an audit proves](#what-an-audit-proves)

## Refresh

1. Read Start here, Conventions and Agent guidelines in this run. Take every
   threshold from Conventions as written, not from memory.
2. List rows past their freshness window (below), and rows with no Last
   reviewed date.
3. Re-check the sources used at setup for material created or changed since
   each row's Last reviewed date. Route it with `filling-context.md`.
4. Compare the new material with the store. List new contradictions in the
   standard shape, with severity.
5. **Growth check:** look for sections skipped or stubbed at setup that now
   matter. Signals: a new product, a new competitor showing up in deals, a team
   that has grown past the small layout, agents or scheduled jobs that have
   started running without a registry row.
6. Check registry rows at `trial` past their review date and routines with no
   recent run notes.
7. Ask the feedback question.
8. Propose every change: target row, proposed text, source, and who must
   approve. Write after approval. Changes to `canonical` rows are proposals to
   the owner (a comment, a pull request, or a suggestion), never edits.
9. Write a report at `memory/reports/YYYY-MM-DD-context-refresh` and changelog
   rows for anything written.

When refresh runs unattended on a schedule, it does steps 1 to 6 and writes the
report only. Nothing else changes until a person reviews it.

## Freshness windows

Defaults for Conventions; the team can change them there.

| Row type | Window | Why |
| --- | --- | --- |
| Competitors | 90 days; a canonical battlecard older than this drops to `working` | Competitors move fast |
| Market signals and active work | 90 days | Time-bound by nature |
| Operations rows (funnel, pricing, channels) | 90 days | Numbers and processes change quarterly |
| Team (people, roles, who decides) | 90 days | Hires, exits and role changes break routing and approvals first |
| Library, personas, objections, glossary, standards | 180 days | Slow-moving |
| Foundations (brand, category, architecture) | 365 days | Changes rarely, and deliberately |
| Proof | 365 days, or Expires if sooner | Usage rights and stats expire |

## The feedback question

Ask: "What do you keep correcting in AI output?" Examples: an old product
name, the wrong tone for a channel, a claim legal won't allow, a persona that
doesn't exist any more.

For each recurring correction:

- Find the row that should have prevented it, or note that none exists.
- Propose the fix at `working`: a changed row, a new standards row (banned
  phrase, approved claim, good or bad example), or a glossary term.
- Record it in Learnings under a theme such as `ai-output-corrections`, with
  the evidence.

This is how the store gets better from use. Nothing about it is automated: a
person names the correction and the owner approves the fix.

## Audit checks

Read-only. List every section in scope and record row counts. A section that
can't be read goes in Coverage and is never reported as healthy.

**01 Context**
- Past the freshness window, or no Last reviewed date.
- Status `stub`.
- No owner on the row and no accountable person for its section.
- Slug missing, malformed or duplicated.
- Two rows for one single document.
- Canonical competitors older than 90 days; proof stats past Expires but still canonical.
- Agent-authored rows waiting in Needs review for more than 7 days.
- Required headings missing or out of order (rows created or changed in the last 30 days).
- Numbers, quotes or customer names with no source.

**02 Memory**
- Decisions at `proposed` for more than 14 days.
- Reports at `draft` more than 7 days after their period end.
- `failed` or `blocked` run notes in the period.
- Undated titles, or slugs that don't match the pattern.

**03 Agent Ops (light)**
- Registry rows with no owner.
- Rows at `trial` past their review date, or with no review date.
- Routines with no run note for their last scheduled cycle.
- Routines running on a personal laptop (record, don't judge: they write no
  run notes, so a gap proves nothing).
- Things agents clearly use (mentioned in run notes, pointers or instructions)
  with no registry row.
- Agents or skills whose instructions hold a copy of store content (rules,
  claims, vocabulary) instead of reading the rows at run time. Each copy
  drifts the day the row changes. Propose the change to the row owner and
  hand it to `skill-design` or `agent-design`.
- Backlog items `in design` for more than 30 days.

**04 Manual**
- Sections in Ownership with no accountable person.
- The same rule stated differently on two pages.
- Vocabulary values in use that aren't on the list.

For a git/markdown store, `scripts/check_store.py` runs the frontmatter,
duplicate-slug and staleness checks. Run it first and read its findings into
the tiers below.

## Tier, route and report

Group: when one check hits more than five rows in one section for one owner,
report one line with the count.

Tiers:
1. Could make an agent cite wrong or unsafe material (stale canonical rows,
   unsourced claims, duplicate single documents, expired proof).
2. Work waiting on a person (drafts, proposals, ratifications).
3. Agent Ops gaps.
4. Cosmetic.

Route each finding to the row owner, else the section's accountable person,
else the store owner. Compare with the previous audit: mark each finding new or
open since a date, and list what has been resolved.

Report as `memory/reports/YYYY-MM-DD-context-audit`:

```
# YYYY-MM-DD context audit
Headline: [n] tier 1 · [n] tier 2 · [n] tier 3 · [n] tier 4 · coverage complete | partial
## Findings
| Tier | Check | Row | Evidence (failing value and rule) | Route to | New or open since |
## Grouped findings
## Resolved since last audit
## Coverage
```

## What an audit proves

It proves which rows break the written rules on the audit date. It does not
prove content is true or current: a wrong row with a fresh date passes. It
does not prove a routine is running. A missing run note is a question for the
routine's owner, not proof of a failure.
