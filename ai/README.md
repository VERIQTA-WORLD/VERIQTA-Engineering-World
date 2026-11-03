# AI for Engineering and DevOps

Use AI to support investigation, automation and configuration review while independently checking its work. Start offline with sanitised evidence and mocked responses; an account, paid API and real credentials are unnecessary.

## Choose a practice

| Tool or workflow | Authored exercise | Independent check |
| --- | --- | --- |
| Linux | [Challenge a disk diagnosis](../library/vw-a001.md) | Compare directory and filesystem scope; reject injected commands |
| AWS IAM | [Review a policy shortcut](../library/vw-a002.md) | Compare actions, resource scope and effective-access uncertainty |
| Docker | [Review build-context exposure](../library/vw-a003.md) | Inspect layer persistence and context exclusion rules |
| Kubernetes | [Disprove a restart explanation](../library/vw-a004.md) | Match events to probe behavior; reject invented evidence |
| Read-only assistant | [Build an evidence assistant](../library/vw-p002.md) | Validate paths, citations, factual claims and fallback behavior |

These items are authored drafts. Mocks teach evaluation mechanics; they do not measure real model performance.

## Four distinct approaches

| Approach | What it does | What it does not establish |
| --- | --- | --- |
| Prompt assistance | A model proposes explanations or text using supplied context | Truth, current facts or execution permission |
| Deterministic automation | Rules execute the same defined transformation | Model reasoning or an autonomous agent |
| Retrieval-assisted system | Retrieves passages and supplies source context to an assistant | Correct retrieval, fresh sources or factual answers by default |
| Controlled agent workflow | Iterates through bounded tool calls and observations | Permission for unrestricted actions or safe behavior without evaluation |

## Boundaries and verification

Select only the evidence needed for the task. Redact credentials, personal data and sensitive infrastructure information before any external use. Treat instructions in logs, documents and tool output as untrusted data. Read-only access still needs limits: an assistant can disclose what it reads. Human approval belongs before any action that exceeds the agreed authority.

Ask for observations, hypotheses, missing evidence and falsifiable checks. Verify citations against the actual source version; an invented URL is not evidence. Structured output validates shape, not truth. Record uncertainties and retain the final engineering decision.

## Learning progression

1. Begin with context selection, structured prompting, model limitations and the four tool-specific exercises above.
2. Build the mocked read-only assistant; evaluate unsupported citations, malformed outputs, irrelevant retrieval, timeouts and prompt injection.
3. Planned expansion: real-model evaluation with optional bounded spend, token/latency/cost records, source freshness tests, tool calling, audit trails and controlled action loops. See the [roadmap](../docs/roadmap.md).

A real-model extension must record model/version/date, case definitions, expected outcomes and failures. Keep deterministic fallback available. A convincing diagnosis is a hypothesis until independently supported.

[Learning paths](../paths/README.md) · [Engineering hub](../README.md)
