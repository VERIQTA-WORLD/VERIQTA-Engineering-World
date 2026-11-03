# Validation: Engineering outcomes and evidence

`VW-S001` · independent review not completed

## Content and technical checks

The section includes explanations and a worked example, expanded VW-C001 questions/answers, a distinct release-packet exercise VW-E007, a fictional recovery incident VW-I006, separate complete solutions and a checkpoint rubric. Day 1 has a fuller conceptual explanation and solution; its task remains distinct from the library exercise. Source URLs and dates are recorded in the catalogues.

Manual technical checking compares the explanations and solutions with the supplied evidence: request counts are not user counts, the 500 ms limit is inclusive, unknown correctness is not demonstrated success, and a requested rollback is not a completed recovery. No independent reviewer is claimed.

## Reproducible execution

The optional Python checker reads the 28-row fictional CSV. Expected eligible counts are 12 per version; demonstrated-good counts are baseline 9 and candidate 8, with one unchecked candidate result. Reference totals are stored separately from the checker so a changed implementation cannot silently redefine the expected answer.

Run from the repository root:

```sh
python3 ai/engineering-evidence/examples/check_evidence.py ai/engineering-evidence/examples/requests.csv
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
```

Tests cover the exact fixture, inclusive timing boundary, fast wrong answers, unknown correctness, health-check exclusions, zero traffic, duplicate IDs, invalid columns/values and CLI failure handling without dumping input. Tests run in memory or disposable directories and use no network, credentials or external model.

Observed execution environment: macOS 26.2, Python 3.9.6. CI separately exercises the checker tests on its configured Ubuntu/Python runner when the published run completes. See the [machine-readable validation record](../catalogue/validation.json) for observed results and dates.

## Limits

The checker verifies arithmetic and input handling only. It does not establish source-label truth, an application result, representative production traffic, statistical confidence or a suitable reliability target. The incident and conceptual answers require human reasoning; they have not been independently reviewed. No service, cloud infrastructure or AI model was executed. Physical mobile-device rendering was not tested.

The section is complete for its promised offline learning scope; its editorial state remains draft. Planned follow-on sections are not included in that claim.

[Section](../ai/engineering-evidence/README.md) · [Checkpoint solution](../ai/engineering-evidence/solutions/checkpoint.md)
