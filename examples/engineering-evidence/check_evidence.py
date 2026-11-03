"""Offline arithmetic reference for VW-E007; never contacts a service."""
import csv
import json
from pathlib import Path
import sys

FIELDS = ['request_id', 'version', 'route', 'status', 'correct', 'duration_ms']
VERSIONS = ('baseline', 'candidate')


def summarise(stream):
    reader = csv.DictReader(stream)
    if reader.fieldnames != FIELDS:
        raise ValueError('unexpected columns')
    totals = {v: dict(eligible=0, status_200=0, demonstrated_good=0,
                      unknown_correctness=0) for v in VERSIONS}
    seen = set()
    for row in reader:
        if set(row) != set(FIELDS) or any(v is None for v in row.values()):
            raise ValueError('malformed row')
        ident = row['request_id']
        if not ident or ident in seen:
            raise ValueError('missing or repeated request ID')
        seen.add(ident)
        if row['version'] not in VERSIONS or row['route'] not in {'/search', '/health'}:
            raise ValueError('unsupported version or route')
        if row['correct'] not in {'true', 'false', 'unknown'}:
            raise ValueError('invalid correctness label')
        if not row['status'].isascii() or not row['status'].isdigit():
            raise ValueError('invalid status')
        if not row['duration_ms'].isascii() or not row['duration_ms'].isdigit():
            raise ValueError('invalid duration')
        status, duration = int(row['status']), int(row['duration_ms'])
        if not 100 <= status <= 599:
            raise ValueError('status out of range')
        if row['route'] != '/search':
            continue
        total = totals[row['version']]
        total['eligible'] += 1
        total['status_200'] += status == 200
        total['unknown_correctness'] += row['correct'] == 'unknown'
        total['demonstrated_good'] += (status == 200 and row['correct'] == 'true'
                                      and duration <= 500)
    for total in totals.values():
        total['good_fraction'] = (total['demonstrated_good'] / total['eligible']
                                  if total['eligible'] else None)
    return totals


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print('usage: check_evidence.py FILE.csv', file=sys.stderr)
        return 2
    try:
        with Path(args[0]).open(newline='', encoding='utf-8') as stream:
            totals = summarise(stream)
    except (OSError, ValueError, UnicodeError, csv.Error):
        print('unable to validate fixture; check path, columns and values', file=sys.stderr)
        return 2
    print(json.dumps(totals, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
