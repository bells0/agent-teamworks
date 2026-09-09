# Agent Teamworks

[English](README.md) | [简体中文](README.zh-CN.md)

> Build the team once. Keep roles, context, and obligations connected.

Agent Teamworks is a **Codex plugin for building project teams**. Ask it to form a team when a project needs durable responsibilities and coordinated work. It establishes the smallest useful roster, clear ownership, runtime bindings, communication, and project-local continuity records.

After formation, work goes through the established coordinator. Ordinary feature requests do not rerun team formation. Return to the plugin when the team needs an explicit roster adjustment or role handoff/restoration.

## Install once

Requirements: Python 3.10+ to build the distribution, and a Codex version with `codex plugin` support. Python dependencies are only needed for development validation, not for building or using the plugin.

From this repository checkout:

```bash
python3 scripts/build_plugin.py
codex plugin marketplace add ./dist
codex plugin add agent-teamworks@agent-teamworks
```

The first command builds a complete local marketplace. The next two register that marketplace and install the plugin in your Codex profile. Start a new Codex task in the project that needs a team after installation so its Skills can be discovered. The source repository path is not needed in everyday prompts.

The builder creates a fresh `dist/` and refuses to overwrite existing output. For another build, choose a fresh directory with `--output dist/<build-name>`. The root sources remain canonical; generated distributions are not a second maintained plugin.

The distribution contains the manifest, Skill, protocols, schemas, adapter, and referenced documentation. Copying only `skills/agent-teamworks/` is not a complete plugin installation. Building alone does not install the plugin or alter Codex configuration.

## Use when you need a team

In your target project, select Agent Teamworks and ask:

> Build an Agent team for this project. Establish the smallest useful roster, clear responsibilities, communication, and continuity records.

The Skill can also be discovered from an explicit natural-language team-building request, or invoked as `$agent-teamworks` where the host exposes that name. You do not need to specify the plugin checkout path.

| Stage | What you ask | What the plugin or team does |
| --- | --- | --- |
| Build | “Build a team for this project.” | Read project context, reuse any existing team, establish roles, bind supported runtimes, and set up communication. |
| Work | “Implement this feature.” | The established coordinator routes the outcome to existing roles; formation does not run again. |
| Adjust | “Adjust the team's responsibilities for the new scope.” | Reconcile current roles and record only the required ownership changes. |
| Hand off or restore | “Replace this role's Agent and continue its open work.” | Preserve the logical role, decisions, history, and outstanding obligations through a handoff. |

Formation produces a team summary with responsibilities, actual runtime readiness, the coordinator entry, communication route, open decisions, and links to records. A roster with unavailable or pending runtimes is reported as a draft, not a running team. Creating a team does not automatically release every implementation item.

## Where the team lives

The plugin's rules are bundled with the installation. Mutable team state belongs to the project being served:

```text
your-project/
├── AGENTS.md                 # Small continuation entry; existing instructions preserved
└── .agent-teamworks/
    ├── team.json
    ├── roles/
    ├── work-items/
    ├── decisions/
    └── handoffs/
```

Records are created as needed. The continuation entry points to project records, not a machine-specific plugin path. A new conversation reads the existing role bindings before taking ownership; it does not create another coordinator merely because a new task opened.

The coordinator integrates role outputs and preserves their evidence. Product experience acceptance, independent technical review, delivery readiness, and merge authorization remain separate. Installing the plugin grants no publication, spending, or merge authority.

## Plugin source

```text
agent-teamworks/
├── .codex-plugin/plugin.json # Codex plugin identity and discovery metadata
├── skills/agent-teamworks/   # Team-building, adjustment, and handoff entry
├── framework/                # Canonical operating model
├── protocols/                # Formation, routing, communication, and acceptance
├── schemas/                  # Team, Role, Work Item, Handoff, Decision
├── adapters/codex/           # Runtime mapping and project continuation template
├── roles/                    # Role-contract guidance
├── examples/                 # Fictional adoption records
├── docs/                     # Decisions, compatibility notes, historical specs
├── evals/                    # Behavioral evaluation cases
├── scripts/                  # Package builder and repository validator
└── tests/                    # Distribution, record, and reference checks
```

The [operating model](framework/operating-model.md), [formation protocol](protocols/team-formation.md), [communication protocol](protocols/communication.md), and [Codex adapter](adapters/codex/README.md) define how teams are built and continue working. The [fictional commerce example](examples/commerce-project/) illustrates records; its five-role roster is not a required team size. The [communication walkthrough](examples/communication-walkthrough.md) illustrates a return route, not a runtime execution log.

Agent Teamworks can work with an available software-delivery workflow. It owns team construction, role continuity, and routing; that workflow handles implementation and delivery for a particular outcome. No separate delivery plugin is required to build a team.

## Validate and contribute

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
```

Validation checks schemas, example records, cross-record references, dependencies, handoffs, Skill metadata, and source links. It also builds a fresh marketplace and checks links inside the copied plugin. Static checks do not certify live team formation, task messaging, or unattended continuation; those require the [behavioral scenarios](evals/scenarios.md).

Plugin `0.3.0` introduces the [team-formation plugin packaging decision](docs/decisions/0001-codex-team-formation-plugin.md). [Work Item Schema `0.2.0`](docs/migrations/work-item-0.2.0.md) and other record schemas at `0.1.0` remain compatible. The plugin uses Codex's available execution capabilities; it includes no hosted runtime, dashboard, hooks, MCP server, or background scheduler.

Changes follow branch → pull request → independent review → authorized merge. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
