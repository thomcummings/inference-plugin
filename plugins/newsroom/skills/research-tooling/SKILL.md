---
name: research-tooling
description: |
  Implementation reference for the three research tools used across the newsroom plugin: Claude native
  web_search/web_fetch, Perplexity Sonar API, and Firecrawl. Covers when to use each tool, call
  patterns, failure handling, and cost awareness. Used by the newsroom-researcher and
  newsroom-fact-checker agents to decide which tool fits each research task. Trigger this skill
  whenever web research is being conducted within the newsroom pipeline and a decision is needed about
  which tool is best suited to the job.
---

# Research tooling

Shared reference for the Researcher and Fact-checker roles. Covers the three research tools the newsroom uses, when to use each, how to call them, and how to handle failures.

## The three tools

| Tool | Stance | Best for | Requires |
|------|--------|----------|----------|
| `web_search` / `web_fetch` | Native | Agentic multi-step research, straightforward source reading | Nothing — always available |
| Perplexity Sonar | Synthesis | Fast cited synthesis across many sources on one question | `PERPLEXITY_API_KEY` |
| Firecrawl | Extraction | Deep reads of JS-heavy, paywalled, or complex sources | `FIRECRAWL_API_KEY` |

## Tool selection principles

Three questions to ask before choosing a tool:

1. **What am I trying to produce?** A broad landscape view? A specific fact? The contents of one specific page?
2. **Do I know the target source already?** If yes, fetch it. If no, search first.
3. **Is the source cooperative?** If it's a public blog with clean HTML, `web_fetch` is fine. If it's a JS-heavy site, behind a paywall the user has access to, or has a complex layout that defeats regular extraction, Firecrawl is worth reaching for.

Default to `web_search` / `web_fetch`. Reach for Perplexity when synthesis is the job and you'd otherwise need to run 5+ searches and compile manually. Reach for Firecrawl only when regular fetch falls short.

## Claude native web_search and web_fetch

Always available, the primary tools for most research work.

### When to use
- Finding candidate sources for a topic you're learning
- Following threads ("this article mentioned X — let's look at X")
- Looking up specific facts where you don't already know the source
- Reading straightforward articles, blog posts, press releases
- Most fact-checking (you have a specific claim, search for it, read the source)

### Query principles
- Keep queries short (1-6 words)
- Start broad, narrow if needed — don't try to encode the full question into a single query
- Each search should be meaningfully different from the last; don't run near-duplicates
- Avoid operators (`site:`, quotes, `-`) unless a specific search strictly needs one

### Common patterns

**Landscape query (Researcher)**: `<topic>` then `<topic> recent` then `<topic> <adjacent concept>`
- Example: `MQL SQL conversion`, `MQL SQL conversion benchmarks`, `B2B funnel handoff metrics`

**Verification query (Fact-checker)**: `<specific entity> <specific claim>`
- Example: `Stripe $6.5bn 2024 funding`, `HubSpot benchmark conversion rate 2024`

**Counter-argument query (Researcher)**: framing from the opposing view
- Example: if the brief argues MQL-to-SQL measures the wrong thing, search `MQL SQL conversion rate important` — find the strongest case for the orthodox view.

