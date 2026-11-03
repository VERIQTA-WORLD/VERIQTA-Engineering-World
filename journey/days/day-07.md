# Day 7: Review the first evidence bundle

`VW-DAY007` · beginner · 60 minutes · draft · free/local

## Learning outcomes

Investigate a broken handoff using your workspace, Git and shell evidence Explain the result and one limitation.

## Prerequisites

Complete [Day 6](day-06.md) and retain your notes.

## Environment and scope

Prerequisites Days 1–6; POSIX shell and text editor. Offline simulation plus the Day 6 local script.

## Prerequisite checks

Check the listed tools exist before starting. If one is missing, record that limitation and consult its official installation guide; do not substitute shared infrastructure.

## Setup

Use a fresh disposable directory for the task. Keep an evidence note outside any directory you intend to remove. Read the cleanup instructions first.

## Explanation

A checkpoint joins observations across tools without requiring a new product. A useful handoff states the intended outcome, inspected revision, environment and remaining uncertainty. An engineer should be able to reproduce your reasoning without trusting your confidence.

## Practical task

Simulation: a teammate sends a note saying “R2 ready.” Their evidence bundle contains:

```text
Git: revision R2 adds expected mode=demo to the contract.
Config content: mode=prod
Shell: sh -n check-config.sh exits 0
Runtime checks: not run
User check: not run
```

Write `handoff.md` with observations, hypotheses, a minimal next test and release decision. Recreate the Day 6 script in a disposable directory, run it against the provided mode=prod fixture and record the actual status. Do not invent a Git object named R2; it is a simulated revision label.

## Expected observations and success criteria

Your actual check exits 1. Reject “ready” based solely on shell syntax. Explain the contract/config mismatch, separate simulated evidence from your execution, and specify a user-facing check before real release.

## Verification

Record the exact commands or reasoning, observed output and any mismatch with the criteria. A text review is not an execution test. Keep simulated evidence labelled.

## Troubleshooting

If a path fails, confirm the current directory and quoted absolute path first. If a tool behaves differently, record OS/tool versions and compare the official reference before changing the task scope.

## Cleanup

Remove the recreated script and fixture; retain only the sanitised handoff and execution evidence.

## Reflection

Which finding blocks release? What information would make changing the config inappropriate?

## Optional extension

Have a peer reproduce the result from your handoff without further instructions.

## Related library content

[VW-C001](../../library/vw-c001.md) offers a distinct follow-up activity.

## Sources

[Official reference](https://www.gnu.org/software/bash/manual/bash.html). Source recorded 2026-11-02. Full metadata is in [the journey catalogue](../../catalogue/journey.json).

[Solution](../../solutions/day-07.md) · [Curriculum](../README.md)
