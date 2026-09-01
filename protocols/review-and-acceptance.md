# Review and Acceptance Protocol

Use the cheapest independent control capable of protecting the outcome. Product experience acceptance, technical review, delivery readiness, and merge authorization are separate gates with separate owners and evidence.

## Four independent states

| State | Decision owner | Positive result | Negative result |
|---|---|---|---|
| Product experience acceptance | User or explicitly designated acceptance owner | `accepted` | `rejected` |
| Technical review | Coordinator-routed independent reviewer or verifier | `pass` | `needs_fix` |
| Delivery readiness | Coordinator-routed independent reviewer or verifier | `merge_ready` | `needs_fix` |
| Merge authorization | Authority defined by project rules | `authorized` | `denied` |

Do not infer one state from another. Product acceptance is not technical `PASS`; technical `PASS` is not `MERGE_READY`; `MERGE_READY` is not permission to merge.

## Product experience acceptance

The user or explicitly designated acceptance owner makes the final decision about product direction, business semantics, information hierarchy, workflow, and the experience of using the real path.

A product review advisor may inspect the candidate and offer fallback advice, risks, or alternatives. The advisor role does not own product acceptance and does not convert technical evidence into product approval. Any designated acceptance authority must be recorded separately.

Technical checks, implementation completion, and an advisor recommendation never substitute for product experience acceptance. Use:

- `not_required` — no product-visible or designated-owner outcome needs acceptance;
- `pending` — the acceptance owner has not decided;
- `accepted` — the acceptance owner exercised or reviewed the agreed outcome and approved it;
- `rejected` — the outcome does not satisfy the intended product workflow.

Rejection caused by misunderstood intent returns to the owning decision or specification. A local defect returns to implementation. Do not label pending work complete merely because agents are idle.

## Technical and delivery review

After product experience acceptance when it is required, the coordinator routes the final candidate HEAD to an independent reviewer or verifier. The implementer cannot approve its own work.

### Technical review

Review the candidate HEAD against the accepted outcome and inspect:

- the actual diff and functional completeness;
- exceptions, failure paths, regressions, and affected boundaries;
- the closest available real running path;
- accessibility where the outcome has a user interface;
- focused tests, broader affected checks, and CI evidence.

Return exactly one technical verdict:

- `PASS` — the reviewed candidate supports the technical claims;
- `NEEDS_FIX` — a concrete defect, unsupported claim, or required check remains.

### Delivery readiness

Review the same candidate HEAD for:

- intended scope and unrelated changes;
- material risks and rollback or recovery path;
- required checks and unresolved dependencies;
- PR description, evidence, and delivery completeness.

Return exactly one delivery verdict:

- `MERGE_READY` — the candidate is ready for the project's merge decision;
- `NEEDS_FIX` — delivery evidence, scope control, risk handling, or repository readiness remains incomplete.

Passing a schema check proves schema validity, not project usefulness. Passing a UI build proves compilation, not hands-on usability. Keep every claim within its evidence boundary.

## Changes after acceptance

- If a later change affects user-visible behavior, repeat product experience acceptance only for the affected scope, then repeat final technical and delivery review for the resulting candidate HEAD.
- If a later change is purely technical and preserves accepted behavior, product re-acceptance is not required, but an independent technical re-review of the changed boundary is required.
- Re-review prior findings and the affected diff. Do not restart an unbounded full-review loop without new impact evidence.

## Required sequence

```text
runnable candidate and implementer self-check
  -> product experience acceptance when required
  -> final technical review of candidate HEAD: PASS / NEEDS_FIX
  -> delivery review: MERGE_READY / NEEDS_FIX
  -> merge authorization under project rules
  -> merge by the permitted actor
```

The coordinator owns sequencing and evidence integration. If review reveals a requirement misunderstanding, return to the decision or specification owner instead of treating it as a local fix.

Mark a gate `not_required` when it does not apply, such as repository merge for a non-repository outcome. Do not skip an applicable gate silently.

## Push and merge permissions

Project rules define who may push, create or update a PR, authorize merge, and execute merge. Merge requires explicit authorization by default. A project may instead define a narrow standing authorization for routine merges; record its scope and do not extend it by implication.

Push permission does not imply merge authorization. `MERGE_READY` does not imply either permission.

## Completion rule

A work item becomes `done` only when:

1. required outputs exist;
2. product experience acceptance is `accepted` or `not_required`;
3. technical review is `pass` or `not_required`;
4. delivery readiness is `merge_ready` or `not_required`;
5. merge authorization is `authorized` or `not_required`, and an authorized merge is completed when merge is in scope;
6. remaining obligations have an owner and state.
