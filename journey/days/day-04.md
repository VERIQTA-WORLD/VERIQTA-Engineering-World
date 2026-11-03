# Day 4: Turn logs into observations

`VW-DAY004` · beginner · 60 minutes · free/local

## Learning outcomes

Filter a tiny log fixture and separate observations from hypotheses Explain the result and one limitation.

## Prerequisites

Complete [Day 3](day-03.md) and retain your notes.

## Environment and scope

POSIX shell, grep and wc on macOS/Linux/WSL; offline text fixture.

## Prerequisite checks

Check the listed tools exist before starting. If one is missing, record that limitation and consult its official installation guide; do not substitute shared infrastructure.

## Setup

Use a fresh disposable directory for the task. Keep an evidence note outside any directory you intend to remove. Read the cleanup instructions first.

## Explanation

A log is a recorded observation from one component at a particular time, not a complete account of a system. Separate exact observations from hypotheses so that a plausible story does not become an unsupported conclusion. Count denominators and state the time range.

## Practical task

Create a temporary `requests.log` containing:

```text
12:00 route=/search status=200 ms=31
12:01 route=/search status=503 ms=7
12:02 route=/health status=200 ms=1
12:03 route=/search status=503 ms=8
```

Use `wc -l requests.log` and `grep 'status=503' requests.log` inside your disposable directory. Write counts for all requests and search-only requests. List two hypotheses for the search failures and one missing observation for each.

## Expected observations and success criteria

Four records, two 503s, three search requests and two failed searches. Your report distinguishes 2/4 across the sample from 2/3 within search. Do not infer a database failure or a service-wide rate from four lines.

## Verification

Record the exact commands or reasoning, observed output and any mismatch with the criteria. A text review is not an execution test. Keep simulated evidence labelled.

## Troubleshooting

If a path fails, confirm the current directory and quoted absolute path first. If a tool behaves differently, record OS/tool versions and compare the official reference before changing the task scope.

## Cleanup

Remove requests.log and the disposable folder after saving a sanitised observation table.

## Reflection

What could be missing from these logs? How would retries affect your denominator?

## Optional extension

Add a malformed record and explain whether your simple counting method still works.

## Related library content

[VW-C001](../../library/vw-c001.md) offers a distinct follow-up activity.

## Sources

[Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html). Source recorded 2026-11-02. Full metadata is in [the journey catalogue](../../catalogue/journey.json).

[Solution](../../solutions/day-04.md) · [Curriculum](../README.md)
