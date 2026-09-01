# Role Contracts

A role is a stable project responsibility, not a job title and not a single agent process. Projects may rename, combine, or extend the following archetypes.

Every active role contract must state:

- a stable `role_id` and human-readable name;
- its durable purpose and owned boundaries;
- decisions it may make independently;
- decisions it must escalate;
- inputs it consumes and outputs it owes the team;
- evidence required for its claims;
- continuity records that a successor must read;
- its current agent binding and generation.

## Coordinator — required

Owns mission interpretation, roster health, task decomposition, routing, shared interfaces, integrated status, authority boundaries, acceptance state, and closure.

The coordinator is normally the user's primary interface. It must surface role results and blockers without making the user manage each agent separately. It cannot convert an implementer report into acceptance without the required evidence and authority.

## Domain or product lead — optional

Owns intended behavior, domain semantics, outcome priorities, and the distinction between proposal and accepted direction.

Use this role when product meaning will recur across work items. It does not own implementation mechanics unless the team explicitly combines those responsibilities.

## Product review advisor — optional

Offers fallback product advice, risks, or alternatives when independent perspective is useful. The advisor role does not own product experience acceptance; any designated acceptance authority must be recorded separately.

Technical evidence or an advisor recommendation never substitutes for the user's or designated acceptance owner's decision about product direction, business semantics, information hierarchy, workflow, and real use.

## Architect or integrator — optional

Owns shared boundaries, cross-component contracts, dependency order, and integration coherence.

Use this role when multiple builders depend on stable interfaces. It should not become a universal approval gate for unrelated local decisions.

## Builder — optional, repeatable by boundary

Owns one stable implementation or artifact boundary and the work items routed to it. Multiple builder roles are valid when their mutable ownership is disjoint and durable.

A builder returns observable output, focused evidence, concerns, and follow-up obligations. It does not approve its own outcome or broaden shared contracts without a decision.

## Technical reviewer — optional

Owns independent comparison of the final candidate HEAD against its requirements, diff, functional completeness, failure and regression paths, accessibility, tests, CI, scope, risk, rollback, and delivery evidence. It remains read-only for the reviewed boundary and returns separate technical and delivery verdicts.

Create or activate this role when independent review protects a concrete outcome. It returns `PASS` or `NEEDS_FIX` for technical review and `MERGE_READY` or `NEEDS_FIX` for delivery readiness. Do not use repeated review as a ritual after accepted findings are resolved.

## Verifier or QA — optional

Owns claim-matched observation through the closest available real path. It distinguishes defects from unavailable environments and supplies independent evidence for the technical verdict while keeping product acceptance separate.

Use this role when verification is substantial or recurring. The coordinator may combine its evidence with an independent technical review and delivery assessment. The user or designated acceptance owner still decides product acceptance where required.

## Combining roles

Small teams may combine compatible responsibilities, but the combined role must list the resulting authority and conflict boundaries. Do not combine implementation with independent approval for the same outcome.
