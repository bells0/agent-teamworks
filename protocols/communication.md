# Communication and Continuation Protocol

Use this protocol before dispatching work to an independent runtime. A role-local final response is not a delivered report, and a delivered report is not an accepted outcome.

## Why this protocol exists

A coordinator can dispatch several roles, end its turn, and leave completed reports stranded in their separate tasks. The return contract defines report content but cannot by itself deliver the report or resume coordination. Protect continued progress with an explicit return route and recovery owner, using existing runtime tools rather than adding a messaging service.

## Dispatch contract

Use the [dispatch template](../adapters/codex/dispatch-template.md) with the applicable runtime adapter. Every assignment identifies:

- the work item and current role binding generation;
- one owner, bounded outcome, owned paths, dependencies, and acceptance evidence;
- the coordinator's resolved runtime reference and any permitted peer recipients;
- the artifact location and how the report will reach coordination;
- who will resume coordination, using an observed host capability;
- when the recovery owner will check again and what triggers escalation.

Choose the smallest available continuation mode:

1. **Coordinator waiting:** the coordinator remains active and waits for role results, then retrieves and integrates them.
2. **Worker notification:** the worker explicitly sends its result to the coordinator using a capability confirmed to deliver to that task and resume it, or queues the result while the coordinator is active.
3. **Scheduled recovery:** when neither path covers an intended unattended interval, use an authorized host follow-up with a concrete condition and cancellation point.

Do not silently invent a background scheduler or assume a visible task stays awake. If no supported mode can cover the interval, report the continuity limitation and retain the open work. Do not claim autonomous continuation. Scheduling and sending remain subject to host and user authorization.

Before ending a coordinator turn with outstanding dispatched work, identify the selected continuation mode and recovery owner in the coordination record. If waiting, continue waiting; if handing off continuation, verify that a usable route exists. An elapsed wait timeout is not completion or a reason to discard the obligation.

## Report and integrate

Send one substantive result or blocker report containing:

- work-item ID, producing role ID and generation, report reference or revision;
- state, canonical artifact reference, and evidence with its limits;
- unresolved obligations, decisions needed, and intended recipient;
- the next action and the role that can take it.

Use a stable report reference, such as a task turn ID or artifact revision. Transport retries reuse that reference; a materially changed result gets a new revision. Do not create a hash solely to identify a report.

The coordinator owns the following observable facts:

| Fact | Evidence | What it does not prove |
|---|---|---|
| Produced | Report or artifact exists at a canonical location | Delivery to another task |
| Received | Recipient fetched the report or host supplied receipt evidence | Review, product acceptance, or integration |
| Integrated | Coordinator reconciled the result with current interfaces, decisions, and work state | Permission to release or merge |
| Routed | Next assignment was dispatched, or an explicit blocked, paused, or completed disposition was recorded with its owner | Completion of downstream work |

A successful send proves only what the host response reports. It may mean queued, not read. The coordinator can record receipt while processing the report; an extra ACK message is unnecessary. No ACK-to-ACK loops.

After receipt, reconcile current work and dependency state, resolve or assign concerns, then dispatch ready dependent work in the same coordination cycle. If dispatch cannot proceed, record the precise missing decision or dependency and who owns it. Notify the user of meaningful changes, not every internal message.

## Peer communication and authority

Roles may exchange bounded interface questions and dependency-ready reports directly with recipients named in the assignment when authorized. Keep the coordinator informed of changes affecting shared contracts, ownership, scope, or ordering. Peer discussion does not transfer mutable ownership or grant product acceptance.

Send the minimum information needed: artifact references and scoped summaries where possible. Define recipient access and allowed content in the assignment. Never include credentials or assume team membership overrides data restrictions. If approval rejects a send, preserve an undelivered disposition, report the reason and affected action, and seek the missing authorization or use a genuinely permitted narrower message. Do not reroute the same prohibited disclosure through another channel.

## Failure and recovery

- **Send failed:** producer retains the report and informs the recovery owner through an allowed route. Do not record receipt.
- **Send result uncertain:** inspect delivery or recipient state before retrying. Use the same report reference and avoid duplicate downstream execution.
- **Recipient unavailable:** preserve pending delivery; the recovery owner resumes the recipient or performs an authorized succession.
- **Report received but not processed:** coordinator recovery retrieves pending reports and integrates them before claiming the team is progressing.
- **Duplicate report:** recognize an already integrated reference and do not dispatch the same outcome twice.
- **Stale generation or changed decision:** preserve the old evidence, compare it with current ownership and requirements, and explicitly decide reuse or rework. Do not apply a stale report as a new instruction.
- **Repeated failure:** after two attempts with the same approach, change the approach or escalate the missing capability. Recovery frequency should match actual task duration and host limits, not impose a universal polling interval.
- **Delayed runtime creation:** a pending creation reference is not an active binding. A late duplicate stays pending until the coordinator reconciles it with the current role; it must not execute the same assignment.

If the coordinator restarts, reconstruct unresolved dispatches and reports from durable records before issuing new work. Use the [handoff protocol](handoff.md) for binding replacement.

## Minimal durable record and compatibility

Keep a compact communication journal in the project's existing coordination document, or at `.agent-teamworks/communication.md`. The coordinator is the sole journal writer; peers send reports rather than racing to edit shared state. Record only substantive dispatches, result revisions, and unresolved recovery obligations.

A journal entry needs: work item, role/generation, runtime reference, report reference and artifact, produced/received/integrated/routed facts, next action/owner, continuation mode, and next check or escalation condition. Unknown facts remain unknown. Use timestamps or host receipt references when available, not invented delivery times.

This is a protocol addition, not a change to Team, Role, Work Item, Handoff, or Decision JSON schemas. Do not add undeclared fields to those strict schemas. Existing records remain valid; add the journal location to existing role continuity paths when adopting it.

The framework supplies no hosted runtime or delivery guarantee. [Behavioral evaluations](../evals/scenarios.md) must observe actual communication and downstream continuation; schema and documentation checks alone cannot demonstrate liveness.
