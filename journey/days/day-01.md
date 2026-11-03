# Day 1: Define an engineering outcome

`VW-DAY001` · beginner · 60 minutes · draft · free/local

## Learning outcomes

Map a small service change from request to feedback; identify one user outcome Explain the result and one limitation.

## Prerequisites

No prior engineering experience required.

## Environment and scope

No tools beyond a text editor. No code execution or account required.

## Prerequisite checks

Check the listed tools exist before starting. If one is missing, record that limitation and consult its official installation guide; do not substitute shared infrastructure.

## Setup

Use a fresh disposable directory for the task. Keep an evidence note outside any directory you intend to remove. Read the cleanup instructions first.

## Explanation

A deployment is an event; a useful engineering outcome is an observable change for users. DevOps connects development and operations through shared responsibility, short feedback loops and repeatable work. Tools help only when the team can explain what they are measuring and who acts on the result.

## Practical task

Create `outcome.md` in a disposable learning folder. Simulation: a library-search team wants to release a faster search page. Current evidence says “build passes”; there is no request or usability measurement. Map request → code → test → release → observe. For each stage, name one artifact and one feedback owner. Define a successful search request without using “server is running.”

## Expected observations and success criteria

Your map contains five stages, a user-visible success definition, a measurement window and one stated uncertainty. Write a stop condition for a rollout if user results worsen.

## Verification

Record the exact commands or reasoning, observed output and any mismatch with the criteria. A text review is not an execution test. Keep simulated evidence labelled.

## Troubleshooting

If a path fails, confirm the current directory and quoted absolute path first. If a tool behaves differently, record OS/tool versions and compare the official reference before changing the task scope.

## Cleanup

Remove your disposable folder after retaining a copy of the outcome record.

## Reflection

What would make your metric misleading? Who receives the feedback?

## Optional extension

Add a countermetric that detects faster but incorrect results.

## Related library content

[VW-C001](../../library/vw-c001.md) offers a distinct follow-up activity.

## Sources

[Official reference](https://sre.google/sre-book/embracing-risk/). Source recorded 2026-11-02. Full metadata is in [the journey catalogue](../../catalogue/journey.json).

[Solution](../../solutions/day-01.md) · [Curriculum](../README.md)
