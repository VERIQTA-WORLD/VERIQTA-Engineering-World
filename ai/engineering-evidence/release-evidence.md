# Review a release evidence packet

`VW-E007` · beginner · 55 minutes · free/offline

## Mission

Simulation: a reading-list service is testing a candidate release. The build passed and the dashboard shows the same HTTP success proportion for both versions. Prepare a release handoff that answers whether the supplied evidence supports expansion.

The teaching gate is explicit: the candidate must demonstrate at least the baseline's observed good-outcome proportion, and every eligible result must have a correctness label of true or false. This is a practice rule, not a recommended production target or a statistical experiment design.

## Outcomes

You will calculate status success and demonstrated good outcomes separately, identify unknown evidence, trace inclusion decisions to request IDs and explain a bounded decision without inventing root cause.

## Environment and scope

Read [Engineering outcomes and evidence](README.md) first. A text editor or spreadsheet-free hand calculation is sufficient. Optional verification uses Python 3.9+ standard library on Linux, macOS or Windows. No server, shell expertise, account or cloud resources are required.

## Prerequisite checks

Explain numerator (count meeting a criterion) and denominator (eligible total) in your own words. If you cannot distinguish an observation from an inference, revisit the section's examples before proceeding. The [concept questions](../../library/vw-c001.md) are useful preparation.

## Setup

Open the [fixture description](examples/README.md) and [request records](examples/requests.csv). All rows are fictional and share one five-minute window. Write your answers in a personal note; do not alter the source fixture or open the expected totals yet.

Use this outcome definition exactly: an eligible request is `/search`; a demonstrated good request has status 200, correctness `true` and duration <= 500 ms. Health checks are excluded. Unknown correctness remains eligible but is not demonstrated good. Its actual result is unknown, not proven incorrect.

## Concepts

An **audit trail** makes your calculation reproducible: list the rows you excluded and the rows that failed each criterion. A 500 ms request meets this inclusive limit; 501 ms does not. A request can fail multiple conditions, so counting each failure category and adding them may double-count requests.

A **percentage point** is the difference between two percentages. Going from 75% to about 66.67% is a fall of about 8.33 percentage points. It is not a fall of 8.33% relative to 75%; those are different calculations.

## Tasks

1. List excluded health-check IDs. State the eligible denominator for each version and why it is not the total CSV row count.
2. Calculate each version's status-200 proportion, then its demonstrated-good proportion. Keep fractions as well as rounded percentages.
3. List all eligible rows not demonstrated good, with the reason for each. Report unchecked correctness separately.
4. Decide whether the teaching gate passes. Explain whether checking C12 alone could make every gate condition pass.
5. Write a six-part handoff: window/population, observations with IDs, calculation, decision, next check with owner role, and limits. Do not say the candidate caused a database failure: no database evidence is supplied.
6. Choose a bounded next check. Predict what you would observe if result correctness is the main difference, and what would weaken that hypothesis.

## Expected observations

Each version has health checks that do not belong in the search denominator. Equal HTTP success proportions can conceal differences in correctness, timing and measurement completeness. The unknown result changes how confidently you can describe observed success.

## Verification

First compare your inclusion list with the CSV. Only after recording your answer, optionally run the reference checker from the repository root:

```sh
python3 ai/engineering-evidence/examples/check_evidence.py ai/engineering-evidence/examples/requests.csv
```

It prints totals and writes no files. Compare your fractions to its output, then read the [explained solution](solutions/release-evidence.md). Passing means correct counts, explicit treatment of C12, a decision that follows both teaching-gate conditions and a claim limited to the supplied window. A matching script result alone does not validate your reasoning or the fixture labels.

## Troubleshooting

If you get 14 eligible requests per version, inspect the route filter. If you differ by one good request, check the inclusive 500 ms boundary and C12's unknown correctness. If your percentages exceed 100%, check whether you added overlapping failure categories. If Python reports an invalid fixture, confirm you are using the unchanged CSV and named path; the manual route remains supported.

## Cleanup

No resources were created. Keep your note as learning evidence or remove only that note. Do not delete the repository fixture. The optional checker modifies nothing and needs no teardown.

## Independent challenge

The team proposes counting unknown correctness as good because the status is 200. Write a response explaining the bias, then calculate the best possible candidate result if C12 is confirmed correct. Decide which conclusions change and which do not. You must not silently change the outcome definition or exclude C12.

## Reflection

What could make the two version populations incomparable in a real rollout? Which failures would a gateway-only record miss? Would passing this small teaching gate prove a safe global release?

## Sources

[Google SRE: implementing SLOs](https://sre.google/workbook/implementing-slos/), checked 2026-11-02, informs the distinction between measurement specification and target selection. The fixture and gate are original teaching constructs, not a production reliability objective.

[Solution](solutions/release-evidence.md) · [Section checkpoint](README.md#section-checkpoint) · [Library](../../library/README.md)
