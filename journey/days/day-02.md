# Day 2: Build a safe learning workspace

`VW-DAY002` · beginner · 60 minutes · free/local

## Learning outcomes

Create a scoped workspace and inventory your local tools without credentials Explain the result and one limitation.

## Prerequisites

Complete [Day 1](day-01.md) and retain your notes.

## Environment and scope

POSIX shell on macOS or Linux; Windows learners use WSL. No sudo. Git and Python are inventoried today, required later.

## Prerequisite checks

Check the listed tools exist before starting. If one is missing, record that limitation and consult its official installation guide; do not substitute shared infrastructure.

## Setup

Use a fresh disposable directory for the task. Keep an evidence note outside any directory you intend to remove. Read the cleanup instructions first.

## Explanation

A learning environment should be easy to identify and discard. A command has a scope: the current directory, the user account, the host or an external service. Recording that scope before action helps make experiments reversible. Never assume a tutorial command belongs on a production machine.

## Practical task

In a POSIX shell run:

```sh
workspace=$(mktemp -d)
printf '%s\n' "$workspace"
mkdir "$workspace/notes" "$workspace/fixtures"
command -v git
command -v python3
uname -s
printf 'local-only; no credentials; no cloud resources\n' > "$workspace/notes/scope.txt"
```

Save OS and tool versions in `notes/environment.txt` using `git --version` and `python3 --version`. Do not export your complete environment: it can contain credentials.

## Expected observations and success criteria

The printed path exists; it contains exactly notes and fixtures. Your environment record names OS, shell, tool versions and no-spend scope. `cat "$workspace/notes/scope.txt"` confirms the intended boundary.

## Verification

Record the exact commands or reasoning, observed output and any mismatch with the criteria. A text review is not an execution test. Keep simulated evidence labelled.

## Troubleshooting

If a path fails, confirm the current directory and quoted absolute path first. If a tool behaves differently, record OS/tool versions and compare the official reference before changing the task scope.

## Cleanup

Inspect the printed path. Remove scope.txt and environment.txt, then rmdir the two child folders and workspace; keep it instead if continuing tomorrow.

## Reflection

Which command would have touched more than this workspace? What information should stay out of a public environment report?

## Optional extension

Create a checklist for a disposable Linux VM without provisioning one.

## Related library content

[VW-C001](../../library/vw-c001.md) offers a distinct follow-up activity.

## Sources

[Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html). Source recorded 2026-11-02. Full metadata is in [the journey catalogue](../../catalogue/journey.json).

[Solution](../../solutions/day-02.md) · [Curriculum](../README.md)
