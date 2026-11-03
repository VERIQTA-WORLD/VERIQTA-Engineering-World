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

## Folder development and approval

The current stage is repository skeleton and navigation. Keep future scope in plans and catalogues; do not create empty lesson folders or label planned entries as completed activities. Existing published material stays in place.

Before content filling begins, the requester chooses a root folder. Define its purpose, scope, prerequisites and completion standard, then develop and validate its sections within that folder. Present the completed folder for review. The requester must approve it before development starts in another root folder. This replaces the earlier section/batch publication boundary.

Publish authorised changes with an ordinary push to main after checks and diff review. Record authored material, technical checks, runtime execution and independent review separately. Do not introduce another root folder without an explicit user request naming it. The challenges/ folder is an approved exception; its initial five entries are currently plans only.
