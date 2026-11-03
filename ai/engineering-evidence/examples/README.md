# Release evidence fixture

This is fictional, sanitised teaching data for [VW-E007](../release-evidence.md). All rows belong to the same simulated five-minute window, 10:00–10:05 UTC. Versions serve comparable search requests by assumption for this arithmetic exercise; the fixture does not establish that real traffic allocation would be comparable.

Each row is one observed request, not a unique person. Request IDs identify rows so you can audit inclusion; no retries are modelled. Gateway-only observations exclude failures before the gateway. Durations are integers in milliseconds measured at that observation boundary. `correct` is a supplied result-check label: `true`, `false` or `unknown`. These labels are assumptions of the simulation, not output of an actual application test.

Only `/search` is eligible. `/health` rows deliberately test denominator selection. A demonstrated good request has status 200, correctness `true` and duration <= 500 ms. Unknown correctness remains in the eligible denominator but is not demonstrated good; report it separately rather than converting it to false or excluding it.

## Files and use

- [requests.csv](requests.csv): learner input, 28 rows.
- [Reference checker](check_evidence.py): optional deterministic arithmetic check, not an AI tool or a live application test.
- [Expected totals](expected.json): solution-side comparison; open after your independent attempt.

Run from the repository root with Python 3.9+:

```sh
python3 ai/engineering-evidence/examples/check_evidence.py ai/engineering-evidence/examples/requests.csv
```

The command reads the named local CSV, writes a JSON summary to stdout and modifies no files. Expected invocation failures exit 2 without dumping the input. It rejects malformed columns, repeated request IDs, unsupported versions, invalid status/duration values and invalid correctness labels. Successful arithmetic still cannot verify that source labels are truthful or that the release is safe.

There is no deployment or network access and nothing to tear down. If you save a personal note, retain it outside your checkout or remove only that note when finished.

Implementation reference checked 2026-11-02: [Python csv module](https://docs.python.org/3/library/csv.html). The checker uses only standard-library CSV parsing and JSON reporting.
