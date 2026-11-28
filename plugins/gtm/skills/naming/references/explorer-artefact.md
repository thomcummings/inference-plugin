# Name-space explorer — artefact build spec

Reference for step 4 of the `naming` workflow. This is **opt-in**: stay in chat for small
rounds, offer the explorer once a round gets big enough to need visual sorting (~20+
candidates, or when the client is losing track of favourites).

Built with `create_artifact` so it persists, re-opens, and pulls live data on each open. It's
the visual home for exploration — what makes naming feel like a tool, not a chat transcript.

## Before you wire it: the confirmed tool shape

Probed live (2026-07-08). The domain checker is the Vercel MCP tool
`check_domain_availability_and_price`.

**Input:** a `names` array (batch the whole shortlist in one call).

```json
{ "names": ["lumenstack.com", "lumenstack.ai", "google.com"] }
```

**Output:**

```json
{
  "message": "Checked 3 domains: 1 available, 2 unavailable or failed. Total cost ...",
  "results": [
    {
      "name": "lumenstack.com",
      "available": true,
      "price": 11.25,
      "period": 1,
      "priceError": null,
      "message": "Domain lumenstack.com is available for $11.25 USD for 1 year",
      "purchaseUrl": "https://vercel.com/domains/search?q=lumenstack.com"
    },
    {
      "name": "google.com",
      "available": false,
      "price": null,
      "period": null,
      "priceError": null,
      "message": "Domain google.com is not available for purchase"
    }
  ],
  "summary": { "total": 3, "available": 1, "unavailable": 2, "totalPrice": 11.25 }
}
```

Notes that matter for the parser:
- Read each card's status from `results[i].available` (boolean) and price from
  `results[i].price` (number or `null`).
- **No premium / EAP flag.** Unlike registrar APIs, this returns a plain available/price. Don't
  invent a premium chip.
- `purchaseUrl` is handy to hang off the domain chip as a "buy" link.
- Inside the artefact, `callMcpTool` wraps the payload: read
  `const r = res.structuredContent ?? JSON.parse(res.content[0].text)` then `r.results`.

## Wiring inside the page

- List `check_domain_availability_and_price` in the artefact's `mcp_tools` so
  `window.cowork.callMcpTool` can reach it.
- Call it **on demand** from a per-card (or shortlist-wide) "check availability" button, not on
  page load for every card — same rate-limit / noise discipline as the chat flow. For each card,
  build the domain candidate list the way the skill's domain strategy does — exact `.com`, then
  the TLD sweep (`.io/.ai/.so/.co/.app/.dev`), then modifiers (`get-/try-/use-/meet-[name].com`,
  `[name]hq/app.com`) — and batch the whole shortlist's candidates into one `names` array.
- On the domain chip, surface the **best available option per name** and which rung it came from
  (exact `.com` = clean win; a modifier or niche TLD = compromise), so the board shows quality of
  availability, not just a binary.
- Optional: `window.cowork.askClaude(prompt, data)` for a quick "why does this one work" blurb
  per card without leaving the page.

## Layout

A board of candidate cards. Each card:

- the **name**
- **territory tag** (descriptive / evocative / coined / metaphor / compound / lexical / …)
- one-line **rationale**
- **rubric mini-scores** (distinctiveness, say-ability, spell-ability, meaning-fit …)
- **availability chips** — domain / handle / TM — greyed until checked, then filled with
  status + price (domain) or signal (handle/TM, with the not-a-verdict caveat visible)

## Interactions

- **Rate** — star / thumbs per card; persist to `localStorage` so ratings survive reload and
  app restarts.
- **Cluster** — group cards by territory, by rating, or by a naming theme (e.g. all the
  light/optics metaphors together).
- **Sort / rank** — by any rubric dimension or overall score.
- **Filter** — hide rejected; show only available-`.com`; show a single territory.
- **Live domain check on demand** — the button described above; fills the domain chip with
  status + price and a `purchaseUrl` link.
- **Shortlist tray** — star/drag favourites into a tray that becomes the deliverable seed.

## Build notes

- Persist ratings, filter, and sort choices to `localStorage` — they should survive reload.
- Don't build your own reload button; the artefact header already has one.
- CDN allowed for Chart.js if a positioning scatter is wanted (e.g. distinctiveness ×
  availability). Grid.js / Mermaid also allowed. Anything else must be inline.
- Keep the trademark chip honest: label it "signal, not clearance" in the UI, matching the
  deliverable caveat.
