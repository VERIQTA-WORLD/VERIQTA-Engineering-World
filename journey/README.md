# 100-Day DevOps Journey

DevOps is one learning area within VERIQTA Engineering World. This is an original introductory sequence. Days 1–7 are available; later days are a complete curriculum plan, not finished lessons. Completion does not automatically establish professional competence.

Allow about 60 minutes daily, with 90-minute final project sessions; repeat days or split activities as needed. AWS is the primary cloud context. Defaults use offline fixtures and local runtimes; paid cloud and real model calls are optional future extensions. Read each authored lesson for supported tools, verification and cleanup.

## Curriculum map

| Day | Focus | Topic | Status |
| --- | --- | --- | --- |
| 1 | [Define an engineering outcome](days/day-01.md) | foundations | Available |
| 2 | [Build a safe learning workspace](days/day-02.md) | foundations | Available |
| 3 | [Navigate files and explain permissions](days/day-03.md) | foundations | Available |
| 4 | [Turn logs into observations](days/day-04.md) | foundations | Available |
| 5 | [Record a change with Git](days/day-05.md) | foundations | Available |
| 6 | [Write a bounded shell check](days/day-06.md) | foundations | Available |
| 7 | [Review the first evidence bundle](days/day-07.md) | foundations | Available |
| 8 | [Processes and exit status](#day-8) | linux | Planned |
| 9 | [Environment variables and configuration](#day-9) | linux | Planned |
| 10 | [Users, groups and least privilege](#day-10) | linux | Planned |
| 11 | [Storage, inodes and filesystem boundaries](#day-11) | linux | Planned |
| 12 | [Service lifecycle and logs](#day-12) | linux | Planned |
| 13 | [Virtual machines and isolation](#day-13) | linux | Planned |
| 14 | [Linux troubleshooting checkpoint](#day-14) | linux | Planned |
| 15 | [Addresses, subnets and routes](#day-15) | networking | Planned |
| 16 | [Ports and TCP connections](#day-16) | networking | Planned |
| 17 | [DNS answers and caching](#day-17) | networking | Planned |
| 18 | [HTTP methods and status semantics](#day-18) | networking | Planned |
| 19 | [TLS identity and trust](#day-19) | networking | Planned |
| 20 | [APIs and authentication boundaries](#day-20) | networking | Planned |
| 21 | [Network troubleshooting review](#day-21) | networking | Planned |
| 22 | [Branches and small reviewable changes](#day-22) | git | Planned |
| 23 | [Resolve a conflict with intent](#day-23) | git | Planned |
| 24 | [GitHub review and issue workflows](#day-24) | git | Planned |
| 25 | [Undo safely and preserve evidence](#day-25) | git | Planned |
| 26 | [Quote inputs and handle failures](#day-26) | bash | Planned |
| 27 | [Compose small command-line tools](#day-27) | bash | Planned |
| 28 | [Python files and structured data](#day-28) | python | Planned |
| 29 | [Validate data before automation](#day-29) | python | Planned |
| 30 | [Test boundary conditions](#day-30) | python | Planned |
| 31 | [Scripted workflow checkpoint](#day-31) | python | Planned |
| 32 | [Cloud responsibility and cost boundaries](#day-32) | cloud | Planned |
| 33 | [AWS identity before resources](#day-33) | cloud | Planned |
| 34 | [AWS networking foundations](#day-34) | cloud | Planned |
| 35 | [Compute and load balancing](#day-35) | cloud | Planned |
| 36 | [Storage and database choices](#day-36) | cloud | Planned |
| 37 | [Availability and recovery objectives](#day-37) | cloud | Planned |
| 38 | [Cloud architecture review](#day-38) | cloud | Planned |
| 39 | [Build inputs and Maven lifecycle](#day-39) | delivery | Planned |
| 40 | [Artifacts and repository promotion](#day-40) | delivery | Planned |
| 41 | [Quality signals and SonarQube limits](#day-41) | delivery | Planned |
| 42 | [Images, layers and context](#day-42) | containers | Planned |
| 43 | [Build a small container locally](#day-43) | containers | Planned |
| 44 | [Container networks and volumes](#day-44) | containers | Planned |
| 45 | [Image identity and scanning](#day-45) | containers | Planned |
| 46 | [Container delivery checkpoint](#day-46) | containers | Planned |
| 47 | [CI events and trust boundaries](#day-47) | delivery | Planned |
| 48 | [GitHub Actions quality gate](#day-48) | delivery | Planned |
| 49 | [Jenkins and GitLab pipeline translation](#day-49) | delivery | Planned |
| 50 | [Promote once and deploy deliberately](#day-50) | delivery | Planned |
| 51 | [Pipeline troubleshooting day](#day-51) | delivery | Planned |
| 52 | [Terraform state and desired configuration](#day-52) | infrastructure | Planned |
| 53 | [Read a plan before applying](#day-53) | infrastructure | Planned |
| 54 | [Variables, modules and provider versions](#day-54) | infrastructure | Planned |
| 55 | [Drift and state safety](#day-55) | infrastructure | Planned |
| 56 | [Infrastructure review checkpoint](#day-56) | infrastructure | Planned |
| 57 | [Ansible inventory and desired state](#day-57) | configuration | Planned |
| 58 | [Check mode and idempotency](#day-58) | configuration | Planned |
| 59 | [Configuration and image trade-offs](#day-59) | configuration | Planned |
| 60 | [The Kubernetes object model](#day-60) | kubernetes | Planned |
| 61 | [Deploy to a disposable local cluster](#day-61) | kubernetes | Planned |
| 62 | [Services and EndpointSlices](#day-62) | kubernetes | Planned |
| 63 | [Configuration and secret boundaries](#day-63) | kubernetes | Planned |
| 64 | [Requests, limits and scheduling](#day-64) | kubernetes | Planned |
| 65 | [Startup, readiness and liveness](#day-65) | kubernetes | Planned |
| 66 | [Helm templates and values](#day-66) | kubernetes | Planned |
| 67 | [Rollouts and Kubernetes troubleshooting](#day-67) | kubernetes | Planned |
| 68 | [Local Kubernetes checkpoint and EKS context](#day-68) | kubernetes | Planned |
| 69 | [Git as reviewed desired state](#day-69) | gitops | Planned |
| 70 | [Argo CD drift and sync safety](#day-70) | gitops | Planned |
| 71 | [GitOps recovery checkpoint](#day-71) | gitops | Planned |
| 72 | [Signals and instrumentation](#day-72) | observability | Planned |
| 73 | [Prometheus counters and rates](#day-73) | observability | Planned |
| 74 | [Grafana dashboards with decisions](#day-74) | observability | Planned |
| 75 | [OpenTelemetry trace context](#day-75) | observability | Planned |
| 76 | [Alert behavior and missing evidence](#day-76) | observability | Planned |
| 77 | [Threat model the delivery path](#day-77) | security | Planned |
| 78 | [Secrets, dependencies and supply chain](#day-78) | security | Planned |
| 79 | [Policy and infrastructure scanning](#day-79) | security | Planned |
| 80 | [Define an SLI and provisional SLO](#day-80) | reliability | Planned |
| 81 | [Incident response and communication](#day-81) | reliability | Planned |
| 82 | [Backups and a restore rehearsal](#day-82) | reliability | Planned |
| 83 | [Capacity and dependency failures](#day-83) | reliability | Planned |
| 84 | [Responsible assistant boundaries](#day-84) | ai | Planned |
| 85 | [Mock-assisted review and evaluation](#day-85) | ai | Planned |
| 86 | [Retrieval and source provenance](#day-86) | ai | Planned |
| 87 | [Controlled tools and failure boundaries](#day-87) | ai | Planned |
| 88 | [Final project architecture checkpoint](#day-88) | reliability | Planned |
| 89 | [Final project delivery evidence](#day-89) | reliability | Planned |
| 90 | [Final project recovery and retrospective](#day-90) | reliability | Planned |
| 91 | [Rehearse the project runbook](#day-91) | reliability | Planned |
| 92 | [Verify configuration convergence](#day-92) | configuration | Planned |
| 93 | [Review a project infrastructure change](#day-93) | infrastructure | Planned |
| 94 | [Trace project artifact provenance](#day-94) | security | Planned |
| 95 | [Test the missing-signal case](#day-95) | observability | Planned |
| 96 | [Check rollback and data compatibility](#day-96) | reliability | Planned |
| 97 | [Evaluate a read-only project assistant](#day-97) | ai | Planned |
| 98 | [Test the learner-to-operator handoff](#day-98) | platform | Planned |
| 99 | [Compare environment assumptions](#day-99) | cloud | Planned |
| 100 | [Demonstrate the project and explain its limits](#day-100) | reliability | Planned |

## Daily scope and outcomes

Days 91–100 build on the integrated project with runbooks, configuration convergence, infrastructure review, provenance, missing-signal tests, recovery, AI evaluation, handoffs, cloud assumptions and a final demonstration.

Planned entries below define learning scope. Full setup, explanations, solutions and runtime validation are authored progressively. For authored days, follow the linked lesson.

### Day 1

**Define an engineering outcome** · Available · 60 minutes

- Outcomes: Distinguish an engineering output from a user outcome. Define a scoped, falsifiable check and a feedback owner.
- Prerequisites: None.
- Focus: A measurable user outcome connects the intended change, observation boundary, result correctness, timing and feedback decision.
- Core task: Map a small service change from request to feedback; identify one user outcome.
- Success: The note defines behavior, eligible requests, observation boundary and window. The feedback map, bounded stop condition and one limitation can be explained without claiming an unrun test succeeded.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md) · [VW-E007](../ai/engineering-evidence/release-evidence.md) · [VW-I006](../ai/engineering-evidence/recovery-scenario.md).
- [Official reference](https://sre.google/sre-book/monitoring-distributed-systems/).

### Day 2

**Build a safe learning workspace** · Available · 60 minutes

- Outcomes: Create a scoped workspace and inventory your local tools without credentials Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY001.
- Focus: This session develops build a safe learning workspace through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Create a scoped workspace and inventory your local tools without credentials.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://sre.google/sre-book/embracing-risk/).

### Day 3

**Navigate files and explain permissions** · Available · 60 minutes

- Outcomes: Create a directory tree; compare file and directory permissions Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY002.
- Focus: This session develops navigate files and explain permissions through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Create a directory tree; compare file and directory permissions.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://sre.google/sre-book/embracing-risk/).

### Day 4

**Turn logs into observations** · Available · 60 minutes

- Outcomes: Filter a tiny log fixture and separate observations from hypotheses Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY003.
- Focus: This session develops turn logs into observations through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Filter a tiny log fixture and separate observations from hypotheses.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://sre.google/sre-book/embracing-risk/).

### Day 5

**Record a change with Git** · Available · 60 minutes

- Outcomes: Create and inspect two local commits in a disposable repository Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY004.
- Focus: This session develops record a change with git through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Create and inspect two local commits in a disposable repository.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://sre.google/sre-book/embracing-risk/).

### Day 6

**Write a bounded shell check** · Available · 60 minutes

- Outcomes: Write a script that checks one file and returns meaningful exit codes Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY005.
- Focus: This session develops write a bounded shell check through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Write a script that checks one file and returns meaningful exit codes.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://sre.google/sre-book/embracing-risk/).

### Day 7

**Review the first evidence bundle** · Available · 60 minutes

- Outcomes: Investigate a broken handoff using your workspace, Git and shell evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY006.
- Focus: This session develops review the first evidence bundle through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Investigate a broken handoff using your workspace, Git and shell evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://sre.google/sre-book/embracing-risk/).

### Day 8

**Processes and exit status** · Planned · 60 minutes

- Outcomes: Start a disposable process and capture its exit status Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY007.
- Focus: This session develops processes and exit status through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Start a disposable process and capture its exit status.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E001](../library/vw-e001.md).
- [Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html).

### Day 9

**Environment variables and configuration** · Planned · 60 minutes

- Outcomes: Compare a process environment with explicit configuration Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY008.
- Focus: This session develops environment variables and configuration through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare a process environment with explicit configuration.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E001](../library/vw-e001.md).
- [Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html).

### Day 10

**Users, groups and least privilege** · Planned · 60 minutes

- Outcomes: Design a service account permission table without changing host users Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY009.
- Focus: This session develops users, groups and least privilege through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Design a service account permission table without changing host users.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E001](../library/vw-e001.md).
- [Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html).

### Day 11

**Storage, inodes and filesystem boundaries** · Planned · 60 minutes

- Outcomes: Compare directory size, filesystem capacity and inode evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY010.
- Focus: This session develops storage, inodes and filesystem boundaries through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare directory size, filesystem capacity and inode evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E001](../library/vw-e001.md).
- [Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html).

### Day 12

**Service lifecycle and logs** · Planned · 60 minutes

- Outcomes: Read a simulated systemd unit and match failure logs to restart behavior Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY011.
- Focus: This session develops service lifecycle and logs through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Read a simulated systemd unit and match failure logs to restart behavior.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E001](../library/vw-e001.md).
- [Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html).

### Day 13

**Virtual machines and isolation** · Planned · 60 minutes

- Outcomes: Compare VM, process and container isolation for a lab workload Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY012.
- Focus: This session develops virtual machines and isolation through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare VM, process and container isolation for a lab workload.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E001](../library/vw-e001.md).
- [Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html).

### Day 14

**Linux troubleshooting checkpoint** · Planned · 60 minutes

- Outcomes: Diagnose a simulated full-disk service failure from bounded evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY013.
- Focus: This session develops linux troubleshooting checkpoint through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Diagnose a simulated full-disk service failure from bounded evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E001](../library/vw-e001.md).
- [Official reference](https://www.gnu.org/software/coreutils/manual/coreutils.html).

### Day 15

**Addresses, subnets and routes** · Planned · 60 minutes

- Outcomes: Trace a sample packet through a documented subnet and route table Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY014.
- Focus: This session develops addresses, subnets and routes through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Trace a sample packet through a documented subnet and route table.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C002](../library/vw-c002.md).
- [Official reference](https://curl.se/docs/manpage.html).

### Day 16

**Ports and TCP connections** · Planned · 60 minutes

- Outcomes: Compare listener, timeout and refused-connection evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY015.
- Focus: This session develops ports and tcp connections through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare listener, timeout and refused-connection evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C002](../library/vw-c002.md).
- [Official reference](https://curl.se/docs/manpage.html).

### Day 17

**DNS answers and caching** · Planned · 60 minutes

- Outcomes: Compare supplied resolver answers and TTLs across two environments Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY016.
- Focus: This session develops dns answers and caching through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare supplied resolver answers and TTLs across two environments.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C002](../library/vw-c002.md).
- [Official reference](https://curl.se/docs/manpage.html).

### Day 18

**HTTP methods and status semantics** · Planned · 60 minutes

- Outcomes: Classify sample HTTP requests by safety, idempotency and response meaning Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY017.
- Focus: This session develops http methods and status semantics through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Classify sample HTTP requests by safety, idempotency and response meaning.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C002](../library/vw-c002.md).
- [Official reference](https://curl.se/docs/manpage.html).

### Day 19

**TLS identity and trust** · Planned · 60 minutes

- Outcomes: Inspect a sanitised certificate summary for hostname and expiry errors Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY018.
- Focus: This session develops tls identity and trust through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Inspect a sanitised certificate summary for hostname and expiry errors.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C002](../library/vw-c002.md).
- [Official reference](https://curl.se/docs/manpage.html).

### Day 20

**APIs and authentication boundaries** · Planned · 60 minutes

- Outcomes: Design a scoped token exchange and redact a sample request Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY019.
- Focus: This session develops apis and authentication boundaries through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Design a scoped token exchange and redact a sample request.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C002](../library/vw-c002.md).
- [Official reference](https://curl.se/docs/manpage.html).

### Day 21

**Network troubleshooting review** · Planned · 60 minutes

- Outcomes: Locate the failing request boundary from DNS, TLS and HTTP evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY020.
- Focus: This session develops network troubleshooting review through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Locate the failing request boundary from DNS, TLS and HTTP evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C002](../library/vw-c002.md).
- [Official reference](https://curl.se/docs/manpage.html).

### Day 22

**Branches and small reviewable changes** · Planned · 60 minutes

- Outcomes: Create two disposable branches and compare diffs Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY021.
- Focus: This session develops branches and small reviewable changes through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Create two disposable branches and compare diffs.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://git-scm.com/docs/gittutorial).

### Day 23

**Resolve a conflict with intent** · Planned · 60 minutes

- Outcomes: Resolve a local conflict while preserving both stated requirements Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY022.
- Focus: This session develops resolve a conflict with intent through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Resolve a local conflict while preserving both stated requirements.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://git-scm.com/docs/gittutorial).

### Day 24

**GitHub review and issue workflows** · Planned · 60 minutes

- Outcomes: Draft a review checklist and an actionable issue offline Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY023.
- Focus: This session develops github review and issue workflows through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Draft a review checklist and an actionable issue offline.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://git-scm.com/docs/gittutorial).

### Day 25

**Undo safely and preserve evidence** · Planned · 60 minutes

- Outcomes: Compare revert, restore and reset in a disposable repository Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY024.
- Focus: This session develops undo safely and preserve evidence through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare revert, restore and reset in a disposable repository.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C001](../library/vw-c001.md).
- [Official reference](https://git-scm.com/docs/gittutorial).

### Day 26

**Quote inputs and handle failures** · Planned · 60 minutes

- Outcomes: Test a script with spaces, empty input and failed commands Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY025.
- Focus: This session develops quote inputs and handle failures through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Test a script with spaces, empty input and failed commands.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E002](../library/vw-e002.md).
- [Official reference](https://www.gnu.org/software/bash/manual/bash.html).

### Day 27

**Compose small command-line tools** · Planned · 60 minutes

- Outcomes: Transform a fixture with explicit pipeline failure handling Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY026.
- Focus: This session develops compose small command-line tools through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Transform a fixture with explicit pipeline failure handling.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E002](../library/vw-e002.md).
- [Official reference](https://www.gnu.org/software/bash/manual/bash.html).

### Day 28

**Python files and structured data** · Planned · 60 minutes

- Outcomes: Parse a small JSON fixture and report selected fields Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY027.
- Focus: This session develops python files and structured data through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Parse a small JSON fixture and report selected fields.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E002](../library/vw-e002.md).
- [Official reference](https://docs.python.org/3/library/unittest.html).

### Day 29

**Validate data before automation** · Planned · 60 minutes

- Outcomes: Reject invalid types and missing fields with useful exit codes Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY028.
- Focus: This session develops validate data before automation through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Reject invalid types and missing fields with useful exit codes.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E002](../library/vw-e002.md).
- [Official reference](https://docs.python.org/3/library/unittest.html).

### Day 30

**Test boundary conditions** · Planned · 60 minutes

- Outcomes: Write tests for empty, malformed and unexpected input Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY029.
- Focus: This session develops test boundary conditions through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Write tests for empty, malformed and unexpected input.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E002](../library/vw-e002.md).
- [Official reference](https://docs.python.org/3/library/unittest.html).

### Day 31

**Scripted workflow checkpoint** · Planned · 60 minutes

- Outcomes: Combine shell and Python into a local evidence collection task Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY030.
- Focus: This session develops scripted workflow checkpoint through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Combine shell and Python into a local evidence collection task.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E002](../library/vw-e002.md).
- [Official reference](https://docs.python.org/3/library/unittest.html).

### Day 32

**Cloud responsibility and cost boundaries** · Planned · 60 minutes

- Outcomes: Map customer/provider responsibilities and write a no-spend lab plan Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY031.
- Focus: This session develops cloud responsibility and cost boundaries through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Map customer/provider responsibilities and write a no-spend lab plan.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 33

**AWS identity before resources** · Planned · 60 minutes

- Outcomes: Review an example IAM policy for unnecessary authority Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY032.
- Focus: This session develops aws identity before resources through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Review an example IAM policy for unnecessary authority.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 34

**AWS networking foundations** · Planned · 60 minutes

- Outcomes: Draw a VPC request path with subnet, route and security group boundaries Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY033.
- Focus: This session develops aws networking foundations through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Draw a VPC request path with subnet, route and security group boundaries.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 35

**Compute and load balancing** · Planned · 60 minutes

- Outcomes: Compare a single instance and a load-balanced service against requirements Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY034.
- Focus: This session develops compute and load balancing through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare a single instance and a load-balanced service against requirements.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 36

**Storage and database choices** · Planned · 60 minutes

- Outcomes: Choose storage semantics and backup requirements for a sample service Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY035.
- Focus: This session develops storage and database choices through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Choose storage semantics and backup requirements for a sample service.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 37

**Availability and recovery objectives** · Planned · 60 minutes

- Outcomes: Define acceptable loss and recovery time for a fictional workload Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY036.
- Focus: This session develops availability and recovery objectives through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Define acceptable loss and recovery time for a fictional workload.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 38

**Cloud architecture review** · Planned · 60 minutes

- Outcomes: Review a costed fictional AWS design; compare Azure and GCP terminology Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY037.
- Focus: This session develops cloud architecture review through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Review a costed fictional AWS design; compare Azure and GCP terminology.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 39

**Build inputs and Maven lifecycle** · Planned · 60 minutes

- Outcomes: Trace source through compile, test and package using a sample POM Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY038.
- Focus: This session develops build inputs and maven lifecycle through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Trace source through compile, test and package using a sample POM.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 40

**Artifacts and repository promotion** · Planned · 60 minutes

- Outcomes: Design versioning and promotion in an Artifactory-style repository Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY039.
- Focus: This session develops artifacts and repository promotion through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Design versioning and promotion in an Artifactory-style repository.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 41

**Quality signals and SonarQube limits** · Planned · 60 minutes

- Outcomes: Distinguish static quality findings from runtime correctness Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY040.
- Focus: This session develops quality signals and sonarqube limits through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Distinguish static quality findings from runtime correctness.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 42

**Images, layers and context** · Planned · 60 minutes

- Outcomes: Review a Docker build context for accidental secret inclusion Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY041.
- Focus: This session develops images, layers and context through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Review a Docker build context for accidental secret inclusion.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C003](../library/vw-c003.md).
- [Official reference](https://docs.docker.com/build/building/best-practices/).

### Day 43

**Build a small container locally** · Planned · 60 minutes

- Outcomes: Build a reviewed local service image and record runtime/version evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY042.
- Focus: This session develops build a small container locally through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Build a reviewed local service image and record runtime/version evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C003](../library/vw-c003.md).
- [Official reference](https://docs.docker.com/build/building/best-practices/).

### Day 44

**Container networks and volumes** · Planned · 60 minutes

- Outcomes: Test persistence and connectivity in a disposable local setup Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY043.
- Focus: This session develops container networks and volumes through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Test persistence and connectivity in a disposable local setup.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C003](../library/vw-c003.md).
- [Official reference](https://docs.docker.com/build/building/best-practices/).

### Day 45

**Image identity and scanning** · Planned · 60 minutes

- Outcomes: Compare tag, digest, provenance and vulnerability evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY044.
- Focus: This session develops image identity and scanning through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare tag, digest, provenance and vulnerability evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C003](../library/vw-c003.md).
- [Official reference](https://docs.docker.com/build/building/best-practices/).

### Day 46

**Container delivery checkpoint** · Planned · 60 minutes

- Outcomes: Reproduce a candidate container release and document rollback limits Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY045.
- Focus: This session develops container delivery checkpoint through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Reproduce a candidate container release and document rollback limits.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C003](../library/vw-c003.md).
- [Official reference](https://docs.docker.com/build/building/best-practices/).

### Day 47

**CI events and trust boundaries** · Planned · 60 minutes

- Outcomes: Compare fork PR and trusted deployment contexts Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY046.
- Focus: This session develops ci events and trust boundaries through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare fork PR and trusted deployment contexts.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 48

**GitHub Actions quality gate** · Planned · 60 minutes

- Outcomes: Add deterministic tests to a disposable workflow with minimal permissions Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY047.
- Focus: This session develops github actions quality gate through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Add deterministic tests to a disposable workflow with minimal permissions.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 49

**Jenkins and GitLab pipeline translation** · Planned · 60 minutes

- Outcomes: Translate stage intent without assuming identical security models Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY048.
- Focus: This session develops jenkins and gitlab pipeline translation through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Translate stage intent without assuming identical security models.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 50

**Promote once and deploy deliberately** · Planned · 60 minutes

- Outcomes: Record source, artifact and configuration identity for promotion Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY049.
- Focus: This session develops promote once and deploy deliberately through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Record source, artifact and configuration identity for promotion.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 51

**Pipeline troubleshooting day** · Planned · 60 minutes

- Outcomes: Diagnose a false-green pipeline and leaked fake sentinel Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY050.
- Focus: This session develops pipeline troubleshooting day through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Diagnose a false-green pipeline and leaked fake sentinel.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 52

**Terraform state and desired configuration** · Planned · 60 minutes

- Outcomes: Explain resource addresses and inspect a sanitised state summary Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY051.
- Focus: This session develops terraform state and desired configuration through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Explain resource addresses and inspect a sanitised state summary.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://developer.hashicorp.com/terraform/cli/commands/plan).

### Day 53

**Read a plan before applying** · Planned · 60 minutes

- Outcomes: Classify add, update, replace and destroy effects in a fixture Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY052.
- Focus: This session develops read a plan before applying through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Classify add, update, replace and destroy effects in a fixture.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://developer.hashicorp.com/terraform/cli/commands/plan).

### Day 54

**Variables, modules and provider versions** · Planned · 60 minutes

- Outcomes: Design a small reusable interface with pinned constraints Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY053.
- Focus: This session develops variables, modules and provider versions through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Design a small reusable interface with pinned constraints.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://developer.hashicorp.com/terraform/cli/commands/plan).

### Day 55

**Drift and state safety** · Planned · 60 minutes

- Outcomes: Distinguish config changes, drift and address refactors in plan evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY054.
- Focus: This session develops drift and state safety through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Distinguish config changes, drift and address refactors in plan evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://developer.hashicorp.com/terraform/cli/commands/plan).

### Day 56

**Infrastructure review checkpoint** · Planned · 60 minutes

- Outcomes: Approve or reject a fictional stateful replacement with explicit evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY055.
- Focus: This session develops infrastructure review checkpoint through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Approve or reject a fictional stateful replacement with explicit evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://developer.hashicorp.com/terraform/cli/commands/plan).

### Day 57

**Ansible inventory and desired state** · Planned · 60 minutes

- Outcomes: Review a local-only inventory and an idempotent file task Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY056.
- Focus: This session develops ansible inventory and desired state through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Review a local-only inventory and an idempotent file task.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html).

### Day 58

**Check mode and idempotency** · Planned · 60 minutes

- Outcomes: Predict first and second run changes; identify check-mode limitations Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY057.
- Focus: This session develops check mode and idempotency through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Predict first and second run changes; identify check-mode limitations.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html).

### Day 59

**Configuration and image trade-offs** · Planned · 60 minutes

- Outcomes: Compare Ansible convergence with a Packer image pipeline Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY058.
- Focus: This session develops configuration and image trade-offs through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compare Ansible convergence with a Packer image pipeline.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_checkmode.html).

### Day 60

**The Kubernetes object model** · Planned · 60 minutes

- Outcomes: Connect desired state, controllers and observed status Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY059.
- Focus: This session develops the kubernetes object model through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Connect desired state, controllers and observed status.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 61

**Deploy to a disposable local cluster** · Planned · 60 minutes

- Outcomes: Deploy a small reviewed app in a dedicated local namespace Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY060.
- Focus: This session develops deploy to a disposable local cluster through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Deploy a small reviewed app in a dedicated local namespace.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 62

**Services and EndpointSlices** · Planned · 60 minutes

- Outcomes: Verify selector matching and ready endpoints Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY061.
- Focus: This session develops services and endpointslices through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Verify selector matching and ready endpoints.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 63

**Configuration and secret boundaries** · Planned · 60 minutes

- Outcomes: Separate nonsecret config from secret references and access controls Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY062.
- Focus: This session develops configuration and secret boundaries through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Separate nonsecret config from secret references and access controls.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 64

**Requests, limits and scheduling** · Planned · 60 minutes

- Outcomes: Explain a Pending pod using node and resource evidence Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY063.
- Focus: This session develops requests, limits and scheduling through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Explain a Pending pod using node and resource evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 65

**Startup, readiness and liveness** · Planned · 60 minutes

- Outcomes: Test a slow-start scenario without hiding a stuck process Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY064.
- Focus: This session develops startup, readiness and liveness through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Test a slow-start scenario without hiding a stuck process.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 66

**Helm templates and values** · Planned · 60 minutes

- Outcomes: Render a chart and check selectors and ports before applying Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY065.
- Focus: This session develops helm templates and values through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Render a chart and check selectors and ports before applying.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 67

**Rollouts and Kubernetes troubleshooting** · Planned · 60 minutes

- Outcomes: Investigate a failed rollout and verify a bounded recovery Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY066.
- Focus: This session develops rollouts and kubernetes troubleshooting through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Investigate a failed rollout and verify a bounded recovery.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 68

**Local Kubernetes checkpoint and EKS context** · Planned · 60 minutes

- Outcomes: Package local evidence and identify managed-control-plane differences Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY067.
- Focus: This session develops local kubernetes checkpoint and eks context through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Package local evidence and identify managed-control-plane differences.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://kubernetes.io/docs/concepts/services-networking/service/).

### Day 69

**Git as reviewed desired state** · Planned · 60 minutes

- Outcomes: Separate artifact build, config change and reconciliation Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY068.
- Focus: This session develops git as reviewed desired state through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Separate artifact build, config change and reconciliation.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/).

### Day 70

**Argo CD drift and sync safety** · Planned · 60 minutes

- Outcomes: Interpret a fictional out-of-sync diff before choosing recovery Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY069.
- Focus: This session develops argo cd drift and sync safety through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Interpret a fictional out-of-sync diff before choosing recovery.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/).

### Day 71

**GitOps recovery checkpoint** · Planned · 60 minutes

- Outcomes: Explain revert, reconciliation and data compatibility limits Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY070.
- Focus: This session develops gitops recovery checkpoint through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Explain revert, reconciliation and data compatibility limits.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I001](../library/vw-i001.md).
- [Official reference](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-options/).

### Day 72

**Signals and instrumentation** · Planned · 60 minutes

- Outcomes: Choose logs, metrics and traces for a specific user failure Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY071.
- Focus: This session develops signals and instrumentation through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Choose logs, metrics and traces for a specific user failure.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C004](../library/vw-c004.md).
- [Official reference](https://prometheus.io/docs/prometheus/latest/querying/basics/).

### Day 73

**Prometheus counters and rates** · Planned · 60 minutes

- Outcomes: Interpret counter reset and aggregation using fixture data Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY072.
- Focus: This session develops prometheus counters and rates through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Interpret counter reset and aggregation using fixture data.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C004](../library/vw-c004.md).
- [Official reference](https://prometheus.io/docs/prometheus/latest/querying/basics/).

### Day 74

**Grafana dashboards with decisions** · Planned · 60 minutes

- Outcomes: Design panels that answer an operational question Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY073.
- Focus: This session develops grafana dashboards with decisions through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Design panels that answer an operational question.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C004](../library/vw-c004.md).
- [Official reference](https://prometheus.io/docs/prometheus/latest/querying/basics/).

### Day 75

**OpenTelemetry trace context** · Planned · 60 minutes

- Outcomes: Find a missing span boundary in a sanitised trace Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY074.
- Focus: This session develops opentelemetry trace context through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Find a missing span boundary in a sanitised trace.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C004](../library/vw-c004.md).
- [Official reference](https://prometheus.io/docs/prometheus/latest/querying/basics/).

### Day 76

**Alert behavior and missing evidence** · Planned · 60 minutes

- Outcomes: Test error, zero-traffic and missing-telemetry cases Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY075.
- Focus: This session develops alert behavior and missing evidence through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Test error, zero-traffic and missing-telemetry cases.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C004](../library/vw-c004.md).
- [Official reference](https://prometheus.io/docs/prometheus/latest/querying/basics/).

### Day 77

**Threat model the delivery path** · Planned · 60 minutes

- Outcomes: Identify assets, actors and trust boundaries for the lab Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY076.
- Focus: This session develops threat model the delivery path through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Identify assets, actors and trust boundaries for the lab.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I002](../library/vw-i002.md).
- [Official reference](https://owasp.org/www-project-top-ten/).

### Day 78

**Secrets, dependencies and supply chain** · Planned · 60 minutes

- Outcomes: Review a secret-handling and artifact-provenance checklist Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY077.
- Focus: This session develops secrets, dependencies and supply chain through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Review a secret-handling and artifact-provenance checklist.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I002](../library/vw-i002.md).
- [Official reference](https://owasp.org/www-project-top-ten/).

### Day 79

**Policy and infrastructure scanning** · Planned · 60 minutes

- Outcomes: Separate scanner findings, policy decisions and risk acceptance Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY078.
- Focus: This session develops policy and infrastructure scanning through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Separate scanner findings, policy decisions and risk acceptance.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I002](../library/vw-i002.md).
- [Official reference](https://owasp.org/www-project-top-ten/).

### Day 80

**Define an SLI and provisional SLO** · Planned · 60 minutes

- Outcomes: Compute a request-based budget with explicit eligibility Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY079.
- Focus: This session develops define an sli and provisional slo through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Compute a request-based budget with explicit eligibility.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 81

**Incident response and communication** · Planned · 60 minutes

- Outcomes: Draft a factual timeline and recovery decision log Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY080.
- Focus: This session develops incident response and communication through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Draft a factual timeline and recovery decision log.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 82

**Backups and a restore rehearsal** · Planned · 60 minutes

- Outcomes: Restore a tiny local dataset and verify integrity and app readability Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY081.
- Focus: This session develops backups and a restore rehearsal through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Restore a tiny local dataset and verify integrity and app readability.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 83

**Capacity and dependency failures** · Planned · 60 minutes

- Outcomes: Reason about queue growth, cache loss and database saturation Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY082.
- Focus: This session develops capacity and dependency failures through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Reason about queue growth, cache loss and database saturation.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 84

**Responsible assistant boundaries** · Planned · 60 minutes

- Outcomes: Evaluate an evidence-grounded response and reject injected instructions Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY083.
- Focus: This session develops responsible assistant boundaries through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Evaluate an evidence-grounded response and reject injected instructions.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-P002](../library/vw-p002.md).
- [Official reference](https://www.nist.gov/itl/ai-risk-management-framework).

### Day 85

**Mock-assisted review and evaluation** · Planned · 60 minutes

- Outcomes: Test structured outputs, timeout fallback and unsupported citations Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY084.
- Focus: This session develops mock-assisted review and evaluation through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Test structured outputs, timeout fallback and unsupported citations.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-P002](../library/vw-p002.md).
- [Official reference](https://www.nist.gov/itl/ai-risk-management-framework).

### Day 86

**Retrieval and source provenance** · Planned · 60 minutes

- Outcomes: Retrieve approved runbook passages and verify each evidence citation Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY085.
- Focus: This session develops retrieval and source provenance through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Retrieve approved runbook passages and verify each evidence citation.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-P002](../library/vw-p002.md).
- [Official reference](https://www.nist.gov/itl/ai-risk-management-framework).

### Day 87

**Controlled tools and failure boundaries** · Planned · 60 minutes

- Outcomes: Design read-only tool permissions, approval boundaries and an audit record Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY086.
- Focus: This session develops controlled tools and failure boundaries through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Design read-only tool permissions, approval boundaries and an audit record.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-P002](../library/vw-p002.md).
- [Official reference](https://www.nist.gov/itl/ai-risk-management-framework).

### Day 88

**Final project architecture checkpoint** · Planned · 90 minutes

- Outcomes: Specify a small delivery system, acceptance criteria and cost boundaries Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY087.
- Focus: This session develops final project architecture checkpoint through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Specify a small delivery system, acceptance criteria and cost boundaries.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 89

**Final project delivery evidence** · Planned · 90 minutes

- Outcomes: Assemble source, tests, artifact, configuration and deployment records Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY088.
- Focus: This session develops final project delivery evidence through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Assemble source, tests, artifact, configuration and deployment records.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 90

**Final project recovery and retrospective** · Planned · 90 minutes

- Outcomes: Demonstrate a bounded failure, recovery and honest portfolio limitations Explain the evidence and one limitation of the result.
- Prerequisites: VW-DAY089.
- Focus: This session develops final project recovery and retrospective through one bounded engineering decision. The task focuses on observable evidence rather than product memorisation.
- Core task: Demonstrate a bounded failure, recovery and honest portfolio limitations.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 91

**Rehearse the project runbook** · Planned · 60 minutes

- Outcomes: Walk through detection, triage, recovery and escalation using your integrated project evidence. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY090.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Walk through detection, triage, recovery and escalation using your integrated project evidence.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 92

**Verify configuration convergence** · Planned · 60 minutes

- Outcomes: Compare first and second local configuration runs; document any non-idempotent task. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY091.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Compare first and second local configuration runs; document any non-idempotent task.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-E003](../library/vw-e003.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 93

**Review a project infrastructure change** · Planned · 60 minutes

- Outcomes: Review a sanitised infrastructure plan and identify stateful lifecycle effects before approval. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY092.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Review a sanitised infrastructure plan and identify stateful lifecycle effects before approval.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I003](../library/vw-i003.md).
- [Official reference](https://developer.hashicorp.com/terraform/cli/commands/plan).

### Day 94

**Trace project artifact provenance** · Planned · 60 minutes

- Outcomes: Connect source revision, test result and artifact identity; identify one unverified supply-chain assumption. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY093.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Connect source revision, test result and artifact identity; identify one unverified supply-chain assumption.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-C003](../library/vw-c003.md).
- [Official reference](https://docs.docker.com/build/building/best-practices/).

### Day 95

**Test the missing-signal case** · Planned · 60 minutes

- Outcomes: Replay an offline telemetry-loss fixture and specify how the project detects unknown health. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY094.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Replay an offline telemetry-loss fixture and specify how the project detects unknown health.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-I004](../library/vw-i004.md).
- [Official reference](https://prometheus.io/docs/prometheus/latest/querying/basics/).

### Day 96

**Check rollback and data compatibility** · Planned · 60 minutes

- Outcomes: Test a tiny local data restore and explain why code rollback alone may not recover a service. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY095.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Test a tiny local data restore and explain why code rollback alone may not recover a service.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-D002](../library/vw-d002.md).
- [Official reference](https://sre.google/workbook/incident-response/).

### Day 97

**Evaluate a read-only project assistant** · Planned · 60 minutes

- Outcomes: Score mocked suggestions against project evidence, injected instructions and a no-answer case. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY096.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Score mocked suggestions against project evidence, injected instructions and a no-answer case.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-P002](../library/vw-p002.md).
- [Official reference](https://www.nist.gov/itl/ai-risk-management-framework).

### Day 98

**Test the learner-to-operator handoff** · Planned · 60 minutes

- Outcomes: Ask a peer to follow a bounded project runbook or self-audit it from a clean local directory. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY097.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Ask a peer to follow a bounded project runbook or self-audit it from a clean local directory.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-P001](../library/vw-p001.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

### Day 99

**Compare environment assumptions** · Planned · 60 minutes

- Outcomes: Map your AWS-context design to Azure and Google Cloud concepts without claiming equivalent services or provisioning resources. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY098.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Map your AWS-context design to Azure and Google Cloud concepts without claiming equivalent services or provisioning resources.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-A002](../library/vw-a002.md).
- [Official reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

### Day 100

**Demonstrate the project and explain its limits** · Planned · 90 minutes

- Outcomes: Present a reproducible evidence bundle, one failure/recovery result and a candid final retrospective. Explain which claims your evidence supports and what remains untested.
- Prerequisites: VW-DAY099.
- Focus: This project verification session strengthens one operational boundary using a small local task or an offline evidence review.
- Core task: Present a reproducible evidence bundle, one failure/recovery result and a candid final retrospective.
- Success: A saved observation or artifact demonstrates the stated task. The evidence record includes environment, result and a limitation.
- Reflection: What is established by your evidence? What would you test next, and why?
- Related practice: [VW-P001](../library/vw-p001.md).
- [Official reference](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions).

[Engineering hub](../README.md) · [Learning paths](../README.md#learning-paths)
