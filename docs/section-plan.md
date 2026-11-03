# Folder and section development plan

Use this plan to organise coherent learning units within the root folder selected for development. The 100-Day DevOps Journey remains the guided route; these sections also support independent topic study. Existing activities keep their stable IDs and canonical paths.

## How to read the sequence

The requester selects the root folder before content filling. Within that folder, follow prerequisite sections before deeper applications. A planned section describes intended scope; it does not claim that lessons or runtime checks already exist. Existing first-batch activities are starting material to deepen, connect and validate.

Each section is ready for publication when it has a clear scope, sufficient explanations for its prerequisites, an ordered learning route, appropriate practice and complete separate solutions, a checkpoint, working navigation and recorded validation limits. Editorial status remains draft until an independent technical reviewer is recorded. Publication readiness is separate from independent review.

## Foundations and engineering subjects

The numbered order is recommended within each row. Cross-subject prerequisites are stated explicitly.

| Area | Sections in recommended order | Prerequisites and existing material | Section-specific completion evidence |
| --- | --- | --- | --- |
| Engineering foundations | 1. Outcomes and evidence; 2. Safe local environments; 3. Changes, feedback and shared ownership | Begin without technical experience; deepen Day 1 and VW-C001 first, then Days 2–3 and VW-C001's workflow discussion | Explain a user outcome, reproduce a bounded observation and defend a handoff decision |
| Linux and operating systems | 1. Files and permissions; 2. Processes and exit status; 3. Services and logs; 4. Storage and recovery | Safe environments; Days 3–4/6 and VW-E001; Days 8–14 need full lessons | Disposable Linux exercises with failure injection, ownership boundaries and verified cleanup |
| Networking | 1. Addresses and routes; 2. DNS and caching; 3. HTTP and TLS; 4. Layered diagnosis | Basic processes; deepen VW-C002; VW-I005 remains reserved for DNS | Distinguish resolution, connection, trust and application evidence using representative fixtures |
| Git and GitHub | 1. Snapshots and review; 2. Branches and conflicts; 3. Safe undo and collaboration | Safe environments; deepen Day 5; remaining sequence needs canonical practice | Reproduce a conflict resolution and explain preserved intent without rewriting shared history |
| Bash and Python | 1. Shell inputs and failure; 2. Structured data and validation; 3. Testing and bounded automation | Files and Git; deepen Day 6 and VW-E002 | Edge-case tests, predictable exit status and explicit input/output contracts |
| Data and APIs | 1. YAML/JSON contracts; 2. HTTP APIs and authentication; 3. Filesystems and virtualisation boundaries | Scripting and networking; new focused material required | Reject malformed data and explain trust and storage boundaries |
| Cloud | 1. Responsibility, IAM and cost; 2. AWS request paths; 3. Compute/storage/database decisions; 4. Recovery and cost evidence; 5. Azure/GCP comparisons | Networking and data; deepen VW-A002 and link VW-I003 | Offline defaults plus explicit budgets and teardown for any optional cloud labs; no implied free tier |
| Builds and artifacts | 1. Maven build lifecycle; 2. Artifact identity and Artifactory promotion; 3. SonarQube and quality limits | Git and scripting; VW-C003 and VW-P001 bridge this area | Trace inputs through gates to one identifiable artifact; explain what each gate cannot prove |
| Containers | 1. Context, layers and Dockerfiles; 2. Runtime/network/volumes; 3. Reproducibility and supply chain | Linux and builds; deepen VW-C003/VW-A003 and VW-P001 | Actual disposable container checks where available; separate build, runtime and scan evidence |
| CI/CD | 1. Events and trust; 2. GitHub Actions gates; 3. Jenkins/GitLab workflows; 4. Promotion and recovery | Git, scripting and artifacts; VW-E003, VW-I002, VW-D001 | Deliberate failures block promotion; untrusted contributions cannot inherit deployment authority |
| Infrastructure as code | 1. Terraform configuration/state; 2. Plan lifecycle and modules; 3. Drift and recovery | Cloud concepts and Git; VW-I003; VW-A005 reserved | Distinguish address refactors, drift and destructive effects without unsafe apply instructions |
| Configuration management | 1. Ansible desired state; 2. Inventory and idempotency; 3. Check-mode limits and Packer trade-offs | Linux and scripting; VW-E005 reserved; full section missing | Compare first/second runs and check-mode predictions in a disposable scope |
| Kubernetes and Helm | 1. Objects and reconciliation; 2. Services and routing; 3. Config/probes/scheduling; 4. Helm and rollout review; 5. EKS boundaries | Containers and networking; VW-I001, VW-E004, VW-A004 | Rendered-manifest review plus live endpoint/probe checks where available, reported separately |
| GitOps | 1. Desired state and reconciliation; 2. Argo CD sync/drift; 3. Recovery and data compatibility | Git, Kubernetes and infrastructure review; new guided labs needed | Explain an out-of-sync diff and distinguish config revert from data recovery |
| Observability | 1. Questions and signals; 2. Prometheus and missing series; 3. Grafana decisions; 4. OpenTelemetry traces | HTTP and basic services; VW-C004/VW-I004; VW-E006 reserved | Test error, zero-traffic and missing-telemetry cases; dashboards answer a named question |
| SRE and distributed systems | 1. SLIs/SLOs and budgets; 2. Incident response; 3. Backup/restore; 4. Capacity, queues, caches and databases | Evidence section plus observability; VW-D002 and recovery projects | Defined denominators, timed recovery evidence and clear uncertainty; primary-source incident studies |
| Security | 1. Threat modelling and least privilege; 2. Secrets and CI; 3. Scanning/provenance; 4. Policy and remediation | Relevant tool fundamentals; VW-I002/VW-E003/VW-A002 | Scoped remediation, negative-access checks where possible and no credentials in fixtures |
| Platform engineering | 1. Developer journeys; 2. Safe self-service; 3. Documentation discovery and feedback | Delivery, security and reliability; new sections needed | A learner can follow a bounded workflow; record usability friction and operational limits |

## AI curriculum

The authoritative [15-section AI curriculum plan](../ai/ROADMAP.md) lives inside the AI folder. It covers foundations, prompting, verification, tool-specific workflows, retrieval, controlled agents and practical projects.

## Current development boundary

Repository organisation and navigation are the current stage. The [challenges area](../challenges/README.md) contains a purpose statement and five planned entries; no challenge lessons or starter environments are available yet. Existing published material is retained while the skeleton is organised.

A root folder will be selected before further content filling. Its scope will be completed and reviewed, and the requester’s approval is required before moving to another root folder. The section order above is a planning reference, not authorisation to populate multiple areas.
