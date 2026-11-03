# Day 5: Record a change with Git

`VW-DAY005` · beginner · 60 minutes · free/local

## Learning outcomes

Create and inspect two local commits in a disposable repository Explain the result and one limitation.

## Prerequisites

Complete [Day 4](day-04.md) and retain your notes.

## Environment and scope

Git 2.x, POSIX shell, local temporary repository. No GitHub account, remote or push required.

## Prerequisite checks

Check the listed tools exist before starting. If one is missing, record that limitation and consult its official installation guide; do not substitute shared infrastructure.

## Setup

Use a fresh disposable directory for the task. Keep an evidence note outside any directory you intend to remove. Read the cleanup instructions first.

## Explanation

Git records snapshots and their parent relationships. A small commit lets a reviewer connect a stated intent with changed bytes. The working directory, staging area and committed tree are distinct. This exercise creates a separate disposable repository and never changes this library's history.

## Practical task

Create a new temporary folder and change into it. Run `git init`, then configure a local-only demo identity:

```sh
git config user.name 'VERIQTA Learner'
git config user.email 'learner@example.invalid'
printf 'health check: process only\n' > service.txt
git add service.txt
git commit -m 'Record initial health contract'
printf 'health check: process and dependency readiness\n' > service.txt
git diff
git add service.txt
git diff --cached
git commit -m 'Clarify dependency readiness contract'
git log --oneline -2
git status --short
```

Explain the limitation of this changed health contract; a text edit alone implements no actual health check.

## Expected observations and success criteria

Two commits exist, final status is clean and the second diff shows one replacement line. Record the two commit IDs and explain what the staged diff reviewed.

## Verification

Record the exact commands or reasoning, observed output and any mismatch with the criteria. A text review is not an execution test. Keep simulated evidence labelled.

## Troubleshooting

If a path fails, confirm the current directory and quoted absolute path first. If a tool behaves differently, record OS/tool versions and compare the official reference before changing the task scope.

## Cleanup

Leave the disposable directory before removing it. Inspect its path first; remove only this lab repository. Never apply cleanup to the learning-library checkout.

## Reflection

Why review the staged diff? Should every dependency failure remove a service from traffic?

## Optional extension

Use git show to compare the evidence each commit preserves.

## Related library content

[VW-C001](../../library/vw-c001.md) offers a distinct follow-up activity.

## Sources

[Official reference](https://git-scm.com/docs/gittutorial). Source recorded 2026-11-02. Full metadata is in [the journey catalogue](../../catalogue/journey.json).

[Solution](../solutions/day-05.md) · [Curriculum](../README.md)
