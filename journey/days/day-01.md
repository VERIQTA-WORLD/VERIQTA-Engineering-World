# Day 1: Define an engineering outcome

`VW-DAY001` · beginner · 60 minutes · free/offline

## Learning outcomes

By the end of this lesson, you can explain how engineering outputs differ from user outcomes, map a small change from request to feedback and define an observation that could disprove a success claim. You will write a short outcome contract, not deploy software.

## Prerequisites

No prior engineering experience is required. You only need to read a short scenario and write a note. This is a conceptual lesson; no shell, installation, account or cloud resources are needed.

## Environment and scope

Use any text editor, a Markdown reader or paper. The search-service scenario is fictional. Nothing runs on your machine or changes an external system. No resource setup or cleanup is necessary.

## Explanation

Suppose a team is asked to make searching a reading catalogue faster. It changes code, builds a package, tests it and deploys it. Those are **outputs**: actions completed or things produced. A useful **outcome** is that a reader receives the expected search result within an acceptable time.

A build can pass while a request never reaches the application. A running process can return an error. A fast response can contain the wrong result. You therefore need evidence that matches the claim you want to make.

**DevOps** connects development and operations through shared responsibility, feedback and repeatable work. It is not a claim that one person must perform every role. A small change should have a clear intent, an inspectable artifact, relevant checks, a controlled release and a way to observe what users receive. **Feedback** is information that lets the team adjust its next decision; a dashboard no one acts on is a weak feedback loop.

| Stage | The question to ask | Possible evidence |
| --- | --- | --- |
| Request | What should improve for the reader? | A stated behavior and acceptance criteria |
| Code | What changed, and why? | A small diff tied to the intended behavior |
| Test | Which cases were checked? | Expected results and observed test outcomes |
| Release | What version/configuration is active? | A release record with revision identity |
| Observe | Did the intended request path work? | Correctness, timing, population and window |

A **population** is the set of requests your statement describes. A **window** is the observation period. For example, a five-minute gateway sample says something about requests reaching that gateway during those five minutes; it may miss failures before that point. A **gateway** receives and routes requests to the application.

Write three kinds of statement separately:

- Observation: “Three supplied search checks exceeded one second.”
- Hypothesis: “The new search implementation may be slower.”
- Decision: “Pause expansion and compare the same inputs on both versions.”

The hypothesis is an explanation to test. It is not an established cause. A bounded decision can be sensible while the cause is uncertain, as long as you can explain the evidence and the next check.

## Practical task

Simulation: the library-search team wants a faster search page. The only current evidence is “build passes.” There is no measured search result or user-path test. Write an `outcome.md` note, or its paper equivalent, containing:

1. One sentence defining a useful search result. Include expected correctness, a duration limit, the eligible request population and observation window. Label any proposed number as a teaching assumption rather than a business commitment.
2. A five-stage map: request → code → test → release → observe. For each stage, name one artifact and a role responsible for its feedback. Roles can be fictional; do not invent real team members.
3. Two ways the build could pass while the defined outcome fails. Choose different failure boundaries rather than repeating the same example.
4. One stop condition for a rollout, meaning a criterion that pauses expansion. State who makes the next decision and what check would resolve the uncertainty.
5. One limitation of the observation you propose. If you only measure status codes, explain how you will detect a fast incorrect answer.

You are designing a check, not reporting that it ran. Do not invent request counts or label this a completed deployment.

## Expected observations and success criteria

Your note has a user-visible result, explicit scope and an inspectable feedback map. “Server running” and “pipeline green” are insufficient outcome definitions. A useful stop condition names evidence that can fail, such as an incorrect response to a controlled search input, rather than “stop if anything seems wrong.”

## Verification

Read your note as if another learner had to perform the check. Can they identify the path, expected answer, duration boundary, eligible population and window without asking you? If a crucial detail is missing, revise it.

Then compare your attempt with the [complete example and reasoning](../solutions/day-01.md). Multiple definitions can be defensible; passing means that the evidence could establish or contradict your stated outcome. Record the check as a proposed check until you run it.

## Troubleshooting

If your outcome is “deploy successfully,” ask what the reader receives afterward. If your measure has no denominator, name which attempts are included. If your stop condition requires knowing the cause first, replace it with an observable symptom and a bounded next check. If you choose 100% success, explain the sample and avoid implying that a short perfect sample guarantees future reliability.

## Reflection

Who acts when a check fails? What would make your metric look better while the experience gets worse? Why might restoring an older version fail to undo a data change?

## Optional extension

Add a countermeasure for fast incorrect answers, then name an observation outside your gateway boundary that would improve coverage. Do not expand into a monitoring-system implementation today.

## Related library content

For deeper study, follow [Engineering outcomes and evidence](../../ai/engineering-evidence/README.md), beginning with [VW-C001](../../library/vw-c001.md). Its release-packet exercise and incident are separate activities, not duplicates of this search-outcome design task.

## Sources

Primary references checked 2026-11-02: [Google SRE: monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) and [implementing SLOs](https://sre.google/workbook/implementing-slos/). The scenario and activity are original. [Catalogue metadata](../../catalogue/journey.json) records authorship and validation separately.

[Solution](../solutions/day-01.md) · [Day 2](day-02.md) · [100-day curriculum](../README.md)
