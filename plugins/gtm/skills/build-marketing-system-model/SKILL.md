---
name: build-marketing-system-model
description: This skill should be used to import IMS diagnostic JSON, compare leadership responses, and build, refresh, inspect, or export a living IMSM client model.
---

# Build Marketing System Model

Resolve every relative file path in this skill from the directory containing this `SKILL.md`.

Create a working, evidence-linked model of a client's marketing system. Treat the model as a living diagnostic overlay, not a one-off audit report and not a replacement folder taxonomy.

## Non-negotiable rules

- Preserve every source unchanged before processing it.
- Separate observed evidence, respondent assessment and agent interpretation.
- Keep self-reported diagnostic conclusions `working` and low-confidence.
- Use the canonical condition codes `ad_hoc`, `early`, `working`, `strong` (plus `unknown`, `not_applicable`); these are stable and map to the L1–L4 display labels (`ad_hoc`=L1 Ad hoc, `early`=L2 Activated, `working`=L3 Adept, `strong`=L4 Adaptive). Normalize legacy `limited` → `early` and legacy `missing` → `ad_hoc`, and preserve the raw source value. L1 (`ad_hoc`) means the capability happens only reactively, by default or through individuals — not that it is absent.
- Keep score, condition, confidence, authority and respondent alignment separate.
- Do not calculate an overall score or percentage.
- Do not average away CEO/Head of Marketing disagreement.
- Do not silently promote agent-derived context into canonical company truth.
- Preserve previous model versions when refreshing.
- Never send private client material to external services unless explicitly authorised.

## Read the right references

Always read [client-model-schema.md](references/client-model-schema.md) before creating or changing a model.

Read [evidence-processing.md](references/evidence-processing.md) when processing anything beyond diagnostic JSON.

Read [local-client-map-renderer.md](references/local-client-map-renderer.md) when creating or changing a local HTML visual map for a client model.

The deterministic IMS diagnostic mapping is in `references/diagnostic-v1-mapping.json`. Do not hand-edit question mappings in generated models.

If your workspace keeps a canonical note for the marketing system map, read it too.
It overrides the bundled mapping when the framework changes. If the taxonomy has changed, stop and update the mapping deliberately before importing new data.

## Choose the operation

### Initialise from diagnostic JSON

Use for the first `ims-diagnostic-response-v1` file for a company.

1. Inspect the JSON without changing it.
2. Confirm or infer the output workspace. Prefer the user's named location. For an existing client, use a clearly named internal working folder inside that client directory; do not use `~/.marketing-audit/`.
3. Run:

```bash
python3 scripts/import_diagnostic.py \
  "/path/to/diagnostic.json" \
  --output-dir "/path/to/client-model-workspace" \
  --company-name "Company name" \
  --company-website "https://example.com"
```

4. Run the validator:

```bash
python3 scripts/validate_model.py "/path/to/client-model-workspace/client-model.json"
```

5. Report component conditions, important gaps, unknowns and the model's evidence limitation. Do not present the result as an audit finding.

Company name and website overrides are optional. Use them when the anonymous diagnostic does not contain those fields.

### Add or compare another diagnostic response

Run `import_diagnostic.py` again with the new JSON and the same output directory. The script preserves the raw response, reloads all diagnostic sources, archives the prior model under `history/`, and rebuilds comparisons.

All responses in one workspace must share an `assessmentId`. If they do not, stop rather than merging companies or assessments.

For paired responses:

- Preserve each respondent's condition.
- Treat a two-step difference as material disagreement.
- Treat one known answer plus one Unknown as a visibility gap.
- Treat disagreement as a question to investigate, not an error to resolve automatically.

### Add a batch of raw context

Use for documents, meeting notes, transcripts, research, data exports, observations or sub-skill outputs.

1. Read the client-domain instructions before touching client files.
2. Preserve sources under the model workspace's `sources/context/` using stable, descriptive names.
3. Create one structured evidence note per source under `evidence/`, following [evidence-processing.md](references/evidence-processing.md).
4. Map assertions to IMSM components and subcomponents. Allow one assertion to touch several areas.
5. Update only the supported capability assessments in `client-model.json`:
   - add `evidence_assertions` and `evidence_refs`;
   - record whether evidence supports, contradicts, qualifies or fills a gap;
   - adjust confidence or condition only when justified;
   - preserve contested conclusions.
