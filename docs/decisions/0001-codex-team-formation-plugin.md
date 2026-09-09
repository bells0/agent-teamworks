# Decision: ship Agent Teamworks as a Codex team-formation plugin

Date: 2026-09-10
Status: accepted

## Problem and evidence

The existing repository distributes a Skill that links to sibling protocols and schemas. Its instructions require keeping the full source checkout available, and adoption has required repeatedly supplying that checkout path. The agreed product entry is an explicit request to build a project team, rather than intercepting ordinary development requests.

## Decision

This repository is the canonical source of the Agent Teamworks Codex plugin. The root `.codex-plugin/plugin.json` exposes the existing Skill and includes all referenced resources in the distributable package. Plugin version `0.3.0` introduces this packaging and entry-point change.

The primary operation is team formation. Explicit roster adjustment and handoff/restoration are supporting operations. Once formed, a team works through its coordinator and project-local records without repeating formation. Natural-language requests to build a team can select the Skill; a special invocation token is not mandatory.

Team setup creates a minimal project continuation entry in the target project's existing instructions. It points to project records, not a developer's source checkout or a version-specific plugin cache. Runtime availability and pending bindings remain visible; the plugin does not supply a hosted scheduler or messaging server.

The root framework, protocols, schemas, and adapter remain the only maintained copies. A standard-library build script creates an ignored local marketplace distribution with the complete plugin under `plugins/agent-teamworks/`. This preserves current source links while satisfying Codex's marketplace installation path. The distribution is generated, never edited as a second source tree.

## Compatibility and boundaries

Existing Team, Role, Work Item, Handoff, and Decision schemas do not change. Work Item stays at `0.2.0`; other records stay at `0.1.0`. Existing role identities, generations, records, and acceptance states remain valid. Earlier foundation specs and plans are retained as history.

The plugin installs no hooks, MCP servers, accounts, or background processes. Repository development does not initialize a real team in this repository or change the developer's global Codex settings. Installation is a separate one-time host action documented in the README.

## Validation

Validate the manifest and Skill with the Codex bundled validators, run existing repository checks, and build into a fresh directory to check that the marketplace resolves its plugin and all shipped local documentation links stay inside the package. Evaluate formation, ordinary requests, and recovery using the cases in `evals/scenarios.md`; static checks alone do not establish live agent readiness or automatic continuation.
