# Validation evidence

Recorded 2026-11-02. Authored material remains draft; no independent reviewer has signed off. [Machine-readable evidence](../catalogue/validation.json) records exact scope. This page reports repository and selected fixture checks, not a guarantee of every learning outcome.

## Static validation

The repository checker validates metadata, stable IDs, catalogue references, required sections, internal files and anchors, image paths, basic Markdown quality, safe SVG structure and generated navigation/counts. Validator unit tests include valid records and deliberately invalid examples. The Python modules are syntax-compiled separately. External documentation links are not comprehensively availability-tested.

## Local execution

The allowlisted runner executes published snippets in disposable directories on macOS with Python 3.9.6, POSIX sh and local Git. It checks workspace setup (Day 2), file permissions (Day 3), log counts (Day 4), two local commits (Day 5), script syntax and four exit-code cases (Day 6), the rejected handoff fixture (Day 7), small file sizes/cleanup (VW-E001), and the Python manifest reference implementation including invalid types and CLI errors (VW-E002).

Execution fields for these items are **partial** because the runner checks those stated scopes, not all reflection, manual reasoning or extension tasks. Day 1 is an unexecuted reasoning activity. The runner uses only explicit first-batch snippets; it does not discover or execute arbitrary contributor code.

## Material limitations

Docker is installed but its daemon is unavailable. No live Docker, Kubernetes, Helm, EKS, Argo CD, Terraform, Ansible or Prometheus environment was executed. Cloud resources were not provisioned. No real AI model was called. Helm/Kubernetes and Terraform activities default to offline review; their syntax and reasoning do not establish runtime behavior. The two projects are authored briefs with solution guidance, not supplied turnkey implementations or executed systems.

The banner, map and tool icons are local SVGs with alt text. The README was rendered through GitHub’s Markdown API and visually inspected in a narrow browser viewport using both dark and light preview styling. Banner, map, tool marks, topic-grid wrapping and progress labels were checked. GitHub's own rendering and mobile behavior may differ from a local preview. Source dates record research/reference preparation, not a product compatibility guarantee.
