# Maintainer operations

## Local checks

Use Python 3.9+ with the standard library. Run:

```sh
python3 scripts/catalogue.py --write
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s ai/engineering-evidence/tests -v
python3 scripts/check_labs.py
python3 ai/engineering-evidence/examples/check_evidence.py ai/engineering-evidence/examples/requests.csv
```

The validator checks metadata, IDs, references, required sections, basic Markdown quality, internal files/anchors, image paths and generated navigation. It does not fetch every external reference, prove prose correctness or execute cloud/container labs. The local lab runner uses only explicit disposable fixtures, no contributed scripts or credentials. Run runtime-specific checks separately in a suitable isolated environment.

## Review and validation records

Editorial states: planned → draft → reviewed. Record reviewer/date before reviewed. Execution is independent: not-run, passed, failed or partial with exact environment, date, result and scope. Add observed evidence to catalogue/validation.json; do not replace an unexecuted live lab status with a static pass. Check that generated counts remain derived from records.

## Publication

Inspect git status and diff, ensure only intended files are staged, scan for secrets/private paths and validate local SVGs. Confirm owner and remote. Run checks before commit. Use ordinary fast-forward pushes only when authorised. If the remote changes, fetch and integrate without overwriting unrelated work; rerun relevant checks.

## Maintenance cadence

Triage broken labs before adding volume. Recheck sources when software behavior changes; schedule a source review each quarter when maintainers are available. Promote draft material after independent technical review. Retire obsolete commands with explanation and a stable pointer. Do not claim a maintenance service-level guarantee the volunteer project cannot support.

## Section publication workflow

Use the [section development sequence](section-plan.md) to select one coherent unit with explicit prerequisites and completion evidence. Finish its learning sequence, canonical practice, solutions and checkpoint before extending another section. The AI area contains multiple separately developed sections.

Validate technical claims against primary sources, record supported environments and source dates, run suitable disposable checks, and distinguish static validation from execution and independent review. Update catalogues, indexes and counts; inspect the staged diff for unrelated files and sensitive data before publishing.

Publish each authorised completed section directly to main with an ordinary push. Report the commit, checks and limitations; name the next section and ask the requester whether to continue to that specific section. Stop until they approve. This section-by-section approval boundary supersedes the older batch roadmap. Routine edits within the approved section need no additional approval.
