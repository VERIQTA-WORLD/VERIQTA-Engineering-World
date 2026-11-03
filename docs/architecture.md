# Architecture and content plan

VERIQTA Engineering World is an engineering learning library. DevOps is the first populated area; future engineering areas should be introduced only with substantive content. A topic index is not a claim of mastery or coverage completion.

## Repository inspection

The starting checkout contained only Git metadata: no commits, remotes, tracked content, licence, automation or AGENTS.md. There were no legacy links or uncommitted learner files to migrate. The verified destination is veriqta/VERIQTA-Engineering-World, a public repository with main as its default branch; its initial remote had no refs. No separate repository was created.

## Canonical architecture

- `journey/`: the DevOps sequence and seven authored daily lessons.
- `library/`: independent canonical items; paths link here rather than copying tasks.
- `solutions/`: separate answers to preserve independent practice.
- `ai/` and `paths/`: curated navigation into the same canonical items.
- `catalogue/`: source records, planned domain expansions and separate execution evidence.
- `docs/`: contributor standards, attribution, roadmap and maintenance information.
- `scripts/`, `tests/`, `.github/`: repository validation and contribution workflows.
- `assets/`: repository-owned design and attributed tool marks.

Stable IDs survive title changes. Prefer retaining existing paths; a move requires a small redirect Markdown page and link validation. The root title covers engineering broadly while the first sequence is explicitly DevOps. No separate site or backend is required.

## Delivery order

Milestone 1: 90 mapped days, 7 authored days and 20 distinct canonical library items. Milestone 2: independently review this batch, author Days 8–14 and add the precisely scoped items in the roadmap. Expansion to 50, 200, 500 or 1000 authored items is contingent on review capacity and distinct learning value.

A draft is authored, not reviewed. Planned records do not count as exercises. Execution is tracked independently of editorial review. A successful parser or static check cannot establish a live Kubernetes, cloud or model result.
