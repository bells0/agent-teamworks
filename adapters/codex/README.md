# Codex Adapter

This adapter maps Agent Teamworks concepts onto Codex without making Codex task IDs the source of project truth.

## Runtime mapping

| Agent Teamworks | Codex mapping |
|---|---|
| Team | Project-level `.agent-teamworks/` records plus a coordinator task |
| Logical role | Stable role ID and role record |
| Agent binding | Current Codex task, thread, or subagent reference stored on the role |
| Work item | Bounded outcome routed by the coordinator |
| Handoff | Durable record created before replacing a binding |
| Decision | Versioned choice with an explicit authority owner |

Prefer one visible coordinator task as the user's main interaction surface. A persistent Codex task can represent a durable role when the environment and user request support it. A bounded subagent may produce one work item, but that temporary runtime does not become the logical role identity.

## Formation

1. Confirm that project duration or responsibility boundaries justify a team.
2. Create the Team and Role records before spawning role runtimes.
3. Use stable role IDs in task titles or prompts so ownership is recognizable.
4. Keep one active Codex binding per role. Archive or retire duplicates only after their state has been reconciled.
5. Record the binding reference and generation in the Role record.

Do not create Codex tasks, subagents, or other external state unless the user request and host authorization allow it. When multi-agent execution is unavailable, the same records may guide sequential role execution by one agent.

## Coordination loop

For every routed work item, the coordinator provides the role with:

- outcome and non-goals;
- owned paths or responsibility boundary;
- dependencies and stable interfaces;
- authority and escalation limits;
- required evidence and return format.

The role returns state, artifact, evidence, concerns, and the requested next action. The coordinator updates durable records and reports the integrated result to the user. A completed role task that is not returned and integrated remains incomplete at the team level.

## Continuity

When a Codex task or agent must be replaced:

1. create a succession Handoff;
2. preserve current truth, evidence, open work, and failed approaches;
3. bind the replacement as pending;
4. obtain acknowledgement;
5. complete the handoff and increment the role generation;
6. retire the previous binding.

If a runtime disappears, reconstruct only from durable evidence and mark unknowns explicitly.

## Software delivery integration

Agent Teamworks decides **who persists and how work moves through the team**. A software-delivery method decides **how one outcome moves through Spec, Plan, implementation, review, verification, acceptance, and Git closure**.

Use them together without duplicating authority:

- the Agent Teamworks coordinator owns roster, routing, and cross-role state;
- the delivery controller owns the current software outcome and its evidence;
- project Role and Work Item records point to delivery artifacts rather than copying them;
- repository merge still requires explicit authorized approval.

## GitHub user-visible text

For multiline pull request descriptions, issue bodies, review bodies, or comments, follow the [GitHub publication integrity protocol](../../protocols/github-publication-integrity.md). Prepare the exact Markdown in a real file or standard input, publish it once, then read the stored text back through the GitHub API. Repair malformed content in the original record; never hide a failed publication by posting a duplicate.
