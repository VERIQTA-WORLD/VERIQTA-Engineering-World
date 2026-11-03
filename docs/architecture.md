# Architecture and content plan

VERIQTA Engineering World is an engineering learning library. DevOps is the first populated area; future engineering areas should be introduced only with substantive content. A topic index is not a claim of mastery or coverage completion.

## Canonical architecture

- `journey/`: the DevOps sequence and seven authored daily lessons.
- `library/`: independent canonical items; paths link here rather than copying tasks.
- Answers live in `journey/solutions/`, `library/solutions/`, or the relevant AI section; tasks link to their separate answers.
- `challenges/`: independent mission-based practice; the entry point and initial catalogue currently describe planned scope only.
- `ai/`: AI learning sections with their exercises, examples and solutions.
- Root `README.md`: the learning hub and curated routes linking directly to canonical material.
- `catalogue/`: source records, planned domain expansions and separate execution evidence.
- `docs/`: contributor standards, attribution, roadmap and maintenance information.
- `scripts/`, `tests/`, `.github/`: repository-wide validation, navigation generation and contribution workflows; subject-specific examples and tests stay inside their subject folder.
- `assets/`: repository-owned design and attributed tool marks.

Stable IDs survive title changes. Prefer retaining existing paths; a move requires a small redirect Markdown page and link validation. The root title covers engineering broadly while the first sequence is explicitly DevOps. No separate site or backend is required.

## Development order

Repository skeleton and navigation come first. The requester will choose a root folder before new content filling begins. Complete and review that folder’s coherent sections, then obtain approval before moving to another root folder. The [development plan](section-plan.md) describes intended coverage; it does not authorise automatic progression.

The 100-day journey and existing canonical IDs remain intact. The AI curriculum plan lives inside ai/. The initial challenges catalogue reserves five future missions without creating lesson, fixture or solution placeholders.

Editorial status and runtime validation remain distinct. Planned records do not count as completed activities, and static checks do not establish that a runtime lab works.
