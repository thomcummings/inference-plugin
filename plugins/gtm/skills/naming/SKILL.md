---
name: naming
description: >-
  Generate, pressure-test, and de-risk candidate names for a product, service, or
  sub-brand — with live availability checks and an opinionated house view, not 200
  interchangeable invented words. Trigger on "name this", "we need a name for X", "help me
  name our new product", "brainstorm names", "come up with names for", "what should we
  call this", "the name's not landing", "check if these names are available", "shortlist
  some names". Runs divergent (fast, high-volume brainstorm across naming territories)
  then convergent (a rated, checked, ranked shortlist with a recommendation). Checks
  domains live via the Vercel MCP; treats social handles, search collisions and trademark
  as signals, never verdicts — and says so. NOT the naming-structure decision of whether a
  thing needs its own name (that's brand-architecture), NOT taglines or signature lines
  (that's essence-craft), NOT the wordmark render (that's brand-asset-renderer), and NEVER
  legal trademark clearance (that's a lawyer).
---

# Naming

This skill does the one thing the rest of the brand stack can't: it generates the
**candidate names themselves**, pressure-tests them against a house view, and de-risks the
shortlist with live checks.

`brand-architecture` decides *whether* a thing needs its own name and where it sits in the
house. `positioning` and `brand-archetype` supply the category and the character. `icp` says
who has to say and spell it. This skill turns all of that into actual names. Then
`essence-craft` writes the tagline around the chosen one and `brand-asset-renderer` draws the
wordmark. Naming sits dead-centre.

It beats a vanilla LLM naming session in three specific ways, which are the whole point:

1. **It runs live availability checks.** Real domain lookups on the shortlist, not confident
   guesses about what's free. Most generic naming suggests names whose .com went years ago.
2. **It has a house view.** It generates across naming *territories* and scores against a
   rubric, so the client sees the space, not one aesthetic repeated forty times.
3. **It reads the client's actual brand context.** Names lean into (or deliberately break
   from) the real positioning, not a generic idea of the category.

## When to use

- Naming a new product, service, feature, sub-brand, or the company itself.
- Renaming something that isn't landing.
- Screening a list the client already has against availability and the rubric.
- Any "what should we call this?" where real options and real checks beat a quick riff.

## When NOT to use

- "Does this new thing even need its own name?" → `brand-architecture` (the branded-house vs
  house-of-brands call decides that; don't generate names for something that should be a
  descriptor).
- Tagline, signature phrase, or manifesto line for a name that already exists →
  `essence-craft`.
- Rendering the wordmark / asset set once a name is chosen → `brand-asset-renderer`.
- A legal trademark *verdict*. This skill surfaces collision signals; it never clears a name.
  That's a lawyer, every time.

## Inputs to read first (don't ask what you can look up)

Before asking the client anything, read the engagement's context store. Asking for what's
already on disk makes this a form, not an advisor.

- `evergreen/positioning.md` — category and competitive alternatives. Names should lean into
  the category or break from it *on purpose*; either way you need to know the set they'll be
  judged against.
- `evergreen/audience/personas.md` — who says, spells, remembers, and trusts the name. A name
  aimed at CFOs and one aimed at teenagers fail differently.
- `evergreen/messaging/voice-and-tone.md` — house lexicon and tone the name should sound like.
- `evergreen/competitive/landscape.md` — so you don't hand over a name one letter off a rival.
- `evergreen/company/product.md` — what the thing actually is and does.
- Any `brand-architecture` / `brand-archetype` output in the folder — the naming-structure
  constraint (distinct name? endorsed? descriptor?) and the character the name should carry.
- `memory/decisions/` — names already ruled in or out. Surface them; don't re-propose a killed
  name.

Cite `canonical` context as fact; treat `working` as hypothesis and say so. If the folder is
thin, run a tight intake (below) rather than guessing.

### Intake — only the gaps context didn't fill

Ask in one short batch, questions near the top, your lean flagged so the client reacts rather
than writes essays:

1. **What is it**, in one line — the thing being named.
2. **Who has to say it** — the buyer/user who'll speak, spell, and remember it.
3. **What must it sit beside** — sibling product/brand names, and the structure constraint
   from brand-architecture (distinct / endorsed / descriptor).
4. **What feeling** — the character in 2–3 words.
5. **Words to avoid** — competitor names, tired category words, anything with baggage.
6. **Boldness dial** — safe-and-clear ↔ provocative-and-ownable. Where on that line?
7. **The availability bar** (this one changes the whole job — see next): does this name need
   its own **social handles and .com**, or just to be a good name?

## The one branch that sets the whole job: does this name need a handle?

Decide this early, because it changes what "available" even means.

- **Handle-hungry names** — a **company, a standalone product, anything that will have its own
  website, social presence, or app-store listing.** These need real-world headroom: a
  registrable domain and clear-enough social handles. Availability is load-bearing.
- **Handle-light names** — a **feature, a tier, an internal capability, a module inside an
  existing product** (think *Smart Compose* inside Gmail, not a new company). These live under
  an existing brand's domain and handles. They need to be distinctive, sayable and non-
  colliding — but you should **not** kill a great feature name because `thatfeature.com` is
  taken. That's the wrong test for the job.

State which mode you're in at intake and carry it through: it decides whether the check
pipeline runs handle/domain checks at all, and whether availability is a hard gate or just a
tidiness note.

## The naming POV — the craft layer (this is the heart)

The part that makes these opinionated names and not a random generator. Drawn from established
naming craft — Alexandra Watkins' SMILE/SCRATCH, Lexicon-style sound-symbolism, Igor/Catchword
category theory — filtered through a house view.

### Naming territories — generate across all, don't collapse to one

A good round shows names from **at least 4–5** of these, so the client sees the *space*, not a
single aesthetic. Tag every name with its territory.

| Territory | What it is | Example shape |
|---|---|---|
| Descriptive | Says what it does | *General Motors, Salesforce* |
| Evocative / suggestive | Points at a benefit or feeling, obliquely | *Amazon, Sprint, Glossier* |
| Invented — real morphemes | Coined from real roots | *Verizon, Vercel, Trello* |
| Invented — abstract | Pure coinage, no meaning yet | *Kodak, Häagen-Dazs* |
| Metaphor / borrowed | A word from elsewhere, carrying its associations | *Oracle, Nike, Stripe* |
| Compound / portmanteau | Two ideas fused | *Netflix, Snapchat, Pinterest* |
| Founder / person / place | Named for someone or somewhere | *Warby Parker, Tesla* |
| Real-word / lexical | An existing word, repurposed | *Slack, Notion, Arc* |

### The scoring rubric — apply to each candidate

| Dimension | Question | Weight |
|---|---|---|
| Distinctiveness | Stands apart in the category, or sounds like the competitor set? | High |
| Say-ability | Survives being said down a phone, shouted across a room, left on a voicemail | High |
| Spell-ability | Can a stranger spell it after hearing it once? | High |
| Meaning fit | Carries the right association without being literal-descriptive-boring | High |
| Stretch | Room to grow past v1; not boxed into one feature or one geography | Med |
| Availability | Domain / handle / trademark headroom (see check pipeline) | Med → High\* |
| Depth | Rewards a second look — a story, a double meaning, a satisfying etymology | Med |
| Risk | Bad meanings in other languages, awkward abbreviations, existing baggage | Gate |

\* Availability is a **signal during divergence** and a **gate near decision** — and only a
hard gate for handle-hungry names. Don't let a taken .com kill a strong name early; there are
always routes (alt TLD, a modifier, or buying it later).

### The house view — the opinions

- **Distinctive beats descriptive.** Descriptive names are easy to approve and hard to own.
  Push toward evocative/coined unless the client has a real SEO/discovery reason to be literal.
- **Empty vessels are legitimate, but earn them.** An abstract coinage (*Kodak*) works only if
  the brand can afford to fill it with meaning. A small client with no marketing budget should
  lean suggestive, not abstract.
- **The "so-bad-it's-taken" test.** If the perfect .com is genuinely free, be suspicious — it
  usually means the name is weak or the space is dead.
- **Say it before you see it.** Every finalist gets read aloud. If you stumble, it's out.
- **No manufactured misspellings** (dropped vowels, z-for-s) without a real reason. They cost
  you forever in spelled-out URLs and support calls.
- **Two meanings beat one.** The best names reward a second look.

### Hard anti-patterns — auto-flag these

Tin-eared portmanteaus; unpronounceable coinages; names that box in v1; accidental profanity
or bad cross-language meaning; names one letter off a big competitor; over-literal descriptors;
anything that needs "it's spelled like X but with a Y". Flag on sight, say why, offer the fix.

## Workflow

The skill moves **divergent → convergent**, but the client can bounce back to brainstorm at
any point. Don't force a straight line.

### 1. Intake
Read the context store; run the tight intake only for gaps. Lock the handle-hungry vs handle-
light mode and the boldness dial before generating.

### 2. Territory pass
Generate a first spread of ~15–25 names, **grouped by territory**, each with its tag and a
one-line rationale. Show the range deliberately — a couple of safe descriptors, several
evocatives, some coinages, a metaphor or two. The client is choosing a *direction* as much as
a name.

### 3. Interactive divergence
The client reacts. Learn the vector — "more coined, less literal", "warmer", "shorter", "more
like *that* one" — and regenerate against it. Repeat freely; this is the brainstorm-infinitely
part. Keep tagging territories so the space stays visible even as it narrows.

### 4. Explorer artefact (opt-in — offer when the round gets big)
Stay in chat for small rounds. Once there are enough candidates that sorting them in prose gets
unwieldy (roughly 20+, or when the client starts losing track of favourites), offer to spin up
the interactive name-space explorer — a board where they rate, cluster, sort, and run live
domain checks visually. See `references/explorer-artefact.md` for the build. Don't spin it up
by default; offer it.

### 5. Convergence
Narrow to a shortlist of ~5–8. Run the full check pipeline (below) on the finalists only.

### 6. Deliverable
A rated, checked, ranked shortlist with a single recommendation and runners-up,
given a client voice pass before it ships, if you have one. Structure in §Deliverable.

### 7. Handoff
On the chosen name, offer `essence-craft` (tagline / signature line) and `brand-asset-renderer`
(wordmark + asset set).

## The check pipeline — what's solid, what's only a signal

Be honest about which checks are real. Run checks **on the shortlist, on demand** — never on
every name during divergence (rate-limit and noise). For handle-light names, skip the
handle/domain rows unless the client asks.

| Check | Tool | Reliability | Notes |
|---|---|---|---|
| Domain availability + price | `check_domain_availability_and_price` (Vercel MCP) | **Solid** | Pass a `names` array; batch the exact-match `.com` + TLD sweep + modifier variants for the shortlist in one call. Returns `available`, `price`, `purchaseUrl` per name. Full strategy below; exact shape in `references/explorer-artefact.md`. |
| Social handle availability | `web_search_exa` + direct profile-URL probes | **Signal only** | Check the fixed core set (below). A blank profile page ≠ a registrable handle — say so. |
| Search competition / namesakes | `web_search_exa` | **Good signal** | Surfaces existing companies/products on the same name, obvious collisions, SEO crowding. |
| Trademark | `web_search_exa` over USPTO / EUIPO / UKIPO surfaces | **Signal only — never a verdict** | Surface obvious same-class collisions and log the search. Then state plainly, in bold, that this is **not legal clearance** — get a lawyer before committing. Do not imply a name is "clear". |
| Cross-language / bad meaning | model knowledge + `web_search_exa` | **Good** | Flag unfortunate meanings or awkward sounds in major languages. |

**Handle check — the core set.** For handle-hungry names, default to **X, Instagram, and
LinkedIn**, plus **GitHub/npm for developer tools** where relevant. Keep it to the handful that
matter; don't sweep thirty platforms. Present handle results as signals with the blank-page-≠-
registrable caveat attached.

**Domain strategy — exact match, then TLD sweep, then modifiers.** A taken exact-match `.com`
is not the end of a name. For each shortlisted handle-hungry name, build the candidate domain
list in this order and batch it all into one `check_domain_availability_and_price` call:

1. **Exact match, `.com` first.** The default the world still assumes. Always check it.
2. **TLD sweep** — the same base across the TLDs that read as legitimate for the client's
   category: `.io`, `.ai`, `.so`, `.co`, `.app`, `.dev`, `.xyz`. Match the TLD to the audience
   (`.ai` for AI tools, `.io`/`.dev` for developer products, `.com` still safest for broad B2B
   and consumer). A clean `.com` beats a clever TLD for anything mainstream — flag when a name
   only survives on a niche TLD.
3. **Name modifiers on `.com`** — the accepted patterns when the bare name is gone:
   - **Verb prefixes:** `get[name].com`, `try[name].com`, `use[name].com`, `join[name].com`,
     `meet[name].com` (widely used and credible — Get Bootstrap, Try Notion).
   - **Suffixes:** `[name]hq.com`, `[name]app.com`, `[name].com` → `[name]ai.com`,
     `[name]hub.com`, `[name]labs.com`.
   - Keep these to the few that read naturally for the brand; don't generate twenty. Note that
     verb-prefix domains still usually want the bare name as the eventual acquisition target.
4. **Modifier + niche TLD** as the last rung (`get[name].io`, `[name]hq.ai`).

Report the *best available option per name* — ideally exact `.com`, else the strongest
fallback — and say which rung it came from, so the client sees whether a name is a clean win or
a compromise. When a name only survives three rungs down, that's a mark against it in the
Availability score, not a disqualification on its own.

**The domain tool has no premium/EAP flag** (unlike registrar APIs). It returns a plain
available/price. If the exact `.com` comes back unavailable, work down the rungs above rather
than guessing at premium pricing.

**Availability is a gate only for handle-hungry names, and only near decision.** A taken `.com`
on a feature name is a shrug. A taken exact `.com` on the company name is a real constraint —
but the route around it (a credible modifier, a category-fit TLD, or acquiring the bare name
later) usually exists. Name that route rather than killing the name outright.

## Deliverable (convergent output)

Client-ready shortlist, voice-passed. Dry register — this is
analysis and it's about a decision the client will spend real money committing to, so no
flourish. Keep the order:

- **Recommendation** — one name, and why, in *this client's* brand-context terms (not generic
  praise). Territory, what it does for the positioning, how it reads.