6. Set `updated_at`, preserve the previous model in `history/`, then validate and render:

```bash
python3 scripts/validate_model.py "/path/to/client-model.json"
python3 scripts/render_model.py "/path/to/client-model.json"
```

When evidence changes a consequential strategic conclusion, propose the change for human review instead of silently ratifying it.

### Refresh or diff

For a refresh:

1. Check `sources/` for unprocessed files.
2. Process new sources.
3. Reassess only capabilities touched by new evidence.
4. Compare the new model to the most recent version in `history/`.
5. Report:
   - conditions changed;
   - confidence changed;
   - new or resolved unknowns;
   - new disagreements;
   - current priorities implied by the evidence.

Do not describe a change from Unknown to Working as capability improvement unless the capability itself changed; it may only mean visibility improved.

### Status or export

For status, read `client-model.json` and report:

- sources processed and unprocessed;
- respondent coverage;
- component display conditions;
- L1 Ad hoc and L2 Activated capabilities;
- Unknown and contested capabilities;
- confidence distribution;
- last update.

Use `client-model.md` as the portable human-readable export. Re-render it after substantive JSON changes.

### Render the HTML call canvas

`scripts/render_client_map.py` is the reusable, brand-styled HTML viewer (the local call canvas). It renders directly from `client-model.json`, follows `references/local-client-map-renderer.md`, uses the L1–L4 labels and the hosted Inference webfonts, and includes the N-person ladder plus alignment heatmap (spread, not a two-leader average) and call/review modes.

```bash
python3 scripts/render_client_map.py "/path/to/client-model.json"
# optional bespoke narrative for the info sheet:
python3 scripts/render_client_map.py "/path/to/client-model.json" --narrative "/path/to/narrative.html"
```

If a `narrative.html` sits beside the model it is injected into the info sheet automatically; otherwise the info sheet uses a generic auto-generated read. Keep any bespoke narrative in a per-client `narrative.html`, never hard-coded into the renderer.

## Workspace shape

```text
<client-model-workspace>/
├── client-model.json
├── client-model.md
├── client-map.html
├── renderer/
├── sources/
│   ├── diagnostic/
│   └── context/
├── evidence/
└── history/
```

The importer creates the files and folders it needs. Do not delete superseded sources or model versions.

## Interpretation discipline

The questionnaire asks about capability, but one answer can imply several different underlying causes. Keep the first model descriptive.

Display labels are the L1–L4 ladder; the internal codes in brackets are unchanged.

- `L1 · Ad hoc` (code `ad_hoc`) means the capability happens only reactively, by default or through individual effort, with no deliberate or repeatable approach. It does not automatically mean “build this now”, and it does not mean the capability is absent; stage fit still matters.
- `L2 · Activated` (code `early`) means switched on: a deliberate start exists but is minimal, incomplete or unproven.
- `L3 · Adept` (code `working`) means done well and dependably, fit for the current stage, not universally sophisticated.
- `L4 · Adaptive` (code `strong`) means the capability learns and evolves with humans in the right places; it should remain exceptional and evidence-backed.
- `Unknown` is an evidence gap, not a weakness.
- `Not applicable` is not the same as `L1 · Ad hoc`.

Prioritisation and interventions come after evidence review. Do not generate an unbounded recommendation list from questionnaire conditions alone.

## Completion check

Before handing back a model:

- raw inputs are preserved;
- any legacy `limited` values have been normalized to `early`, and any legacy `missing` values to `ad_hoc`, in the model;
- all 30 mapped questions are present;
- source log and evidence references resolve;
- a single response is labelled self-reported and low-confidence;
- paired disagreement remains visible;
- the previous model is preserved after refresh;
- `validate_model.py` passes;
- `client-model.md` matches the current JSON.
- if a local visual map exists or was requested, `client-map.html` has been regenerated and checked against `references/local-client-map-renderer.md`.
