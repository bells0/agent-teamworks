# Contributing

Agent Teamworks should evolve from observed project needs and reproducible collaboration failures, not from speculative process expansion.

This repository is the source of the Codex plugin. Its primary entry is an explicit request to build a project team; roster adjustment and role handoff/restoration are supporting operations. Preserve this boundary when changing discovery descriptions or protocols. See the [plugin decision](docs/decisions/0001-codex-team-formation-plugin.md).

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

For manifest changes, also use the Codex bundled plugin validator when available:

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py .
```

Build the installable marketplace using Python 3.10 or newer (no build dependencies):

```bash
python3 scripts/build_plugin.py
```

The generated `dist/` contains `.agents/plugins/marketplace.json` and `plugins/agent-teamworks/`. It is ignored by Git. Edit the root sources, never the generated copy. For subsequent builds, use `--output dist/<new-build-name>` with a fresh directory. The build refuses to overwrite an existing directory.

Repository validation includes building a temporary distribution and resolving links inside the packaged plugin. It does not install the plugin into a personal Codex profile or execute live team-formation scenarios. Keep static package checks, host installation, and behavioral evaluation distinct in delivery notes.

## Compatibility

The `schema_version` field tracks record compatibility. Backward-incompatible record changes require a migration note and a version change. Keep proposed values out of current-truth examples.

The plugin manifest version tracks plugin releases separately. Packaging version `0.3.0` keeps all existing record schema versions. Include the bundled resources whenever publishing the plugin; distributing only the Skill directory breaks its relative references.

## Public-data boundary

Examples must be fictional or explicitly approved for publication. Do not contribute credentials, personal data, private repository paths, private project status, or claims that cannot be supported by public evidence.
