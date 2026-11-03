# Catalogue records

- [Library](library.json): authored canonical items and their metadata.
- [Journey](journey.json): exactly 100 ordered days; planned days have no lesson path.
- [Challenges](challenges.json): planned independent missions, excluded from authored activity counts.
- [Sections](sections.json): authored section scope, canonical content references and the next planned section.
- [Backlog](backlog.json): prioritised domain expansion, including tool-specific AI objectives.
- [Validation](validation.json): observed checks with environment and scope, separate from editorial review.

Stable IDs identify learning outcomes. Paths are canonical. Status is planned, draft or reviewed; counts exclude planned records. Execution is independent of editorial status. Generate browse pages with `python3 scripts/catalogue.py --write`; validation rejects stale generated pages.

[Engineering hub](../README.md)