### After search → fetch
`web_search` returns snippets. For any source that might actually support a claim (or any source that's going in the dossier), `web_fetch` the full page. Snippet-only research produces dossiers with mis-contextualised quotes.

### Limits
- Cannot handle JS-heavy SPAs well
- Cannot access paywalled content even when the user has a subscription
- Can truncate very long pages
- No direct access to PDFs embedded in pages (sometimes works, often doesn't)

When you hit these limits, that's when Firecrawl earns its place.

## Perplexity Sonar API

Used when the job is fast cited synthesis across many sources. Not for finding specific facts — for getting "what's the current conversation on X" in one call instead of five searches plus synthesis.

### When to use
- Landscape sweeps at the start of research: "what are the dominant framings of X in 2025?"
- Consensus questions: "what do B2B marketing experts currently say about attribution?"
- Competitor mentions: "who's writing substantively on topic X lately?"
- Quick sanity checks on the broad state of a topic

### When NOT to use
- Specific fact verification (use web_search + fetch — you want to read the primary source yourself)
- Finding quotes (synthesis flattens wording — go to the original)
- Reading one specific known source (fetch it directly)
- Anything where source quality matters and you want to inspect the cited sources yourself

### Call pattern

```python
import os
import requests

api_key = os.environ.get("PERPLEXITY_API_KEY")
if not api_key:
    # Announce explicitly to the user, fall back to web_search
    print("Perplexity unavailable — no API key set. Falling back to web_search.")
    # ... use web_search instead
else:
    response = requests.post(
        "https://api.perplexity.ai/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "sonar",  # or "sonar-pro" for heavier queries
            "messages": [
                {"role": "user", "content": "<synthesis query>"}
            ],
            "return_citations": True
        },
        timeout=30
    )
    if response.status_code != 200:
        print(f"Perplexity call failed: {response.status_code}. Falling back to web_search.")
        # ... use web_search instead
    else:
        data = response.json()
        # data["choices"][0]["message"]["content"] — the synthesised answer
        # data["citations"] — list of source URLs
```

### Model selection
- `sonar` — faster, cheaper, good for most synthesis work
- `sonar-pro` — better for complex multi-source synthesis, worth it for landscape sweeps on dense topics

### Handling the response
Perplexity returns a synthesised answer plus a list of citations. Two important steps:

1. **Never use the synthesised answer verbatim.** It's a research signal, not text for the dossier. Read it, then decide which cited sources to fetch and read directly.
2. **Fetch the top 2-3 cited sources yourself.** Perplexity cites them; you verify them. The dossier's claims should trace to sources you've read, not sources Perplexity read for you.

### Failure handling
- **Missing API key**: announce explicitly, fall back to `web_search`. Example: "Perplexity unavailable — no `PERPLEXITY_API_KEY` set in environment. Falling back to Claude web_search for this landscape query."
- **API error (4xx/5xx)**: announce and fall back. Include the status code in the announcement.
- **Timeout**: announce and fall back. Perplexity occasionally hangs on complex queries; 30s is a reasonable timeout.
- **Empty/unusable response**: announce and fall back. Don't try to salvage a bad synthesis.

Never silently swallow Perplexity failures. The user should always know which tool produced which evidence.

## Firecrawl

Used when regular `web_fetch` can't get clean content out of a specific source. Not a search tool — a extraction tool for specific known URLs.

### When to use
- JS-heavy sites where `web_fetch` returns an empty shell or boilerplate
- Complex page layouts (comment threads, embedded apps, tab-based content) where `web_fetch` misses the main content
- Archive sites that serve different content to different clients
- Pages with lots of embedded media where regular fetch truncates
- Research papers, SEC filings, investor pages with specific layouts

### When NOT to use
- Straightforward articles and blog posts (`web_fetch` handles these fine — don't burn Firecrawl credits unnecessarily)
- Landscape searches (it's not a search tool — you need to know the URL)
- Content behind auth you don't have (Firecrawl doesn't magically bypass paywalls; it helps with rendering, not access)

### Call pattern

Firecrawl offers multiple endpoints — the most useful for newsroom work is `/v1/scrape` for single-page extraction.

```python
import os
import requests

api_key = os.environ.get("FIRECRAWL_API_KEY")
target_url = "https://example.com/article"

if not api_key:
    print(f"Firecrawl unavailable — no API key set. Attempting web_fetch for {target_url}; note that JS-rendered content may not be captured.")
    # ... use web_fetch instead
else:
    response = requests.post(
        "https://api.firecrawl.dev/v1/scrape",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "url": target_url,
            "formats": ["markdown"],  # cleanest format for downstream use
            "onlyMainContent": True   # strips nav, footer, sidebars
        },
        timeout=60  # Firecrawl can take a while on complex pages
    )
    if response.status_code != 200:
        print(f"Firecrawl call failed ({response.status_code}) for {target_url}. Falling back to web_fetch; some content may not render.")
        # ... use web_fetch instead
    else:
        data = response.json()
        # data["data"]["markdown"] — the extracted content
        # data["data"]["metadata"] — title, description, etc.
```

### Format selection
- `markdown` — cleanest for dossier inclusion
- `html` — when structure matters (e.g. tables in a research paper)
- `rawHtml` — rarely needed; raw HTML is noisy

Prefer `markdown` + `onlyMainContent: true` for most newsroom use.

### Failure handling
- **Missing API key**: announce, fall back to `web_fetch`. Flag that JS-rendered content may be missed.
- **API error**: announce with status code, fall back. Include the URL so the user knows what didn't render.
- **Timeout**: Firecrawl can take 30-60 seconds on complex pages — that's normal, not a failure. Only treat as failure at ~90s+.
- **Returns empty content**: announce and fall back. Rare but happens.

Same principle as Perplexity: never silent fallbacks. The user should know which tool produced which content.

## Tool combination patterns

Research rarely uses one tool in isolation. Common patterns:

**Landscape → deep read**: Perplexity for the landscape synthesis → identify top 3-5 cited sources → `web_fetch` (or Firecrawl for the tricky ones) to read them directly → dossier.

**Verify a specific claim (Fact-checker)**: `web_search` for the specific claim → identify the authoritative source → `web_fetch` (or Firecrawl) to read it → match claim against source.

**Read a known source that resists normal fetch**: `web_fetch` first (cheap) → if content is incomplete or JS-shelled, Firecrawl.

**Verify an attributed quote**: Search for the quote's exact wording if memorable, or for the speaker + topic → fetch the source where the quote appears → match verbatim.

## Announcing tool usage

Both Researcher and Fact-checker report tool usage in their outputs so the user knows what produced what.

In the dossier's "Research notes" section or the claims-check's "Verification notes" section, include a brief tools-used summary:

```
Tools used:
- Perplexity Sonar: 1 query for landscape synthesis
- web_search: 12 queries (7 evidence, 3 counter-arguments, 2 fact verifications)
- web_fetch: 18 article reads
- Firecrawl: 2 deep reads (SEC filing on Stripe funding, IEEE paper on attribution modelling)

Failures encountered:
- Firecrawl timed out on [URL] — used web_fetch, returned truncated content. The key figure was still captured; see claim #7.
- Perplexity returned a thin result on the contrarian-view query; supplemented with 3 targeted web_search queries instead.
```

This transparency is non-negotiable. It's what lets the user evaluate the research's reliability without having to reverse-engineer it.

## Configuration

Both APIs read their keys from environment variables:
- `PERPLEXITY_API_KEY`
- `FIRECRAWL_API_KEY`

If either is missing, the tool is unavailable and the roles fall back to Claude native capabilities with an announcement. Users who want these tools should set the keys in their shell environment before invoking the newsroom skill.

Getting API keys:
- Perplexity: https://www.perplexity.ai/settings/api
- Firecrawl: https://www.firecrawl.dev/app/api-keys

Both offer free tiers sufficient for moderate personal use; heavier pipelines may need paid tiers.

## A note on cost awareness

Perplexity and Firecrawl both cost money per call. The Researcher and Fact-checker should be cost-aware without being paranoid about it:

- Don't call Perplexity for questions a single `web_search` would answer
- Don't call Firecrawl for pages `web_fetch` handles fine
- Don't re-call either tool for content already in the dossier
- Batch related queries where possible

Research depth should scale with the piece. A 500-word LinkedIn post doesn't justify 20 Firecrawl deep reads. A 3000-word argumentative essay might. Match effort to output.
