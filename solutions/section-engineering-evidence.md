# Checkpoint solution: Engineering outcomes and evidence

`VW-S001` · self-assessment guidance · draft, not independent review

The checkpoint is an explanation task. A matching phrase or checker result alone does not pass it. Use these criteria to audit your own evidence note.

## 1. Distinguish the claims

A configured pipeline passed; a particular request returned a status; a user obtained the intended result. These are different claims with different observation boundaries. In VW-E007, equal status proportions of 11/12 conceal baseline demonstrated-good outcomes of 9/12 and candidate 8/12, plus one unchecked candidate result. In VW-I006, eight health checks do not verify search recovery.

## 2. Make the calculation reproducible

For VW-E007, include only `/search`, count 12 requests per version and use status 200 AND correctness true AND duration <= 500 ms for good. The window is 10:00–10:05 UTC in the simulation. Retain the fractions; rounded values are 75% versus 66.67%. Keep C12 eligible but unknown. If your note lacks the boundary condition or exclusion list, another person cannot reproduce it reliably.

## 3. Separate inference from fact

“C10 is labelled incorrect in the packet” is an observation. “Candidate-specific result handling may differ” is a hypothesis. “A database caused the fault” is unsupported. The labels themselves come from a fictional fixture; the arithmetic checker cannot establish their real-world truth.

## 4. Predict a discriminating check

Compare a controlled input with a known expected answer through known revisions and the same path. A candidate-only repeatable wrong answer supports a version-specific explanation. The same failure on both versions weakens it and suggests shared assumptions, data or the result oracle need inspection. Specify what is held constant; do not hide timing, route or authentication differences.

## 5. Justify the handoff decision

Hold expansion under VW-E007's teaching gate while C12 and the relative result are unresolved. A confirmed-correct C12 could make candidate 9/12 and satisfy both teaching conditions, without proving global release safety. Assign the next check to a role and the next decision to a coordinator. In VW-I006, say gateway recovery remains unverified; confirm the active revision and run the intended user path before announcing recovery.

## Completion standard

All five criteria need explicit evidence. Correct the missing parts and recheck. The section is complete for self-study when you can explain the result without reading the solution, describe a competing explanation and identify one limitation of the check you used. Continue to the existing Day 2 starter when ready; the full Safe local learning environments section remains planned.

[Return to checkpoint](../foundations/engineering-evidence/README.md#section-checkpoint)
