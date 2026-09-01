# Work Item Schema 0.2.0 Migration

Work Item Schema `0.2.0` replaces the two-field acceptance model with four independent product, technical, delivery, and authorization states. Other Agent Teamworks record schemas remain at `0.1.0` because their contracts do not change.

## Field migration

| Work Item 0.1.0 | Work Item 0.2.0 |
|---|---|
| `acceptance.user` | `acceptance.product_experience` |
| `acceptance.engineering` | `acceptance.technical_review` after evidence qualification |
| no equivalent | `acceptance.delivery_readiness` |
| no equivalent | `acceptance.merge_authorization` |
| `status: user_acceptance` | `status: product_acceptance` |
| `status: review` or `verification` | `status: technical_review` or `delivery_review`, according to the actual gate |

Do not automatically convert `engineering: passed` into `technical_review: pass`. An implementer self-check or pre-acceptance verification remains evidence, not final technical `PASS`. Use `pass` only when an independent reviewer or verifier evaluated the final candidate HEAD after required product experience acceptance.

Initialize new fields as follows:

- use `pending` when the gate applies but has not been decided;
- use `not_required` only when the project outcome does not require that gate;
- use `merge_ready` only after the delivery review covers scope, risk, rollback, checks, and PR or delivery evidence;
- use `authorized` only when the authority defined by project rules has authorized merge.

## Completion

A migrated work item is `done` only when product experience acceptance is `accepted` or `not_required`, technical review is `pass` or `not_required`, delivery readiness is `merge_ready` or `not_required`, merge authorization is `authorized` or `not_required`, and an authorized merge is complete when merge is in scope.
