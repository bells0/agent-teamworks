# Review and Acceptance Protocol

Use the cheapest independent control capable of protecting the outcome. Review, verification, and acceptance are different responsibilities.

## Review

Review compares the actual outcome and evidence with the accepted requirement. It returns a verdict and findings with location, impact, and correction.

- The implementer does not approve its own outcome.
- Review depth follows concrete risk, not team size or ritual.
- Re-review the fix boundary and prior findings; do not restart an unbounded review loop without new evidence.
- If review reveals a requirement misunderstanding, return to the decision or specification owner.

## Engineering verification

Verification observes the claim through the closest reliable path. It records the environment, action, result, and evidence scope.

Passing a schema check proves schema validity, not project usefulness. Passing a UI build proves compilation, not hands-on usability. Keep every claim within its evidence boundary.

## User acceptance

Use one of four states:

- `not_required` — no user-visible or designated-owner outcome needs acceptance;
- `pending` — engineering evidence exists but the acceptance owner has not decided;
- `accepted` — the acceptance owner exercised or reviewed the agreed outcome and approved it;
- `rejected` — the outcome does not satisfy the intended workflow.

Rejection caused by misunderstood intent returns to the owning decision or specification. A local defect returns to implementation. Do not label pending work complete merely because agents are idle.

## Completion rule

A work item becomes `done` only when:

1. required outputs exist;
2. material findings are resolved or explicitly accepted by the authorized owner;
3. engineering claims have proportionate evidence;
4. user acceptance is `accepted` or `not_required`;
5. remaining obligations have an owner and state.
