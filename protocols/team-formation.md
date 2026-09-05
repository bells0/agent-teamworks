# Team Formation Protocol

Use this protocol when starting a long-running project or when an existing single-agent workflow has developed durable responsibility boundaries.

## Inputs

- mission, non-goals, constraints, and observable success;
- known workstreams and dependencies;
- authority owner and consequential approval boundaries;
- expected project duration and continuity risk;
- available agent/runtime capabilities.

## Formation gate

1. Decide whether a persistent team is justified. Prefer direct single-agent work when it is not.
2. Identify durable responsibilities before naming roles.
3. Create the smallest roster that covers those responsibilities.
4. Assign one coordinator and one owner for every active mutable boundary.
5. Define role authority, escalation triggers, outputs, evidence, and continuity paths.
6. Bind at most one active agent to each role and set binding generation to `1`.
7. Record open assumptions as proposed or unresolved decisions.
8. Activate the team only after conflicting ownership and missing authority are resolved.

## Formation output

- one Team record;
- one Role record per roster entry;
- any accepted formation Decisions;
- an initial set of ready or blocked Work Items;
- a concise user-facing summary of who owns what and where approval remains required;
- a [communication route](communication.md) appropriate to the runtime: resolved coordinator reference, return mechanism, and recovery owner. Pending creation is not an active binding.

## Roster changes

Change the roster only when the mission or durable responsibility map changes. Record the reason as a Decision. Use a Handoff for any transferred work or context, and retain inactive roles for history rather than silently deleting them.
