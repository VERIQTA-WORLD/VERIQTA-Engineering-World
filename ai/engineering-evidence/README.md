# Engineering outcomes and evidence

`VW-S001` · beginner · approximately 3 hours across several sessions · free/offline

A team can ship working software and still fail the people using it. A deployment may finish while a request fails, or a fast response may contain the wrong result. This section teaches you to turn an engineering claim into a question you can investigate, a measurement you can interpret and a decision you can explain.

## Scope and prerequisites

You need no Linux, cloud, programming or AI experience. Read tables, compare small numbers and write short explanations. A Markdown reader or text editor is enough; optional calculation checks use Python 3.9 or later with its standard library on Linux, macOS or Windows. Nothing is deployed, no account is required and no resources incur costs.

You will learn to define an observable outcome, distinguish a recorded fact from a proposed explanation, choose a denominator and time window, identify gaps in evidence and decide whether a change should proceed. Formal reliability objectives, incident command and tool-specific diagnosis come later.

## Learning sequence

| Step | Activity | Evidence you will produce | Time |
| --- | --- | --- | ---: |
| 1 | Read the explanations and walkthrough below | A claim rewritten as a measurable outcome | 35 min |
| 2 | [A green deployment and a failed user request](../../library/vw-c001.md) | Answers with explained limits | 25 min |
| 3 | [Review a release evidence packet](release-evidence.md) | Independent calculations and a decision brief | 55 min |
| 4 | [The recovery announcement that outran the evidence](recovery-scenario.md) | Timeline, alternatives and a recovery test | 40 min |
| 5 | Complete the checkpoint below | A defensible engineering handoff | 25 min |

The tasks and solutions remain in their canonical library files. Attempt each task before opening its solution. If you are following the daily route, [Day 1](../../journey/days/day-01.md) is a smaller introduction with a different search-service activity.

## 1. Describe the user outcome

An **output** is something engineering produces: a build artifact, a deployed version or a dashboard. An **outcome** is the useful behavior a person receives. Outputs can contribute to an outcome, but do not establish it by themselves.

| Claim | Useful evidence | What that evidence alone cannot establish |
| --- | --- | --- |
| The build passed | Recorded results for the configured tests | That all relevant tests exist or real requests work |
| The process is running | A process or liveness observation | Correct responses through the user's route |
| The request returned HTTP 200 | A success status from a responder | Correct body, acceptable latency or all-user availability |
| The user completed the task | Defined result observed from the intended path | Every user's experience or future reliability |

HTTP is the protocol commonly used for web requests; a status such as 200 or 503 is one part of a response. A 503 usually represents an unavailable service from the responding component. It does not name the failed component or prove a database fault.

Replace “the new search is better” with a definition that includes the request population, result and timing. For example: “For eligible catalogue-search requests observed by the gateway in this five-minute comparison, return the expected result within one second.” A **gateway** is a component that receives and routes requests. A **population** is the set of requests you intend the statement to describe. If some users fail before reaching that gateway, its record cannot represent them.

This definition is still incomplete until you say how expected results are checked, which requests are eligible and what happens when measurements disappear. An outcome definition is a starting contract, not proof of its own measurement quality.

## 2. Separate observation, inference and decision

An **observation** states what the supplied evidence records. An **inference** proposes what that evidence means. A **decision** selects an action under the current evidence and constraints.

- Observation: 12 of 100 candidate requests returned 503 in the supplied window.
- Inference: the candidate may have introduced a route-specific failure.
- Decision: pause expansion and compare affected routes before sending more users to it.

The inference could be wrong: the two versions may serve different routes or a dependency may have changed at the same time. The pause can still be defensible because it limits exposure while a low-risk check resolves uncertainty. You do not need to invent root cause to make a bounded decision.

Use this evidence chain:

```text
User need -> defined outcome -> scoped observation -> competing explanations
          -> discriminating check -> bounded decision -> recovery verification
```

A **discriminating check** separates alternatives. “Collect more logs” is vague. “Compare the same route through the candidate and baseline during the same window” can test whether a version-specific difference persists. A check should state the expected observation if a hypothesis is true and what would weaken it.

## 3. Count the right things

A **denominator** is the total population in a ratio. A success proportion is good eligible requests divided by all eligible requests. Define “good” and “eligible” before counting. Otherwise it is easy to remove inconvenient failures and report apparent improvement.

For this teaching example, a good request must meet all three conditions:

1. Its status is 200.
2. Its result was checked and is correct.
3. Its observed duration is at most 500 milliseconds, including exactly 500.

If 90 of 100 requests are good, the observed proportion is 90%. If all 100 return 200 but ten have incorrect results, status success is 100% while outcome success is at most 90%. Call these different measurements by different names.

