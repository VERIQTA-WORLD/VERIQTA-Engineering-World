# Engineering challenges

Independent, mission-based practice for investigating and solving engineering problems. Each challenge will start with a problem, a bounded environment, permitted changes and measurable outcomes. You choose the investigation and justify the result.

## Choose the right learning format

| Format | What to expect |
| --- | --- |
| Guided exercise | Explanations and steps to practise a focused skill |
| Challenge | A mission and constraints, with independent investigation and optional hints |
| Project | A larger build organised around multiple milestones |

## Planned challenge areas

No challenges are available to run yet. The entries below reserve the initial scope; instructions, fixtures, setup, verification and solutions will be added when this folder is selected for content development. Planned entries are not counted as completed challenges.

| Planned challenge | Topic | Difficulty / time | Environment | Cost | Validation |
| --- | --- | --- | --- | --- | --- |
| Linux service recovery | Linux | To define | Disposable Linux VM or isolated container | Local; final requirements pending | Not executed |
| Network connectivity diagnosis | Networking | To define | Disposable local environment | Local; final requirements pending | Not executed |
| Container build and runtime repair | Docker | To define | Local Docker daemon | Local; final requirements pending | Not executed |
| Kubernetes service connectivity | Kubernetes | To define | Disposable local cluster | Local; final requirements pending | Not executed |
| Terraform change investigation | Terraform | To define | Offline sanitised plan fixtures | No cloud account intended | Not executed |

## How the challenges will work

Read the mission, prerequisites and environment boundary before setup. Future challenge pages will state supported versions and identify any optional downloads or costs. Fault injection will be limited to disposable resources; shared infrastructure and host configuration are outside the challenge scope.

Choose beginner work for a bounded single-tool problem, intermediate work for connected components and incomplete evidence, and advanced work for competing explanations and trade-offs. Difficulty will be assigned to each authored challenge with a rationale.

Attempt the investigation before opening progressive hints. Verification will test the stated outcome and permitted-change boundaries where practical, without printing a repair recipe. Local checks support learning; they are not tamper-proof certification. An offline fixture check will be labelled separately from a live environment test.

Each authored challenge will keep its explained solution separate from the initial instructions, inside its own challenge directory. No solution files or empty scenario folders are created for the planned entries.

## Retain your evidence

Keep a short personal record of the mission, environment/version, observations, hypotheses, changes, verification and cleanup. Record which hints or solution material you used. Explain what you verified and what remains uncertain; do not present a copied solution as independent work. Remove credentials and private information before sharing evidence.

## Related practice available now

These existing activities remain in their original categories and are not counted as new challenges:

- [Linux storage exercise](../library/vw-e001.md): practise safe local evidence collection.
- [Network protocol question](../library/vw-c002.md): distinguish DNS, connection and HTTPS evidence.
- [Docker configuration review](../library/vw-a003.md): check a proposed recommendation against image layers.
- [Kubernetes selector incident](../library/vw-i001.md): reason about a Service with no destinations.
- [Terraform replacement incident](../library/vw-i003.md): assess a stateful lifecycle change.

Future challenges will add distinct practical outcomes rather than copy these activities. Each challenge will have one stable catalogue ID and one canonical directory, even when several learning paths link to it.

[Engineering hub](../README.md) · [100-day journey](../journey/README.md) · [Planned challenge records](../catalogue/challenges.json)
