# Scope + tooling checklist (Phase 2)

## Scope decisions to confirm with the user

Ask these before spending research effort. Each materially changes the work.

1. **Competitor set.** Which competitors are in scope? Distinguish:
   - *Direct* — same job, same buyer.
   - *Adjacent / emerging* — overlapping job or a new entrant worth watching.
   Default to the user's pinned list if one exists; offer to add obvious emerging
   players, but don't pad the set — depth beats breadth.

2. **Output structure.**
   - *Per-competitor files + synthesis* (default) — most modular and reusable.
   - *Single combined doc* — easier to read end-to-end for a small set.

3. **Depth.**
   - *Fresh deep re-scan* — re-gather everything, even if prior notes exist.
   - *Incremental deepening* — build on prior work, focus new effort on gaps.

4. **First run vs refresh.** If a prior scan exists, decide whether this is a
   refresh (Phases 1–5 fresh + a "what changed" delta) or a clean first run.

5. **Audience for the deliverable.** Internal-only, or heading to a client?
   Determines whether Phase 6 (client-ready register) is needed.

If the deliverable format or competitor scope is genuinely ambiguous, ask. If a
prior scan or pinned list answers it, don't re-ask — just confirm your read.

## Tooling guidance

The single most important practical lesson: **plain HTML web-fetch is frequently
blocked, rate-limited, or returns an empty JS shell on competitor marketing
sites.** Don't fight it — reach for the right tool per job.

| Job | Preferred tool | Notes |
|---|---|---|
| Homepage / pricing / product page content (verbatim) | A renderer that returns clean page text (e.g. Exa search/fetch) | Renders JS; gets the real copy. This is the workhorse for Dimension 1. |
| Finding pages, reviews, press, rankings | Web search | The workhorse for Dimension 3 (earned visibility). Try multiple query angles. |
| Live social follower counts, live review counts | A JS-rendering browser (e.g. Claude-in-Chrome) | Optional. Desk tools often can't pull these reliably; flag as a gap if unavailable. |
| Competitor "vs [subject]" pages | Renderer + search | Search "[subject] vs", "[subject] alternative"; fetch and read verbatim. |

Before starting Phase 3, confirm you have at least a capable page renderer and web
search. If you don't, say so — a scan built on blocked fetches will be thin, and
it's better to flag that upfront than to ship hedged guesses.

Note recency: competitor pages, pricing, and counts change. Date-stamp the scan and
note "as of [month/year]" on time-sensitive figures.

## Subagent vs inline

If subagents are available, fan out one per competitor (Phase 3) — it keeps each
competitor's raw research out of the main context and runs concurrently. If not,
work through competitors one at a time inline, using the same brief and discipline.