A result from a small fixture is a description of that fixture. It is not a statistically justified estimate of the entire service, and it does not establish a suitable long-term target. Later SRE material develops service level indicators (SLIs), objectives (SLOs) and measurement windows more formally.

## 4. Worked example: the healthy-looking status page

Simulation: a reading-list service introduces a candidate release. A **candidate** is the version being evaluated; the **baseline** is the comparison version. During the same short window, the gateway records:

| Version | Requests | Status 200 | Correct result and status 200 | Good under all three conditions |
| --- | ---: | ---: | ---: | ---: |
| Baseline | 20 | 19 | 19 | 18 |
| Candidate | 20 | 20 | 18 | 17 |

Calculate the measurements separately:

- Baseline status success: 19/20 = 95%; candidate: 20/20 = 100%.
- Baseline good outcomes: 18/20 = 90%; candidate: 17/20 = 85%.

A dashboard showing status alone suggests improvement while the defined outcome worsens by five percentage points. Two candidate responses have incorrect results; another correct response misses the timing limit. Do not add those categories without knowing whether they overlap. The table explicitly supplies the final all-conditions count, so no guess is necessary.

A useful note is: “Candidate status success improved in this sample, but defined good outcomes fell from 18/20 to 17/20. Hold expansion under our teaching gate; investigate result correctness and the slow request. The sample is small and gateway-only.” It does not say the whole service is 85% reliable or that the candidate is proven to cause every failure.

## 5. Choose a bounded decision

A **release gate** is a stated criterion for proceeding. For practice, you may set a rule such as “hold expansion if candidate good-outcome proportion is below baseline.” This is a teaching rule; production criteria need user expectations, representative traffic and an agreed risk policy.

| Option | When it may help | Evidence or constraint to check |
| --- | --- | --- |
| Continue at current exposure | More comparable observations are needed and present risk is acceptable | Explicit exposure limit, owner and stop condition |
| Pause expansion | Evidence is insufficient or a comparison gate fails | A specific next check and next decision time |
| Roll back | A prior version is available and compatible | Artifact/configuration identity, data compatibility and recovery observations |

A **rollback** restores a prior software or configuration state. It may not undo data changes, failed user actions or cached responses. “Roll back immediately” is therefore not a complete decision without recovery constraints. Hold, investigation and rollback are separate choices, not interchangeable phrases.

## 6. Make the handoff usable

A useful handoff lets another person continue without guessing. Include the observed population/window, evidence identifiers, exact calculation, current decision, next check, owner role and remaining uncertainty. Do not post private customer data or credential-bearing logs to make a note look realistic.

Shared responsibility means people from development and operations collaborate on the user outcome. It does not mean everyone changes everything at once. Assign a coordinator for the decision and a specific owner for each check; record what changed so observations remain interpretable.

## Common mistakes and recovery

| Mistake | Why it misleads | How to recover |
| --- | --- | --- |
| Equating a passed test with a healthy user route | Test scope differs from user scope | State exactly what was tested and add a route-level observation |
| Counting only successful requests | Failures vanish from the denominator | Define eligibility independently of the result |
| Calling missing data zero failures | Absence can look healthy | Mark health unknown and investigate measurement coverage |
| Announcing root cause after a correlated change | Timing alone does not distinguish alternatives | Predict and run a discriminating check |
| Treating rollback as guaranteed recovery | Data and configuration can be incompatible | Check compatibility and verify the actual user outcome after recovery |

## Section checkpoint

Use your completed exercise and incident notes. Without looking at the solutions, explain:

1. The difference between pipeline evidence, request status and the intended outcome.
2. The numerator, denominator, boundary condition and window of your calculation.
3. One justified inference and one tempting claim the evidence cannot support.
4. A low-risk next check with predictions for two alternatives.
5. A release or recovery decision, the responsible role and what evidence would change it.

Pass when all five are supported by named evidence and your calculation can be reproduced. If you miss a criterion, revise that part; no score is awarded for confident unsupported wording. Use the [checkpoint solution](solutions/checkpoint.md) only after your attempt. Use the rubric to identify gaps and revise your reasoning before progressing.

## References and progression

Primary references checked 2026-11-02: [Google SRE: monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) explains user-visible and internal observation; [implementing SLOs](https://sre.google/workbook/implementing-slos/) develops explicit measures and objectives. This section uses original small fictional data, not a production case study or copied exercise.

Next planned section: **Safe local learning environments**. Existing [Day 2](../../journey/days/day-02.md) provides a starter workspace activity; the full section is not yet authored. [AI learning index](../README.md) · [Section sequence](../../docs/section-plan.md) · [Validation scope](../../docs/validation-engineering-evidence.md)
