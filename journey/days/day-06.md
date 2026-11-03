# Day 6: Write a bounded shell check

`VW-DAY006` · beginner · 60 minutes · free/local

## Learning outcomes

Write a script that checks one file and returns meaningful exit codes Explain the result and one limitation.

## Prerequisites

Complete [Day 5](day-05.md) and retain your notes.

## Environment and scope

POSIX sh and grep on macOS/Linux/WSL. No execution bit required when invoking sh.

## Prerequisite checks

Check the listed tools exist before starting. If one is missing, record that limitation and consult its official installation guide; do not substitute shared infrastructure.

## Setup

Use a fresh disposable directory for the task. Keep an evidence note outside any directory you intend to remove. Read the cleanup instructions first.

## Explanation

An automation contract defines input, output and failure behavior. Quote path arguments so that spaces remain part of one path. Avoid a script that silently treats a failed check as success; callers need a reliable status to decide what happens next.

## Practical task

In a disposable directory create `check-config.sh`:

```sh
#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo 'usage: check-config.sh FILE' >&2
    exit 2
fi
if [ ! -f "$1" ]; then
    echo 'config file missing' >&2
    exit 1
fi
if ! grep -q '^mode=demo$' "$1"; then
    echo 'expected demo mode absent' >&2
    exit 1
fi
echo 'config check passed'
```

Run it using `sh check-config.sh`. Create `good config.txt` with mode=demo and `bad.txt` with mode=prod. Test valid file, invalid file, missing file and no argument; capture `$?` immediately after each run.

## Expected observations and success criteria

Exit codes are 0, 1, 1 and 2 respectively. The valid path contains a space and still passes. Run `sh -n check-config.sh` for syntax evidence separately.

## Verification

Record the exact commands or reasoning, observed output and any mismatch with the criteria. A text review is not an execution test. Keep simulated evidence labelled.

## Troubleshooting

If a path fails, confirm the current directory and quoted absolute path first. If a tool behaves differently, record OS/tool versions and compare the official reference before changing the task scope.

## Cleanup

Remove only check-config.sh and the two fixture files, then rmdir the disposable directory.

## Reflection

How could duplicate keys create a false pass? Why is syntax validation different from executing the tests?

## Optional extension

Reject duplicate mode keys and add a test before claiming stronger validation.

## Related library content

[VW-C001](../../library/vw-c001.md) offers a distinct follow-up activity.

## Sources

[Official reference](https://www.gnu.org/software/bash/manual/bash.html). Source recorded 2026-11-02. Full metadata is in [the journey catalogue](../../catalogue/journey.json).

[Solution](../solutions/day-06.md) · [Curriculum](../README.md)
