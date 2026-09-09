---
name: agent-teamworks
description: Build a persistent multi-agent team when the user asks to form a project team (构建团队、组建团队). Also use for an explicit request to adjust that team or hand off and restore its roles. Ordinary feature work, debugging, status questions, and one-off parallel tasks do not trigger team formation.
---

# Agent Teamworks

The primary outcome is a project team ready to work: a minimal roster, clear ownership, real runtime bindings where available, a return route, and durable project records.

## Choose the requested operation

- **Build a team:** read existing project records first, then establish the mission and missing team structure. Repeated requests reuse the existing team instead of creating another roster.
- **Adjust a team:** read its current roles, decisions, and open work; change only the requested responsibilities and record any ownership transfer.
- **Hand off or restore:** recover the existing logical roles and obligations using the handoff protocol. Do not rebuild from chat memory.

Installing or selecting the plugin alone does not authorize creating a team. Follow the user's actual request. A normal feature request goes through an established coordinator; it does not rerun formation or grow the roster automatically.

All links below resolve relative to this installed Skill inside the plugin. Keep the plugin package read-only. Write team records into the user's target project, never into the plugin, its examples, or a personal global configuration directory. Do not ask the user for the plugin source checkout path.

## Establish project truth

1. Read the project's existing `.agent-teamworks/` records when present.
2. For a new team, read the [operating model](../../framework/operating-model.md) and [formation protocol](../../protocols/team-formation.md).
3. Define the mission, non-goals, observable success, authority boundary, and acceptance owner.
4. Form the smallest stable roster justified by durable responsibilities. Keep one coordinator and one active binding per role.
5. Store the Team, Role, Work Item, Handoff, and Decision records using the bundled [schemas](../../schemas/) in the target project's `.agent-teamworks/` directory. Create records as needed; never copy fictional identities or acceptance results into a live project.
6. Follow the [Codex adapter](../../adapters/codex/README.md) to bind runtimes and install the minimal project continuation entry. Use the scope and authorization already given; ask only for missing decisions that materially affect the team or its authority.

Do not form a team for a single clear edit or unresolved work that cannot yet be decomposed safely.

## Make the team ready for everyday work

Before reporting formation complete, return the roster and owned boundaries, actual runtime readiness, the coordinator entry, the communication route, open decisions, and links to the project records. A saved roster with unavailable or pending runtimes is a formation draft, not a running team. Building the team does not by itself authorize starting every implementation item.

The following operating rules are for the established coordinator. Daily work uses the existing team and records without requiring the user to invoke formation again.

## Route work within the established team

Read the [work-routing protocol](../../protocols/work-routing.md) and [communication protocol](../../protocols/communication.md) before dispatch. For Codex, use the [adapter](../../adapters/codex/README.md) and its [dispatch template](../../adapters/codex/dispatch-template.md). Resolve the coordinator address, return mechanism, and recovery owner; honor requested task visibility. Pending runtime creation is not an active binding. Decompose new work by observable outcome, dependencies, shared interfaces, mutable ownership, evidence, and acceptance. Route it to existing roles before considering roster growth.

Create a new role only for a responsibility that will persist beyond one work item. A role is not an agent count, and an agent task is not the role's durable identity.

Keep the coordinator as the integrated user-facing surface. Require role outputs to return state, artifact, evidence, concerns, and a next action. Do not infer project completion from an idle or completed child task.

A role-local final reply is not delivered unless the selected return route retrieves it. Workers explicitly notify the coordinator when that mode is selected. On receipt, integrate the report and dispatch ready dependent work or record its blocker and owner. Before ending a coordinator turn, retain a supported continuation route or disclose the continuity limitation. Deduplicate repeated reports and avoid ACK loops; communication never grants additional authority.

## Preserve continuity

Read the [handoff protocol](../../protocols/handoff.md) before replacing an agent binding or transferring ownership. Keep the logical role ID, create a complete Handoff, increment the binding generation, and retire the predecessor without deleting its history.

Stop duplicate active owners. If a predecessor disappears, reconstruct only from durable evidence and label unknowns.

## Publish GitHub text safely

Read the [GitHub publication integrity protocol](../../protocols/github-publication-integrity.md) before creating or updating a multiline pull request description, issue body, review body, or comment. Use a real file or standard input, verify Markdown structure before publication, read the stored body back through the GitHub API, and repair the original record instead of posting a duplicate.

## Close outcomes and teams

Read [review and acceptance](../../protocols/review-and-acceptance.md) when an outcome needs product experience acceptance, independent technical review, delivery review, or merge. Preserve the sequence: runnable candidate and implementer self-check; product acceptance when required; final technical `PASS` or `NEEDS_FIX`; delivery `MERGE_READY` or `NEEDS_FIX`; merge authorization under project rules; permitted merge.

Keep product acceptance, technical verdict, delivery readiness, and merge authorization as four independent states. A product review advisor role only advises; record any designated acceptance authority separately. Re-accept only affected user-visible scope after a behavior change; require independent technical re-review for a purely technical fix. Implementers do not approve their own work.

Read [escalation](../../protocols/escalation.md) when authority, ownership, requirements, or evidence is genuinely missing. Project rules define push and merge permissions. Merge requires explicit authorization unless a recorded, narrowly scoped standing authorization applies. The framework does not authorize publication, spending, credential use, destructive changes, privacy-sensitive operations, acceptance, or merge.

Pause or dissolve the team explicitly. Preserve remaining obligations and final acceptance state instead of silently abandoning the roster.
