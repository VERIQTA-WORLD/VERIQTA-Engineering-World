# Repository instructions

Project: VERIQTA Engineering World. Canonical repository: https://github.com/VERIQTA-WORLD/VERIQTA-Engineering-World. DevOps is one area in a broader engineering library. Preserve unrelated work, stable IDs and useful paths. Do not create a separate repository, website or backend for learning-content tasks.

Read docs/architecture.md, docs/style-guide.md and docs/maintainers.md before editing content. Use original explanations and fixtures. Never import licensed material without checking and recording terms. Preserve existing licences; an unresolved licensing decision is not authority to apply one.

Keep one canonical exercise. Separate solutions. Catalogue JSON is authoritative for status and generated indexes. Planned items do not count as authored. Generation never qualifies as independent review. Execution evidence must identify scope, date, environment and actual result; static checks are not runtime validation.

Run python3 scripts/catalogue.py --write, python3 scripts/validate.py, python3 -m unittest discover -s tests -v, python3 -m unittest discover -s ai/engineering-evidence/tests -v and appropriate disposable lab checks. Do not execute arbitrary contributed scripts with privileged credentials. No paid APIs, cloud provisioning or private fixture data in default checks.

Before publication inspect the complete staged diff, links, image paths, credentials and unrelated files. Never force push or rewrite shared history. Follow the current user's commit/push authorisation; do not infer perpetual publication authority from this file. Report commit and push status, authored/planned counts, validation scope, untested environments and the next concrete batch.

## Folder-by-folder development

Current stage: repository skeleton and navigation only. Do not author new lessons, challenges, fixtures, solutions or runtime labs until the user selects a root folder for content filling. Preserve existing published material; this is not permission to delete it. Plans and indexes must distinguish available material from future scope.

After a folder is selected, state its purpose and scope, develop its coherent sections thoroughly, run relevant checks and present it for review. The user must approve that folder before work begins in another root folder. Do not treat earlier section/batch roadmaps as authority to populate multiple folders. Routine edits within the selected scope need no additional approval.

Preserve the 100-day journey, branding and MIT licence. Keep learner pages free of instructions to Codex, editorial-status bylines, superiority claims and reference-repository inspiration wording. Record technical checks, runtime scope and independent review honestly in catalogue/maintainer records.

Publication to main follows the current user's authorisation, with diff and sensitive-data inspection and no force-push. After a selected folder is completed, report checks and limitations, ask which named folder the user wants next, and wait for explicit approval before starting it. This workflow supersedes earlier section-by-section or multi-batch instructions.

## Public presentation

Write learner pages as finished teaching material. Keep editorial draft/review labels in catalogues and maintainer records, not lesson headings, solutions, badges or learner indexes. Preserve honest supported-environment and execution limitations. Place the AI curriculum and its new section material under ai/. Do not promote editorial status merely to remove a public label.

Use the existing top-level folders. Do not add root subject or example directories for AI sections; put section lessons, new practice, examples and solutions under ai/. Update links and catalogue records when moving answers into their learning area.

Learning paths belong in the root README and link directly to canonical subject material. Do not recreate a root paths/ folder. Keep root scripts/ for repository-wide maintenance only; put subject-specific executable examples inside the relevant subject folder.

## Root layout constraint

Do not add any new top-level folder without an explicit user request to create that folder. Use the original approved layout; the retired paths/ and solutions/ folders must not be recreated. Current approved root folders are .github/, ai/, assets/, catalogue/, challenges/, docs/, journey/, library/, scripts/ and tests/. The user explicitly authorised challenges/; this is not authority to create any other root folder. Place subject-specific answers, examples and tests inside the corresponding learning area. Root tests/ is for repository-wide validators; root scripts/ is for repository-wide maintenance. AGENTS.md remains at the root because its instructions apply across the repository. This rule applies to future sections as well as routine edits.
