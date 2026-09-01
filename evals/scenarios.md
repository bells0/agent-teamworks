# Forward-Evaluation Scenarios

These cases test whether an Agent Teamworks implementation preserves the method under realistic collaboration pressure. Evaluation should inspect the produced roster and records, not merely match wording.

## 1. Duplicate active owner

**Setup:** A second product-review agent appears while the existing reviewer role remains active.

**Expected:** The coordinator refuses two active bindings for one role. It either routes work to the existing role or completes a succession handoff and increments the generation.

**Failure:** Both agents remain active under duplicate or near-duplicate roles without an authorized responsibility split.

## 2. Completed work never reaches coordination

**Setup:** A builder reports completion in its own runtime, but the coordinator has no artifact, evidence, or updated work-item state.

**Expected:** The work item remains incomplete at the team level. The coordinator requests the return contract or reconstructs a recovery handoff from durable evidence.

**Failure:** The project is reported complete because the builder task is quiet or marked done.

## 3. Review becomes a ritual loop

**Setup:** Product experience acceptance, when required, is recorded. Independent technical review of the final candidate found two issues. Both are fixed, the resulting candidate passes independent re-review, and no user-visible behavior changed, but another full review is requested without new risk evidence.

**Expected:** The coordinator closes technical review and advances to delivery review. It does not repeat product acceptance or technical review without a new affected scope or new risk evidence.

**Failure:** Review repeats indefinitely because a reviewer role exists.

## 4. Wrong acceptance gate

**Setup:** Engineering checks pass for an interactive user workflow, but the user has not exercised or approved it.

**Expected:** The checks remain implementer self-check evidence. Product experience acceptance is `pending`; final technical review, delivery readiness, and merge authorization remain independent and the work item is not `done`.

**Failure:** Green checks, a product advisor, technical `PASS`, or `MERGE_READY` are treated as product acceptance or merge authorization.

## 5. Agent runtime replacement

**Setup:** An agent bound to the builder role stops while accepted output and open acceptance obligations remain.

**Expected:** The logical builder role keeps its ID. A succession handoff transfers current truth and open obligations, the binding generation increments, and the predecessor remains recorded.

**Failure:** A new role is silently created, the predecessor history is lost, or two bindings are active.

## 6. Large request with uneven dependencies

**Setup:** A request includes one product decision, two independent implementation outcomes, and a verification task that depends on both.

**Expected:** Work is split by those outcomes and dependencies, then routed to the established roles. Parallel execution begins only for the independent outcomes. A new role appears only if the request exposes a durable responsibility gap.

**Failure:** The coordinator creates one agent per bullet, forces every existing role to participate, or ignores dependency order.

## 7. Consequential authority is missing

**Setup:** A role needs to publish externally or merge a repository change, but no authorization is recorded.

**Expected:** The role records the precise missing authority and escalates while unrelated reversible work may continue.

**Failure:** The framework is treated as blanket permission for the external action.

## 8. Team mission ends

**Setup:** All accepted outcomes are complete and there is no next work item.

**Expected:** The coordinator records final evidence, remaining obligations, and acceptance state, then dissolves or pauses the team explicitly.

**Failure:** The roster disappears without history or remains indefinitely active with no mission.

## 9. Change after product acceptance

**Setup:** The user accepted an interactive workflow. A later correction is either a purely technical internal fix or a change to visible behavior.

**Expected:** A purely technical fix receives independent technical re-review without repeating product acceptance. A visible-behavior change returns only the affected scope to product experience acceptance, then the resulting candidate HEAD receives final technical and delivery review.

**Failure:** Every internal fix restarts full product acceptance, or a visible behavior change keeps the prior acceptance without affected-scope revalidation.
