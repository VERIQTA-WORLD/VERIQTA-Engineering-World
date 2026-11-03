# Roadmap and section development

The library grows by useful outcomes, not file count. Planned records are not completed exercises. The [domain backlog](../catalogue/backlog.json) covers the requested ecosystem without empty product folders.

## Section sequence takes precedence

Follow the [section development plan](section-plan.md), completing and publishing one coherent section before requesting approval for the next. The [Engineering outcomes and evidence](../ai/engineering-evidence/README.md) section is the first developed unit; Safe local learning environments is next. The older batch proposals below remain future work, not authority to start multiple sections.

## Future work after the prerequisite sections

| Priority | Deliverable | Acceptance and prerequisite |
| --- | --- | --- |
| P0 | Independent technical review of authored material, section by section | Name reviewer/date; resolve incorrect reasoning; retain execution scope |
| P0 | Establish a private conduct/security contact | Verified private reporting route; retain MIT terms and separate asset notices |
| P1 | Author Days 8–14 | Processes, environment, users, storage, service lifecycle, VMs and Linux checkpoint; each with solution and safe cleanup |
| P1 | VW-E005: Ansible local idempotency lab | Disposable local directory; first run changes, second run unchanged; document check-mode gaps |
| P1 | VW-A005: Terraform plan review | Sanitised JSON with replacement and drift; reject an AI “safe apply” claim; no provider calls |
| P1 | VW-E006: Prometheus rule-test lab | Local promtool fixtures for errors, zero traffic and absent series; record exact runtime version |
| P1 | VW-I005: DNS cache divergence | Two resolver fixtures, TTL timeline and alternative hypotheses; separate solution |
| P1 | VW-P003: Linux service deployment | Disposable Linux VM only; service account, listener, failure injection and verified teardown |
| P2 | Tool-specific AI reviews | Git conflict, Bash/Python boundaries, Jenkins/GitLab failure, Ansible idempotency, Helm renders, Argo sync, PromQL, Grafana gaps and OpenTelemetry traces |
| P2 | Evidence-based published incident study | Primary public report, facts/adaptations split, no invented private details |
| P2 | Original interview practice and operational runbook | Explained reasoning and bounded commands; no unsupported employer provenance |

The five reserved library additions above would add five distinct items, subject to their prerequisite sections and review. Add their records only when substantive pages exist. Their IDs are reserved here; do not repurpose them.

## Connected project pipeline

| Planned project | Milestones | Acceptance, cleanup and portfolio evidence |
| --- | --- | --- |
| Linux service | Account → service → logs → failure injection | Bounded HTTP verification; remove only lab VM; show lifecycle decisions |
| Container delivery | Source → image → runtime → rollback | Same image identity across runs; remove lab images; explain context handling |
| CI with quality/security | Tests → Maven build → SonarQube/scanner signals → artifact | Deliberate failure blocks promotion; dispose runner; explain gate limitations |
| Terraform change review | Interface → plan → peer review → recovery evidence | No unexpected destroy; optional cloud budget/teardown; show plan decisions |
| Ansible convergence | Inventory → tasks → first/second run → check mode | Idempotent second run; restore lab state; show module behavior |
| Helm deployment | Values → render → local deploy → probes | Endpoints and requests pass; delete namespace; show label/probe reasoning |
| GitOps delivery | Config PR → Argo diff → sync → recovery | Explain drift and data compatibility; remove lab app; retain audit trail |
| Observability improvement | Instrument → query → dashboard → alert tests | Detect supplied failures/missing telemetry; remove lab stack; explain signal choice |
| Backup/recovery | Tiny dataset → backup → restore → integrity/app check | Meet stated loss/time goals; remove fixture copies; report measured duration |
| AI configuration reviewer | Sanitised input → structured output → tests → fallback | Reject excessive permissions and invented facts; delete unreviewed data; report case results |
| Integrated DevOps project | Architecture → delivery → infrastructure → operations → recovery | Explain every acceptance claim, cost boundary and teardown; no copied-solution ownership claims |

The [release evidence project](../library/vw-p001.md) and [read-only assistant project](../library/vw-p002.md) are authored starting points. The table is a project roadmap, not eleven finished project specifications; detailed requirements, constraints and architecture must be authored before promotion to draft.

## Growth gates

At 50 authored items, require coherent coverage and a completed review queue. Expand toward 200, 500 and 1000 only with maintainers able to validate and revisit material. Azure and Google Cloud follow AWS foundations progressively; advanced distributed systems, platform engineering and controlled agents remain wider-library work rather than being crammed into the introductory journey.
