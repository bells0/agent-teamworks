# Work Routing Protocol

The team is persistent; the work graph changes. Decompose each request according to the request itself, then route the resulting outcomes into the established roster.

## Decompose before assigning

For each request:

1. State the observable outcome and non-goals.
2. Identify consequential unresolved decisions and stop dependent execution until they have authority.
3. Map dependencies, shared interfaces, and mutable ownership.
4. Split only where an outcome can be accepted, evidenced, and integrated independently.
5. Order dependent work and mark genuinely independent paths.
6. Define evidence and acceptance state for every work item.

## Route into the roster

- Assign by owned responsibility, not by agent availability alone.
- Reuse the existing role for recurring responsibility.
- Give one role primary ownership; supporting roles remain explicit.
- Create a new role only when the uncovered responsibility will persist beyond one work item.
- If no current role can own a consequential decision, escalate rather than improvising authority.

## Work-item transitions

```text
backlog -> ready -> in_progress -> review -> verification
                                      |           |
                                      v           v
                                   blocked   user_acceptance -> done
```

`blocked` may be entered from any active state. `cancelled` preserves abandoned work without erasing history. A work item becomes `done` only when its required engineering and acceptance states are satisfied or explicitly marked not required.

## Coordinator return contract

Every role returns:

- current work-item state;
- produced artifact or observable change;
- decisive evidence and its scope;
- concerns, failed approaches, or unresolved obligations;
- requested decision or next routing action.

The coordinator integrates this information into the project view. Internal completion that never returns to coordination is not team completion.
