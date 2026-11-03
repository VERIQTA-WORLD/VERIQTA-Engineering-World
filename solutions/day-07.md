# Day 7 solution: Review the first evidence bundle

Draft guidance; not independent review.

## Reasoning and expected result

Syntax passed, but configuration behavior was not checked in the bundle. The supplied config contradicts the stated demo contract and the Day 6 check should fail. Reject or hold the handoff pending intended-environment clarification and behavioral evidence. Blindly changing prod to demo would be unsafe without context. The user outcome still needs a separate request check.

## Acceptance

Your actual check exits 1. Reject “ready” based solely on shell syntax. Explain the contract/config mismatch, separate simulated evidence from your execution, and specify a user-facing check before real release.

[Return to lesson](../journey/days/day-07.md)
