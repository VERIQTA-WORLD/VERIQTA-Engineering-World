# Solution: Review a release evidence packet

`VW-E007` · Solution and reasoning

## Inclusion and calculation

Exclude BH1, BH2, CH1 and CH2 because their route is `/health`. There are 28 CSV rows, but 12 eligible search requests for each version. Neither failed status nor unknown correctness removes an eligible search request from the denominator.

| Version | Eligible | Status 200 | Demonstrated good | Unknown correctness |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 12 | 11 (91.67%) | 9 (75%) | 0 |
| Candidate | 12 | 11 (91.67%) | 8 (66.67%) | 1 |

Baseline B01–B09 are demonstrated good. B09 is exactly 500 ms and passes. B10 is correct with status 200 but takes 501 ms; B11 returns 503 and is labelled false; B12 returns 200 but has an incorrect result. The three failed-good rows are distinct. Do not add B11 twice because it violates two conditions.

Candidate C01–C08 are demonstrated good, including C08 at exactly 500 ms. C09 takes 501 ms; C10 is incorrect; C11 returns 503 and is labelled false. C12 has a 200 status and a short duration, but its correctness was not checked. It is not demonstrated good, and it is also not established to be incorrect.

The difference in demonstrated-good proportion is 8/12 - 9/12 = -1/12, about -8.33 percentage points. The checker deliberately uses a JSON null fraction when there are no eligible requests; no traffic does not mean a 100% good result.

## Gate and independent challenge

Hold expansion under the supplied rule: candidate demonstrated-good proportion is below baseline and one correctness label is unknown. If C12 is checked and confirmed correct, candidate good outcomes rise to 9/12, matching baseline. Both teaching-gate conditions could then pass, provided the new observation is documented. If it is incorrect, the candidate stays at 8/12 and fails the comparison even though completeness is resolved.

Counting C12 as good now would substitute an assumption for an observation. Excluding it would reduce the denominator and select the population based on measurement success. Neither follows the specified contract. A possible upper result of 9/12 is not an observed 9/12.

## Example handoff

“Simulation, 10:00–10:05 UTC: 12 eligible `/search` requests per version observed at the gateway; health checks excluded. Both versions return status 200 on 11/12. Demonstrated good outcomes are baseline 9/12 and candidate 8/12 under the status/correctness/<=500 ms definition. Candidate C12 correctness is unknown. Hold expansion under the teaching gate. The release coordinator owns the next decision; the application test owner should check C12's expected result, then compare incorrect-result cases B12/C10 against controlled expected outputs. Gateway coverage, small sample size and assumed comparable traffic limit the conclusion.”

The role names assign work without inventing a real team or authorising a production change. A useful decision time would be after the scoped check completes or at an explicit review time, rather than “when someone gets around to it.”

## Next check and alternatives

If a candidate-specific result defect explains C10, the same controlled input should produce the incorrect result in the candidate while the baseline matches the expected result. If both fail the same input, inspect the shared expected-result oracle, data or dependency assumptions. An **oracle** is the rule or known answer used to judge correctness. A broken oracle can mislabel a correct application.

Timing differences could also reflect load or different inputs rather than version behavior. Hold inputs and measurement boundary constant where possible. No supplied evidence supports a database cause, customer count, safe rollback or a service-wide long-term success rate.

[Return to exercise](../release-evidence.md)
