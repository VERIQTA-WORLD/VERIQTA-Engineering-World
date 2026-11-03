# Repository instructions

Project: VERIQTA Engineering World. DevOps is one area in a broader engineering library. Preserve unrelated work, stable IDs and useful paths. Do not create a separate repository, website or backend for learning-content tasks.

Read docs/architecture.md, docs/style-guide.md and docs/maintainers.md before editing content. Use original explanations and fixtures. Never import licensed material without checking and recording terms. Preserve existing licences; an unresolved licensing decision is not authority to apply one.

Keep one canonical exercise. Separate solutions. Catalogue JSON is authoritative for status and generated indexes. Planned items do not count as authored. Generation never qualifies as independent review. Execution evidence must identify scope, date, environment and actual result; static checks are not runtime validation.

Run python3 scripts/catalogue.py --write, python3 scripts/validate.py, python3 -m unittest discover -s tests -v and appropriate disposable lab checks. Do not execute arbitrary contributed scripts with privileged credentials. No paid APIs, cloud provisioning or private fixture data in default checks.

Before publication inspect the complete staged diff, links, image paths, credentials and unrelated files. Never force push or rewrite shared history. Follow the current user's commit/push authorisation; do not infer perpetual publication authority from this file. Report commit and push status, authored/planned counts, validation scope, untested environments and the next concrete batch.
