# Client model schema

## Contents

- [Purpose](#purpose)
- [Authority and confidence](#authority-and-confidence)
- [Top-level model](#top-level-model)
- [Capability assessment](#capability-assessment)
- [Condition and comparison rules](#condition-and-comparison-rules)
- [Updating the model](#updating-the-model)

## Purpose

`client-model.json` is the machine-readable working model of a company's marketing system. `client-model.md` is a generated human-readable view of the same state.

The model is an IMSM overlay, not a folder taxonomy. It points to evidence and retained context without requiring every source document to be reorganised around the seven components.

The v1 model accepts self-reported diagnostic responses and agent-processed source evidence. It does not claim to be an evidence-verified audit.

## Authority and confidence

Keep these concepts separate:

- `model_status`: `working` until a human explicitly ratifies conclusions.
- `condition`: `ad_hoc`, `early`, `working`, `strong`, or null when unresolved.
- `assessment_state`: describes whether answers agree, differ, or remain unknown.
- `confidence`: `low`, `medium`, or `high`.
- `evidence_basis`: explains what supports the conclusion.

A single questionnaire response is self-reported evidence and starts at low confidence. Two independent respondents who agree can raise confidence to medium. Questionnaire agreement alone never creates high confidence. High confidence requires corroborating operational evidence.

Do not promote diagnostic-derived statements into canonical company facts without human review.

## Top-level model

```json
{
  "schema_version": "ims-client-model-v1",
  "taxonomy_version": "ims-v1",
  "model_id": "model_<uuid>",
  "assessment_id": "assessment_<uuid>",
  "model_status": "working",
  "created_at": "ISO-8601",
  "updated_at": "ISO-8601",
  "company": {},
  "respondents": [],
  "current_context": {},
  "presenting_problems": [],
  "components": {},
  "system_observations": {},
  "source_log": [],
  "unmapped_answers": []
}
```

### `company`

Retain stage, buying motion and marketing-team shape from the questionnaire. Company name and website may be absent in anonymous submissions. Treat respondent-provided company data as working context.

### `respondents`

Record response ID, role and completion timestamp. Keep name and email only if the source contains them and the user has authorised retaining them.

### `current_context`

Preserve desired outcomes and biggest constraints by respondent rather than flattening divergent answers.

### `source_log`

Append one entry per diagnostic or context source. Include source ID, type, original filename, response ID where relevant, timestamp and provenance path.

## Capability assessment

Every diagnostic question creates or updates one capability assessment:

```json
{
  "question_id": "orc-03",
  "question": "How are channels selected, assigned a role and reviewed?",
  "primary_subcomponent": "gtm-workflows",
  "secondary_subcomponents": ["planning-and-allocation"],
  "condition": "early",
  "condition_range": ["early", "working"],
  "assessment_state": "adjacent",
  "confidence": "low",
  "evidence_basis": "self_reported_diagnostic",
  "respondent_assessments": [],
  "evidence_refs": ["diagnostic:<response-id>#orc-03"]
}
```

`condition` can be null when responses are materially contested. `condition_range` preserves the observed range.

## Condition and comparison rules

Use the canonical condition codes `ad_hoc`, `early`, `working`, `strong` (stable). If older sources contain `limited`, normalize them to `early`; if they contain `missing`, normalize them to `ad_hoc`. Preserve the original answer in the raw source file. `ad_hoc` (rung 1) denotes a capability that happens only reactively, by default or through individuals, not an absent one. Codes map to L1–L4 display labels; render the label, store the code.

Ordinal values and display labels:

| Condition code | Ordinal | Display label |
|---|---:|---|
| ad_hoc | 1 | L1 · Ad hoc |
| early | 2 | L2 · Activated |
| working | 3 | L3 · Adept |
| strong | 4 | L4 · Adaptive |
| unknown | null | Unknown |
| not_applicable | null | Not applicable |

Comparison rules for two or more responses:

- Same capability condition: `agreement`; retain that condition; medium confidence.
- One ordinal apart: `adjacent`; retain the lower condition and the full range; low confidence.
- Two or more ordinals apart: `material_difference`; condition null; low confidence.
- Unknown plus a capability answer: `visibility_gap`; retain the known condition; low confidence.
- Not applicable plus a capability answer: `applicability_difference`; retain the known condition; low confidence.
- All unknown: `unknown`; condition null.
- All not applicable: `not_applicable`; condition null.
- One response only: `single_response`; retain its condition; low confidence.

Component display conditions are derived from capability conditions for navigation only. Exclude null, Unknown and Not applicable values. Use the lower middle value for an even count. If more than half the component's mapped capabilities are unresolved, display the component as Unknown.

Never calculate an overall score or percentage.

## Updating the model

Preserve source evidence and previous model versions.

When a new diagnostic response arrives:

1. Add the raw JSON to `sources/diagnostic/`.
2. Rebuild assessments from all responses sharing the assessment ID.
3. Archive the previous current model in `history/`.
4. Recompute comparisons and component displays.
5. Keep contested results visible.

When raw context is added:

1. Preserve the original source.
2. Create a structured source summary with provenance.
3. Map each supported assertion to IMSM components and subcomponents.
4. Record whether the evidence supports, contradicts or qualifies the current assessment.
5. Update condition or confidence only when the evidence justifies it.
6. Propose high-impact changes for human review rather than silently promoting them.
