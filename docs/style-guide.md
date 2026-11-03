# Content style and review standard

Write directly to a worldwide learner audience. Define acronyms on first use, prefer concrete observations and avoid claims that a short journey establishes professional competence. Separate task instructions from solutions.

## Levels

- Beginner: one or two tools, supplied context, bounded task and explicit verification.
- Intermediate: combine tools, choose among hypotheses, handle incomplete evidence and justify trade-offs.
- Advanced: uncertain requirements, competing risks, failure modes and evaluation design; difficulty does not mean obscure syntax.

## Metadata

Catalogue records require stable ID, title, topic, tags, type, difficulty, prerequisite IDs, minutes, environment, cost, software versions, sources/date, editorial status and independent execution status. Status is planned, draft or reviewed. Draft means substantive authored material, not a placeholder. A reviewed record also needs reviewer and review date. Execution records specify environment, date, result and scope; a subset pass is never a whole-lab pass.

## Lab structure

Include mission, outcomes, environment and scope, prerequisite checks, setup, concepts, tasks, expected observations, verification, troubleshooting, cleanup and reflection. Projects add architecture, milestones, acceptance criteria and portfolio evidence. Explain expected command effects before potentially destructive operations; use disposable local environments by default. Cloud exercises must include a cost boundary and teardown verification; no paid cloud in default CI.

## Other content types

Concept questions need an explained answer and a way to assess reasoning. Incidents need symptoms, impact, evidence, investigation, optional progressive hints, a separate solution, alternatives, recovery verification and prevention trade-offs. Decisions need constraints, options, trade-offs and acceptance criteria. AI exercises also need boundaries, sanitised inputs, an interaction, response criteria, failure modes, independent verification and an explicit human decision.

## Evidence and originality

Fictional scenarios must say simulation. For published incidents, cite the primary report, distinguish facts from adaptations and do not invent private details. Interview material is original practice unless reliable provenance supports a stronger statement. AI output is a suggestion, not proof of cause. Do not mechanically repeat the same prompt across topics.

## Markdown

One H1 per page; descriptive links; fenced code with a language; alt text on images; no trailing whitespace or skipped heading levels. Avoid giant root pages and wide multi-column prose. Use relative internal links and keep anchors stable. The repository checker enforces a lightweight subset; visual and editorial review remain necessary.
