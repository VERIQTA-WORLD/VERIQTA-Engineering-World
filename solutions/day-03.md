# Day 3 solution: Navigate files and explain permissions

Draft guidance; not independent review.

## Reasoning and expected result

600 is owner read/write with no group/other access. 400 removes owner write. Directory traversal needs execute permission; deletion concerns the parent directory, subject to other controls. A permission listing is an observation, not a complete access-control audit: ACLs and elevated privileges can change effective behavior.

## Acceptance

The owner has read/write at 600 and read-only at 400. The content remains mode=demo. Explain why a privileged process could bypass your ordinary permission expectations and why directory permissions also matter.

[Return to lesson](../journey/days/day-03.md)
