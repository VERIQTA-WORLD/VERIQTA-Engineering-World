# Day 3: Navigate files and explain permissions

`VW-DAY003` · beginner · 60 minutes · free/local

## Learning outcomes

Create a directory tree; compare file and directory permissions Explain the result and one limitation.

## Prerequisites

Complete [Day 2](day-02.md) and retain your notes.

## Environment and scope

POSIX shell, chmod, ls and cat on Linux/macOS/WSL. Use your own temporary files.

## Prerequisite checks

Check the listed tools exist before starting. If one is missing, record that limitation and consult its official installation guide; do not substitute shared infrastructure.

## Setup

Use a fresh disposable directory for the task. Keep an evidence note outside any directory you intend to remove. Read the cleanup instructions first.

## Explanation

Directories map names to files. Read, write and execute permissions have different meanings for directories: execute permits traversal, while directory write can permit entry changes. File permissions alone do not determine who can remove a directory entry. This lab changes permissions only on a fixture you own.

## Practical task

Use a new temporary folder, then run:

```sh
lab=$(mktemp -d)
mkdir "$lab/config"
printf 'mode=demo\n' > "$lab/config/service.conf"
chmod 600 "$lab/config/service.conf"
ls -ld "$lab/config"
ls -l "$lab/config/service.conf"
cat "$lab/config/service.conf"
```

Draw the absolute path. Explain the permission string and predict the effect of changing this file to 400. Try it, inspect with ls, then restore 600. Do not test with sudo.

## Expected observations and success criteria

The owner has read/write at 600 and read-only at 400. The content remains mode=demo. Explain why a privileged process could bypass your ordinary permission expectations and why directory permissions also matter.

## Verification

Record the exact commands or reasoning, observed output and any mismatch with the criteria. A text review is not an execution test. Keep simulated evidence labelled.

## Troubleshooting

If a path fails, confirm the current directory and quoted absolute path first. If a tool behaves differently, record OS/tool versions and compare the official reference before changing the task scope.

## Cleanup

Restore 600, remove service.conf, then rmdir config and the temporary parent.

## Reflection

Why can a readable file still be unreachable? What permission would a service need for a read-only config?

## Optional extension

Inspect, without changing, how your OS reports ACLs.

## Related library content

[VW-C001](../../library/vw-c001.md) offers a distinct follow-up activity.

## Sources

[Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html). Source recorded 2026-11-02. Full metadata is in [the journey catalogue](../../catalogue/journey.json).

[Solution](../../solutions/day-03.md) · [Curriculum](../README.md)
