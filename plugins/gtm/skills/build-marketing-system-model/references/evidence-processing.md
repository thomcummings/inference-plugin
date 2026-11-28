# Evidence processing

## Contents

- [Source handling](#source-handling)
- [Source summary](#source-summary)
- [Assertion rules](#assertion-rules)
- [Model update rules](#model-update-rules)

## Source handling

Preserve every supplied source unchanged. Record its original filename, source type, ingestion timestamp and provenance. For connected sources, save a local snapshot with the originating URL or system identifier.

Do not send private client material to external services unless the user explicitly requests it.

Use these broad source types:

- `diagnostic_response`
- `interview`
- `meeting_notes`
- `document`
- `research`
- `performance_data`
- `sub_skill_output`
- `observation`

## Source summary

For each non-diagnostic source, create a structured evidence note:

```markdown
# Evidence: <source description>

Source ID: <stable-id>
Original: <path or source reference>
Source type: <type>
Captured: <date>

## Assertions

### <short assertion>

- IMSM component: <component>
- Primary subcomponent: <subcomponent>
- Secondary subcomponents: <optional list>
- Evidence: <specific observation, quote or data point>
- Relationship: supports | contradicts | qualifies | fills-gap
- Confidence: low | medium | high
- Limitations: <what this source cannot establish>
```

Keep assertions specific. “Messaging is weak” is not evidence. “The homepage, sales deck and founder interview use three different primary customer definitions” is evidence.

## Assertion rules

- Separate observation from interpretation.
- Preserve exact figures and distinctive wording where useful.
- Map evidence one-to-many when it affects several parts of the system.
- Treat absence carefully: a missing item in one reviewed repository is not proof that it does not exist elsewhere.
- Record source limitations and access gaps.
- Do not convert a respondent's confidence into evidence confidence.
- Do not let one document produce high confidence for an organisational capability.
- Surface contradictions rather than resolving them through averaging.

## Model update rules

Questionnaire conditions are hypotheses about capability. Operational evidence can support, contradict or qualify them.

- Raise confidence from low to medium when an independent source supports the diagnostic conclusion.
- Use high confidence only when multiple independent sources or direct system evidence corroborate it.
- Change a condition only when the new evidence speaks directly to that capability.
- Mark a condition contested when credible sources disagree materially.
- Preserve the prior state and the reason for every substantive change.
- Keep current objectives time-bound and separate from canonical strategic Memory.
- Never turn agent inference into canonical company knowledge without review.
