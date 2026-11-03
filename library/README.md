# Engineering practice library

One canonical copy of every activity. Authored entries below are drafts; try the task before viewing its separate solution. No account is needed.

## By topic

[Engineering foundations](#foundations) · [Linux and operating systems](#linux) · [Networking and web protocols](#networking) · [Git and GitHub](#git) · [Bash automation](#bash) · [Python and structured data](#python) · [Cloud foundations](#cloud) · [Builds and continuous delivery](#delivery) · [Containers and Docker](#containers) · [Infrastructure as code](#infrastructure) · [Configuration management](#configuration) · [Kubernetes and Helm](#kubernetes) · [GitOps with Argo CD](#gitops) · [Observability](#observability) · [Site reliability engineering](#reliability) · [Platform engineering](#platform) · [Security and DevSecOps](#security) · [AI for engineering](#ai)

## Foundations

Engineering foundations. Planned expansion: DevOps principles, workflows, evidence, YAML, JSON, APIs and authentication, storage, virtualisation.

- [VW-C001: A green deployment and a failed user request](vw-c001.md) — beginner, 20 min, concept, draft.

## Linux

Linux and operating systems. Planned expansion: Linux, system administration, filesystems, processes, users, permissions.

- [VW-E001: Find the large file without filling a disk](vw-e001.md) — beginner, 35 min, exercise, draft.
- [VW-A001: Challenge an AI Linux disk diagnosis](vw-a001.md) — beginner, 45 min, ai-exercise, draft.

## Networking

Networking and web protocols. Planned expansion: Subnets, routing, DNS, HTTP, TLS, proxies, authentication.

- [VW-C002: Why DNS success does not prove HTTPS health](vw-c002.md) — beginner, 25 min, concept, draft.

## Git

Git and GitHub. Planned expansion: Diffs, conflicts, review, branch protection, original interview practice.

No canonical library item authored yet; this topic remains planned.

## Bash

Bash automation. Planned expansion: Quoting, pipelines, failure handling, shell portability.

No canonical library item authored yet; this topic remains planned.

## Python

Python and structured data. Planned expansion: JSON validation, API clients, tests, packaging.

- [VW-E002: Reject malformed release manifests](vw-e002.md) — beginner, 45 min, exercise, draft.

## Cloud

Cloud foundations. Planned expansion: AWS primary, IAM, VPC, compute, storage, databases, load balancing, resilience, backup, cost, Azure and Google Cloud progressively.

- [VW-A002: Review an AI IAM policy shortcut](vw-a002.md) — intermediate, 45 min, ai-exercise, draft.

## Delivery

Builds and continuous delivery. Planned expansion: Maven, JFrog Artifactory, SonarQube, Jenkins, GitHub Actions, GitLab CI/CD.

- [VW-E003: Review a CI gate before giving it authority](vw-e003.md) — intermediate, 40 min, exercise, draft.
- [VW-I002: A passing pipeline publishes a secret](vw-i002.md) — intermediate, 45 min, incident, draft.
- [VW-D001: Choose a release gate for a small service](vw-d001.md) — intermediate, 40 min, decision, draft.
- [VW-P001: Build a release evidence bundle](vw-p001.md) — intermediate, 150 min, project, draft.

## Containers

Containers and Docker. Planned expansion: Build context, layers, networks, volumes, provenance, image scanning.

- [VW-C003: An image tag is not a release identity](vw-c003.md) — intermediate, 25 min, concept, draft.
- [VW-A003: Test an AI Dockerfile review against build context](vw-a003.md) — intermediate, 45 min, ai-exercise, draft.

## Infrastructure

Infrastructure as code. Planned expansion: Terraform, state, drift, modules, provider constraints, replacement.

- [VW-I003: Replacement hidden inside a small Terraform diff](vw-i003.md) — intermediate, 45 min, incident, draft.

## Configuration

Configuration management. Planned expansion: Ansible, inventory, idempotency, check mode, Packer images.

No canonical library item authored yet; this topic remains planned.

## Kubernetes

Kubernetes and Helm. Planned expansion: Pods, Services, probes, scheduling, Helm, AWS EKS.

- [VW-E004: Render Helm values before approving a change](vw-e004.md) — intermediate, 50 min, exercise, draft.
- [VW-I001: The service with no destinations](vw-i001.md) — beginner, 45 min, incident, draft.
- [VW-A004: Disprove an AI Kubernetes restart explanation](vw-a004.md) — intermediate, 45 min, ai-exercise, draft.

## Gitops

GitOps with Argo CD. Planned expansion: Desired state, drift, reconciliation, sync safety.

No canonical library item authored yet; this topic remains planned.

## Observability

Observability. Planned expansion: Prometheus, Grafana, logs, metrics, traces, OpenTelemetry, alerting.

- [VW-C004: An average can hide an outage](vw-c004.md) — intermediate, 30 min, concept, draft.
- [VW-I004: The error alert that goes quiet during failure](vw-i004.md) — advanced, 45 min, incident, draft.

## Reliability

Site reliability engineering. Planned expansion: SLIs, SLOs, error budgets, incidents, recovery, capacity, distributed systems, databases, queues, caches, published incident studies.

- [VW-D002: Choose a useful first reliability objective](vw-d002.md) — advanced, 45 min, decision, draft.

## Platform

Platform engineering. Planned expansion: Developer experience, self-service, golden paths, documentation discovery.

No canonical library item authored yet; this topic remains planned.

## Security

Security and DevSecOps. Planned expansion: Least privilege, secrets, dependency/image/IaC scanning, CI security, policy as code, threat modelling, supply chain.

No canonical library item authored yet; this topic remains planned.

## Ai

AI for engineering. Planned expansion: Capabilities, context, prompts, structured output, tool calling, RAG, freshness, provenance, read-only tools, permissions, injection, privacy, evaluation, latency, tokens, cost, fallback, audit trails, controlled agents.

- [VW-P002: Build a read-only incident evidence assistant](vw-p002.md) — advanced, 180 min, project, draft.

## By level

### Beginner

- [VW-C001: A green deployment and a failed user request](vw-c001.md)
- [VW-C002: Why DNS success does not prove HTTPS health](vw-c002.md)
- [VW-E001: Find the large file without filling a disk](vw-e001.md)
- [VW-E002: Reject malformed release manifests](vw-e002.md)
- [VW-I001: The service with no destinations](vw-i001.md)
- [VW-A001: Challenge an AI Linux disk diagnosis](vw-a001.md)

### Intermediate

- [VW-C003: An image tag is not a release identity](vw-c003.md)
- [VW-C004: An average can hide an outage](vw-c004.md)
- [VW-E003: Review a CI gate before giving it authority](vw-e003.md)
- [VW-E004: Render Helm values before approving a change](vw-e004.md)
- [VW-I002: A passing pipeline publishes a secret](vw-i002.md)
- [VW-I003: Replacement hidden inside a small Terraform diff](vw-i003.md)
- [VW-A002: Review an AI IAM policy shortcut](vw-a002.md)
- [VW-A003: Test an AI Dockerfile review against build context](vw-a003.md)
- [VW-A004: Disprove an AI Kubernetes restart explanation](vw-a004.md)
- [VW-D001: Choose a release gate for a small service](vw-d001.md)
- [VW-P001: Build a release evidence bundle](vw-p001.md)

### Advanced

- [VW-I004: The error alert that goes quiet during failure](vw-i004.md)
- [VW-D002: Choose a useful first reliability objective](vw-d002.md)
- [VW-P002: Build a read-only incident evidence assistant](vw-p002.md)

## By type

### concept

- [VW-C001: A green deployment and a failed user request](vw-c001.md)
- [VW-C002: Why DNS success does not prove HTTPS health](vw-c002.md)
- [VW-C003: An image tag is not a release identity](vw-c003.md)
- [VW-C004: An average can hide an outage](vw-c004.md)

### exercise

- [VW-E001: Find the large file without filling a disk](vw-e001.md)
- [VW-E002: Reject malformed release manifests](vw-e002.md)
- [VW-E003: Review a CI gate before giving it authority](vw-e003.md)
- [VW-E004: Render Helm values before approving a change](vw-e004.md)

### incident

- [VW-I001: The service with no destinations](vw-i001.md)
- [VW-I002: A passing pipeline publishes a secret](vw-i002.md)
- [VW-I003: Replacement hidden inside a small Terraform diff](vw-i003.md)
- [VW-I004: The error alert that goes quiet during failure](vw-i004.md)

### ai-exercise

- [VW-A001: Challenge an AI Linux disk diagnosis](vw-a001.md)
- [VW-A002: Review an AI IAM policy shortcut](vw-a002.md)
- [VW-A003: Test an AI Dockerfile review against build context](vw-a003.md)
- [VW-A004: Disprove an AI Kubernetes restart explanation](vw-a004.md)

### decision

- [VW-D001: Choose a release gate for a small service](vw-d001.md)
- [VW-D002: Choose a useful first reliability objective](vw-d002.md)

### project

- [VW-P001: Build a release evidence bundle](vw-p001.md)
- [VW-P002: Build a read-only incident evidence assistant](vw-p002.md)

[Learning paths](../paths/README.md) · [Engineering hub](../README.md)
