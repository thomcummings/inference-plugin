# Vocabulary

Slug: `infra/vocabulary`. The controlled lists the store uses to label things.
Business terms (MQL, activated account) are not defined here; each gets a
glossary row. Adding, renaming or removing a value is a person's decision,
recorded in the changelog with kind `vocabulary`.

## Function

Adapt to the team's shape.

| Value | Covers |
| --- | --- |
| `pmm` | Positioning, messaging, launches |
| `brand` | Identity, narrative, events |
| `content` | Blog, social, video, newsletters |
| `devrel` | Developer relations, docs, community |
| `growth` | Self-serve funnel, experiments, lifecycle |
| `paid` | Paid media |
| `sales` | Pipeline, deals, sales process |
| `abm` | Target accounts and account programmes |
| `cs` | Onboarding and customer success |
| `web` | Website, SEO, answer engines, conversion |
| `ops` | GTM operations, data, tooling, this store |

## Product

[Agreed product names.] Until they are agreed, hold one `placeholder` value and
list "agree product names" as a `[NEEDS DECISION]`. Don't file content under
guessed names.

## Report type

Start with what the team already produces, for example `context-setup`,
`context-refresh`, `context-audit`, `weekly-insight`, `competitive-scan`,
`funnel-review`.

## Standards kind

`rubric`, `example-good`, `example-bad`, `approved-claim`, `banned-phrase`.

## Registry

- Kind: `agent`, `skill`, `routine`.
- Status: `draft`, `trial`, `active`, `degraded`, `dormant`, `retired`. New
  rows enter at `trial` with a review date; an expired trial becomes `dormant`.

## Run result and output type

- Result: `success`, `partial`, `failed`, `blocked`.
- Output type: `report`, `digest`, `alert`, `data-update`, `no-change`.

## Changelog kind

`content`, `structure`, `vocabulary`, `definitions` (definitions covers
registry rows).

## Personas

[Agreed.] Persona slugs are named by role, never by number.
