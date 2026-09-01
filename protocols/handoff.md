# Handoff Protocol

A handoff protects continuity when ownership moves between roles or when a new agent binding succeeds the prior binding of the same role.

## Handoff types

- **Role succession:** same logical role, new agent binding and incremented generation.
- **Ownership transfer:** responsibility or work moves from one role to another after an authorized decision.
- **Temporary delegation:** a bounded output is produced elsewhere, while the original role retains final ownership.

## Required handoff content

1. Source and destination role IDs and binding generations.
2. Reason and authorized scope of transfer.
3. Current truth and the last known-good state.
4. Completed outputs and evidence locations.
5. Open work, blockers, risks, and failed approaches.
6. Decisions already made and decisions still required.
7. Mutable state or files owned at the transition.
8. Destination acknowledgement and completion time.

## Succession sequence

1. Mark the handoff `prepared` while the current owner still owns the role.
2. Bind the successor as pending; do not create two active owners.
3. The successor reads the named continuity records and acknowledges unresolved obligations.
4. Mark the handoff `completed`.
5. Retire the previous binding, increment the role generation, and activate the successor.

If the prior agent disappears unexpectedly, the coordinator creates a recovery handoff from durable evidence, marks unavailable facts explicitly, and does not invent completion.

## Failure conditions

- two active bindings for one role;
- a generation change without a completed succession handoff;
- transfer of a consequential responsibility without an authorized decision;
- a destination claiming inherited work without reading or acknowledging open obligations;
- deletion of predecessor history after replacement.
