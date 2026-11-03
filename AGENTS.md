# Repository instructions

Project: VERIQTA Engineering World. DevOps is one area in a broader engineering library. Preserve unrelated work, stable IDs and useful paths. Do not create a separate repository, website or backend for learning-content tasks.

Read docs/architecture.md, docs/style-guide.md and docs/maintainers.md before editing content. Use original explanations and fixtures. Never import licensed material without checking and recording terms. Preserve existing licences; an unresolved licensing decision is not authority to apply one.

Keep one canonical exercise. Separate solutions. Catalogue JSON is authoritative for status and generated indexes. Planned items do not count as authored. Generation never qualifies as independent review. Execution evidence must identify scope, date, environment and actual result; static checks are not runtime validation.

Run python3 scripts/catalogue.py --write, python3 scripts/validate.py, python3 -m unittest discover -s tests -v and appropriate disposable lab checks. Do not execute arbitrary contributed scripts with privileged credentials. No paid APIs, cloud provisioning or private fixture data in default checks.

Before publication inspect the complete staged diff, links, image paths, credentials and unrelated files. Never force push or rewrite shared history. Follow the current user's commit/push authorisation; do not infer perpetual publication authority from this file. Report commit and push status, authored/planned counts, validation scope, untested environments and the next concrete batch.

## Section-by-section development

Read docs/section-plan.md before selecting work. Develop one coherent section thoroughly; do not interpret an entire topic folder or the full AI curriculum as one section. Preserve the approved 100-day journey, branding and MIT licence. Keep learner pages free of instructions to Codex and public claims of superiority or reference-repository inspiration.

State the selected section's scope first. Complete explanation, varied appropriate practice, fixtures, separate defensible solutions, checkpoint, catalogue/navigation updates and honest validation within that scope. Distinguish authored, technically checked, runtime-executed and independently reviewed material. Do not label generation independent review.

When the user authorises section publication, validate, inspect the diff and push the completed section to main without force-pushing. Summarise completion, checks, limitations and next section. Ask exactly “Would you like me to continue to [specific next section]?” with the actual next section name, then stop and wait. Do not begin the next section without the user's answer. This workflow supersedes older multi-batch roadmap instructions. Do not ask for approval between routine files or steps within the approved section.

## Public presentation

Write learner pages as finished teaching material. Keep editorial draft/review labels in catalogues and maintainer records, not lesson headings, solutions, badges or learner indexes. Preserve honest supported-environment and execution limitations. Place the AI curriculum and its new section material under ai/. Do not promote editorial status merely to remove a public label.

Use the existing top-level folders. Do not add root subject or example directories for AI sections; put section lessons, new practice, examples and solutions under ai/. Keep stable links in existing library/ and solutions/ where needed.
