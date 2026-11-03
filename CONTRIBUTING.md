# Contribute to VERIQTA Engineering World

Help make engineering practice clear, reproducible and welcoming. Start with a small correction or one distinct exercise, rather than a large collection of repeated questions.

## Before you start

Read the [style guide](docs/style-guide.md), [code of conduct](CODE_OF_CONDUCT.md), [licensing status](docs/licensing.md) and [roadmap](docs/roadmap.md). Use original explanations and sanitised fictional fixtures. Attribute external ideas and verify permissions before importing assets. Never upload credentials, personal data or private infrastructure details.

## Submit a change

1. Choose an existing issue or describe a concrete learning outcome.
2. Add one canonical Markdown item and a separate solution using the [content template](docs/content-template.md).
3. Add a stable unique record to the relevant JSON catalogue. Keep new work draft; planned work has no placeholder lesson file.
4. Include environment, cost, versions, sources and the date you actually checked them. Record execution evidence only for commands you ran.
5. Regenerate navigation with `python3 scripts/catalogue.py --write`.
6. Run `python3 scripts/validate.py`, `python3 -m unittest discover -s tests -v`, `python3 -m unittest discover -s ai/engineering-evidence/tests -v` and `python3 scripts/check_labs.py` where the supported local environment is available.
7. Open a pull request explaining the result, validation and limitations. Maintainer-authorised direct publication may follow the same checks.

## Reporting issues

Use [GitHub issues](https://github.com/VERIQTA-WORLD/VERIQTA-Engineering-World/issues/new/choose) for incorrect answers, broken labs or topic proposals. Include the content ID, environment, expected and observed results, and redacted reproduction steps. For a suspected secret or private data exposure, contact the owner privately through an available verified channel; do not repeat the sensitive content in a public issue.

## Review

Reviewers check technical reasoning, originality, accessibility, links and reproducibility. Generation or passing CI alone does not make an item reviewed. Record the reviewer's identity and date when changing that status. Contributor ideas are welcome from any region or experience level; English fluency is not an entry requirement.
