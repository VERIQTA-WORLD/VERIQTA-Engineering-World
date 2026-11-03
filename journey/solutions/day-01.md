# Day 1 solution: Define an engineering outcome

`VW-DAY001` · Solution and reasoning

## Example outcome contract

“During a fictional five-minute comparison, eligible catalogue-search requests observed at the gateway return the expected result within one second.” One second and five minutes are teaching assumptions here, not justified service commitments. Define eligible requests before measuring; do not exclude an attempt merely because it failed.

For a bounded first check, use controlled search inputs with known expected results and record status, response correctness and duration. A known answer provides an **oracle**, the rule used to judge a result. If the oracle is wrong, a test can mislead you. The gateway observation also misses attempts that never reach it, so the contract does not establish all-reader success.

## Example feedback map

| Stage | Artifact | Feedback owner and next action |
| --- | --- | --- |
| Request | Search behavior and expected-result examples | Product/application role confirms the intended user result |
| Code | Small diff and explanation | Author/reviewer compares change with the stated intent |
| Test | Controlled inputs, expected bodies and timings | Test owner investigates a mismatch rather than approving a green label alone |
| Release | Active artifact/configuration revision | Release coordinator confirms what is actually active |
| Observe | Scoped request results and uncertainties | Application and operations roles evaluate the outcome and choose the next check |

This is one workable assignment, not a required organisation chart. Shared responsibility connects the roles around the outcome; recording who performs each check avoids conflicting uncontrolled changes.

## Failures the build can miss

The package can build while a gateway routes requests to the wrong destination. The application can also return an incorrect result quickly because the test omitted that input. These differ: one concerns reaching the intended path, the other concerns semantic correctness after reaching it. Neither requires inventing a database or network root cause.

## Stop condition and decision

A bounded teaching condition is: pause expansion if a defined controlled search input returns the wrong result or misses the assumed one-second limit. The coordinator records the pause and assigns a check comparing the same input on known baseline/candidate revisions through the same path.

If only the candidate repeatedly fails under comparable conditions, a version-specific explanation becomes more plausible. If both fail, inspect shared assumptions, data, routing or the expected-result oracle. A pause does not establish cause; a rollback additionally needs compatibility and recovery evidence.

## Verification and acceptance

Your answer need not match these words, but it must name the expected behavior, observation boundary, time window, eligibility, feedback roles, falsifiable stop condition and limitation. Do not award yourself execution credit for an unrun check. A 200 status without a body check is incomplete evidence for the proposed outcome.

For the optional extension, add an expected-result comparison to prevent fast wrong answers from passing. A client-side or representative external-path observation could improve coverage before the gateway; its geography, identity and sample size would still limit generalisation.

[Return to lesson](../days/day-01.md)
