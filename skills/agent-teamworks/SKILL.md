---
name: agent-teamworks
description: Form and operate a persistent multi-agent team for a long-running project, keeping logical roles stable while decomposing new work by outcome and dependency. Use when the user requests a project team or recurring cross-role collaboration; exclude one-off tasks and simple parallel delegation.
---

# Agent Teamworks

Treat the team as durable project infrastructure, not a temporary group created for one prompt.

## Establish project truth

1. Read the project's existing `.agent-teamworks/` records when present.
2. For a new team, read the [operating model](../../framework/operating-model.md) and [formation protocol](../../protocols/team-formation.md).
3. Define the mission, non-goals, observable success, authority boundary, and acceptance owner.
4. Form the smallest stable roster justified by durable responsibilities. Keep one coordinator and one active binding per role.
5. Store the Team, Role, Work Item, Handoff, and Decision records using the project [schemas](../../schemas/).

Do not form a team for a single clear edit or unresolved work that cannot yet be decomposed safely.

## Route each request

Read the [work-routing protocol](../../protocols/work-routing.md). Decompose new work by observable outcome, dependencies, shared interfaces, mutable ownership, evidence, and acceptance. Route it to existing roles before considering roster growth.

Create a new role only for a responsibility that will persist beyond one work item. A role is not an agent count, and an agent task is not the role's durable identity.

Keep the coordinator as the integrated user-facing surface. Require role outputs to return state, artifact, evidence, concerns, and a next action. Do not infer project completion from an idle or completed child task.

## Preserve continuity

Read the [handoff protocol](../../protocols/handoff.md) before replacing an agent binding or transferring ownership. Keep the logical role ID, create a complete Handoff, increment the binding generation, and retire the predecessor without deleting its history.

Stop duplicate active owners. If a predecessor disappears, reconstruct only from durable evidence and label unknowns.

## Publish GitHub text safely

Read the [GitHub publication integrity protocol](../../protocols/github-publication-integrity.md) before creating or updating a multiline pull request description, issue body, review body, or comment. Use a real file or standard input, verify Markdown structure before publication, read the stored body back through the GitHub API, and repair the original record instead of posting a duplicate.

## Close outcomes and teams

Read [review and acceptance](../../protocols/review-and-acceptance.md) when an outcome needs independent review, technical verification, or user acceptance. Keep those states distinct and use only controls justified by the actual risk.

Read [escalation](../../protocols/escalation.md) when authority, ownership, requirements, or evidence is genuinely missing. The framework does not authorize publication, spending, credential use, destructive changes, privacy-sensitive operations, acceptance, or merge.

Pause or dissolve the team explicitly. Preserve remaining obligations and final acceptance state instead of silently abandoning the roster.
