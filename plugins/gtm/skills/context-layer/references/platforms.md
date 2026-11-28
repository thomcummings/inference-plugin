# Platforms

The pattern depends on five capabilities, not on any one tool. Map them onto
whatever the team already uses.

## Contents

- [Which platform](#which-platform)
- [The capability map](#the-capability-map)
- [Notion](#notion)
- [Git or markdown](#git-or-markdown)
- [Google Drive](#google-drive)
- [Moving between platforms](#moving-between-platforms)
- [Retrieval and indexes](#retrieval-and-indexes)

## Which platform

Ask first. Use the knowledge base the team already works in; a store in a tool
nobody opens is dead on arrival.

When there is no knowledge base, recommend one, with the reason:

| Situation | Recommend | Why |
| --- | --- | --- |
| The team already uses Claude Code, Cowork or a code repo, or wants full history and portability | Git/markdown (a GitHub repo) | Plain files every agent reads; a pull request is the propose-then-approve step |
| A non-technical team with no tool, or one already paying for Notion | Notion | Typed rows, filtered views and a freshness formula with no setup; agents reach it through the Notion connector |
| The company lives in Google Workspace and won't adopt another tool | Google Drive | Familiar; weakest at typed rows, so say so at the start |

State the trade-off in one line. Agents read all three through connectors or
files; the choice is about what people will maintain.

## The capability map

| Capability | Notion | Git/markdown | Google Drive |
| --- | --- | --- | --- |
| Typed rows with select options | Databases | YAML frontmatter, checked by `scripts/check_store.py` | One Sheet as the index, a tab per row type; a header table at the top of each Doc |
| Links between rows | Relation properties | Slugs in frontmatter | Slugs in the Sheet and the Doc header |
| Saved filtered views | Database views | Index pages written by the skill, or the check script's output | Filter views on the Sheet tabs |
| Computed freshness | Formula | The check script, run by hand or in CI | A Stale column formula in the Sheet |
| Propose, then approve | Rows at `working`; comments on canonical rows | Pull requests | Suggestion mode on canonical Docs; new Docs in a `_proposed` folder |

Whatever the platform:

- Slugs are the citation key everywhere.
- The five separations in `concepts.md` hold, even if section names change.
- If the platform can't hold a "proposed" state, use a review folder or label.

## Notion

- One teamspace page per section (00–04). Collections are databases; single
  documents are rows in the Library database.
- Properties exactly as in `row-types.md`. Select options as listed; adding an
  option is a vocabulary change.
- Stale formula, adjusting the window per database:
  ```
  if(empty(prop("Last reviewed")), true, dateBetween(now(), prop("Last reviewed"), "days") > 180)
  ```
  For proof stats, also return true when `Expires` has passed.
- Build the review views from `row-types.md` on every database with owners.
- Share the agents' integration with the store root page only.
- Permissions can't enforce most rules, so they are conventions plus review
  views that owners check.

## Git or markdown

Folders follow the sections. Each row is one file; its slug maps to its path:

| Slug prefix | Folder |
| --- | --- |
| `infra/start-here` | `00-start-here/start-here.md` |
| `core/` | `01-context/` |
| `memory/` | `02-memory/` |
| `ops/` | `03-agent-ops/` |
| `infra/` | `04-manual/` |

So `core/story/positioning-canvas` lives at
`01-context/story/positioning-canvas.md`, and
`memory/decisions/2026-11-27-drop-smb` at
`02-memory/decisions/2026-11-27-drop-smb.md`.

Frontmatter on every Context row:

```yaml
---
slug: core/story/positioning-canvas
status: working            # canonical | working | stub | archived
owner: "[NEEDS DECISION]"
author: ai-agent:context-layer
last_reviewed: 2026-11-27
source: "Series A deck (2026-03); interview with the founder, 2026-11-27"
function: [pmm]
---
```

Memory rows replace `status` with `stage` and add their own dated fields
(`date`, `decider`, `period_start`, `period_end`). Registry rows use `name`,
`kind`, `status`, `owner`, `review_date`, `where_it_runs`, `reads`, `writes`.
Run notes carry `slug` and `result`. Start here and Manual pages carry `slug`
only.

- Write each section's landing page as its folder's `README.md`.
- The skill writes on a branch and opens a pull request; the owner merges.
  Promotion to `canonical` is a one-line frontmatter change in a pull request
  the owner approves.
- Run `python3 scripts/check_store.py [store-root]` for the frontmatter,
  duplicate-slug and staleness checks. A team can run the same command in CI
  on every pull request.
- Never add a script that overwrites store files from somewhere else. Two
  sources of truth drift.

## Google Drive

- One folder per section (00–04), with subfolders per Library section and
  collection.
- One Doc per row. The first thing in each Doc is a two-column header table:
  Slug, Status (or Stage), Owner, Author, Last reviewed, Source.
- One Sheet, `store-index`, with a tab per row type mirroring the header
  fields plus a link to the Doc. The Sheet is what agents and people filter.
  Add a Stale column:
  ```
  =IF(ISBLANK(F2), TRUE, TODAY()-F2 > 180)
  ```
  where F is Last reviewed; adjust the window per tab.
- Keep the Doc header and the Sheet row in step: the skill updates both in the
  same change, and the audit flags any mismatch.
- Proposals: suggestion mode on canonical Docs; new rows go in a `_proposed`
  folder until the owner moves them.
- Drive has no real typed rows or relations. Say so at setup, and keep the
  Sheet as the single index.

## Moving between platforms

1. Inventory every row on the old platform with slug, status or stage, owner
   and dates.
2. Map each row type with the capability map above.
3. Build the new store's Manual first, then rows in priority order.
4. Write a coverage table: every old row lands somewhere, or is listed as
   dropped with a reason.
5. Keep the old store read-only until the owner approves the new one, then
   archive it and update the pointer. Two live stores is worse than one stale
   one.

## Retrieval and indexes

The store is the source of truth. A vector index, a knowledge graph, a search
service or an AI product's built-in memory is a way to find rows, never a
place to keep them.

- **Indexes are derived.** Build them from the store, rebuild them at will,
  and never write into one directly. Nothing in the store is ever restored
  from an index.
- **The design already suits indexing.** Short rows that open with a TL;DR
  make good chunks; frontmatter gives the metadata filters (status, owner,
  last reviewed, function); slugs are stable IDs that survive a re-index; slug
  links between rows already form a graph.
- **Filter before you rank.** An index must respect status: `canonical` and
  `working` rows only, with status and last reviewed returned alongside each
  hit so agents can still cite properly.
- **Reach the store through the pointer**, or an MCP server that serves rows
  by slug, rather than through file paths. The backend can then change
  without changing the agents.
- **Add an index only when Start here stops working**: when agents regularly
  miss the right rows because there are too many to route by hand. Most GTM
  stores never get there.
- For git/markdown stores, `python3 scripts/check_store.py STORE --export
  rows.jsonl` writes one JSON line per row (slug, path, frontmatter, body)
  for any index to build from.
