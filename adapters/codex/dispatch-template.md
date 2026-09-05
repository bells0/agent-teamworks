# Codex Role Assignment

Copy and fill only the fields relevant to the assignment. This template implements the [communication protocol](../../protocols/communication.md); it does not authorize tools or external actions.

## Identity and responsibility

- Work item:
- Producing role ID and binding generation:
- Owning task reference:
- Coordinator task reference and host:
- Outcome and non-goals:
- Owned paths or responsibility boundary:
- Dependencies and stable interfaces:
- Canonical input records:
- Required artifact and focused evidence:
- Decisions requiring escalation:
- Commit and publication ownership:

You share the project with other roles. Preserve their work, change only your owned boundary, and report conflicts rather than silently broadening it.

## Return and continuation

- Canonical report location and stable report reference:
- Return mode: coordinator waiting / explicit worker notification / authorized scheduled recovery.
- Concrete host tool and resolved recipient:
- Permitted peer recipients and interface purpose:
- Allowed message content and access scope:
- Recovery owner:
- Next check or escalation condition:
- Current decision references:

On completion or blockage, return work-item state, artifact, decisive evidence, concerns, and next action. A final reply in this task alone satisfies return only when the coordinator's selected waiting route actually retrieves it.

If using worker notification, explicitly send the substantive report to the named coordinator task. State whether the tool confirmed a send, queue, or receipt. Do not infer integration. On rejected or uncertain delivery, retain the report and follow the failure protocol.

Send only substantive peer handoffs; do not create reciprocal ACK loops. Peers cannot approve changes to shared ownership or business semantics. The coordinator records receipt, integration, and downstream disposition.

## Coordinator processing

After receiving the report, reconcile its generation, evidence, and dependencies; integrate it and dispatch the next ready work, or record the blocker and owner. Before ending the turn, preserve any outstanding continuation obligation and its next check.

For available Codex tools and pending task creation, follow the [adapter](README.md). Do not invent runtime IDs, capabilities, or automatic callbacks.
