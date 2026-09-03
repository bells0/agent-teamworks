# Contributing

Agent Teamworks should evolve from observed project needs and reproducible collaboration failures, not from speculative process expansion.

## Propose a change

For a semantic change, describe:

- the project outcome being protected;
- current evidence that the problem exists;
- why existing records or protocols are insufficient;
- the smallest effective change;
- how the behavior can be evaluated.

Small corrections may go directly to a pull request. Consequential changes to role semantics, authority, lifecycle, or record compatibility should begin with an issue or accepted Spec.

## Delivery workflow

1. Create a focused feature branch from the current default branch.
2. Keep each commit independently understandable and limited to one accepted outcome.
3. Update schemas, examples, protocols, Skill routing, and evaluations together when a semantic change affects them.
4. Run the repository validation.
5. Follow the [GitHub publication integrity protocol](protocols/github-publication-integrity.md) for every multiline pull request, issue, review, or comment body.
6. Open a pull request with scope, evidence, compatibility impact, and unresolved questions.
7. Obtain independent maintainer review and required checks.
8. Merge only with explicit maintainer authorization.
9. Delete the merged feature branch when no unmerged work or dependency remains.

Do not push implementation directly to the default branch. Do not rewrite shared history or force-push without explicit maintainer authorization.

## Validate locally

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

When changing the Skill, also run the Codex bundled Skill validator when available:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/agent-teamworks
```

## Compatibility

The `schema_version` field tracks record compatibility. Backward-incompatible record changes require a migration note and a version change. Keep proposed values out of current-truth examples.

## Public-data boundary

Examples must be fictional or explicitly approved for publication. Do not contribute credentials, personal data, private repository paths, private project status, or claims that cannot be supported by public evidence.