- **Runners-up** — 4–7, each with its territory, one-line rationale, rubric read, and
  availability status.
- **Rejected-territories note** — what you explored and consciously ruled out, and why. This
  shows rigour and stops the client wondering if you missed an obvious lane.
- **Availability appendix** — domains checked with prices and `purchaseUrl`s, handle signals,
  and the trademark caveat **in bold**: *signals only, not legal clearance*.
- **Next steps** — legal clearance first, then tagline (`essence-craft`) and wordmark
  (`brand-asset-renderer`).

Write the shortlist and the decision to the engagement folder as a draft (a dated note in
`notes/`, or the folder's convention). Propose, don't overwrite — a chosen name that hardens
into a foundation graduates to `strategy/` only once the client ratifies it.

## Quality rules

1. Read the context store before asking the client anything.
2. Lock the handle-hungry vs handle-light mode at intake — it decides whether availability is a
   gate or a footnote.
3. Every round spans at least 4–5 territories. No forty-coinages monoculture.
4. Tag every name with its territory and give it a one-line rationale. No bare lists.
5. Score against the rubric; say-ability and spell-ability are pass/fail, not nice-to-haves.
6. Auto-flag anti-patterns on sight, with the reason and a fix.
7. Run live checks on the shortlist only, on demand — never on every name mid-brainstorm.
8. Domain availability is real; handle, search, and trademark are **signals**. Label them as
   such. Never imply a name is legally clear.
9. Trademark caveat ships in bold in every deliverable that touches availability.
10. Say every finalist aloud before recommending it. If it stumbles, it's out.
11. Availability is a gate only for handle-hungry names near decision, and never a silent
    killer — name the route around a taken domain.
12. Recommend in the client's own brand terms, not generic superlatives.

## Common failure modes to avoid

- Generating one aesthetic forty times instead of showing the territory space.
- Killing a strong name early because its `.com` is taken (especially on handle-light names).
- Presenting handle or trademark checks as if they were verdicts.
- Running checks on every name during divergence and drowning in noise / rate limits.
- Manufactured misspellings to force a free domain.
- A name one letter off a competitor sailing through because it "sounds good".
- Recommending with generic praise instead of brand-context reasons.
- Spinning up the explorer artefact by default when a chat round would do.

## Method lineage

Use as lineage, not as copy:

- Alexandra Watkins, *Hello, My Name Is Awesome* — SMILE (suggestive, memorable, imagery,
  legs, positive) and SCRATCH (the anti-patterns), the backbone of the rubric and the
  say-it-aloud rule.
- Lexicon / sound-symbolism practice — why certain sounds carry certain feelings; feeds
  meaning-fit and say-ability.
- Igor / Catchword category theory — the territories and the distinctive-beats-descriptive
  house line.
- Inference doctrine — read context before asking, visible and graded assumptions (solid check
  vs signal), propose-don't-overwrite the spine.
- Voice: dry mode on the deliverable and anything about money;
  concision; flag the trademark caveat once, hard, then commit.

## Handoffs

- `brand-architecture` — if intake reveals the thing shouldn't have its own name at all.
- `essence-craft` — tagline / signature line around the chosen name.
- `brand-asset-renderer` — wordmark and asset set for the chosen name.
- `positioning` / `icp` — close a foundation gap if names keep missing because the category or
  buyer isn't pinned down.
