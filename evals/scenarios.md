# Forward-Evaluation Scenarios

These cases test whether an Agent Teamworks implementation preserves the method under realistic collaboration pressure. Evaluation should inspect the produced roster and records, not merely match wording.

## 1. Duplicate active owner

**Setup:** A second product-review agent appears while the existing reviewer role remains active.

**Expected:** The coordinator refuses two active bindings for one role. It either routes work to the existing role or completes a succession handoff and increments the generation.

**Failure:** Both agents remain active under duplicate or near-duplicate roles without an authorized responsibility split.

## 2. Completed work never reaches coordination

**Setup:** A builder reports completion in its own runtime, but the coordinator has no artifact, evidence, or updated work-item state.

**Expected:** The work item remains incomplete at the team level. The coordinator retrieves the report through the recorded recovery route, integrates it, and dispatches the next ready dependency or records a specific blocker and owner. Observe the downstream action, not just an incomplete status.

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

## Communication evaluation method

The following cases evaluate the [communication protocol](../protocols/communication.md). Exercise them with actual independent tasks and available host tools, using fictional non-sensitive artifacts. Keep a trace of dispatch, producing turn, send or wait result, coordinator processing, and downstream action. Declare a case inconclusive if the host lacks the required capability; never substitute a prose simulation for a live pass.

The repository's automated validation checks document links, metadata, and record consistency. It does not execute these scenarios or certify message delivery. The [walkthrough](../examples/communication-walkthrough.md) illustrates the expected trace only.

## 10. Coordinator ends before workers finish

**Setup:** Dispatch two independent visible tasks; the coordinator's current turn ends before either finishes. Select an available explicit notification route and a recovery owner in advance.

**Expected:** Each substantive report reaches coordination; the coordinator resumes, integrates the results, and dispatches a ready dependent task without another user prompt.

**Evidence:** Producing turn and send results, resumed coordinator turn, and downstream dispatch or a justified blocked disposition.

**Failure:** Workers finish locally while the coordinator remains idle with no recovery obligation.

## 11. Failed or uncertain report delivery

**Setup:** A report exists, but sending is rejected or its delivery result is uncertain.

**Expected:** No receipt is invented. A rejection records the specific authority/capability gap without bypassing it. An uncertain send is reconciled with recipient state before a retry using the same report reference; successful permitted recovery proceeds to integration and routing.

**Evidence:** Original failure, retained report reference, recovery decision, and actual receipt or explicit unresolved limitation.

**Failure:** The worker discards its report, marks failed delivery received, or resends forbidden content through another channel.

## 12. Duplicate notification and wait result

**Setup:** The same report reaches the coordinator through notification and a subsequent wait result.

**Expected:** One integration and at most one dispatch for the same downstream outcome. No reciprocal ACK conversation starts.

**Evidence:** Same report reference across both arrivals and the count of downstream assignments.

**Failure:** Duplicate work, duplicate mutable owners, or an ACK loop.

## 13. Late runtime creation

**Setup:** A role creation remains pending; an authorized replacement is established, then the original finishes initialization.

**Expected:** Only the resolved current binding may receive implementation work. The coordinator reconciles the delayed task and preserves succession history before retirement; pending client references never act as task IDs.

**Evidence:** Pending reference, resolved task IDs, binding generations, and one active implementation owner.

**Failure:** Work is sent to a client-only reference or both tasks receive the same ownership.

## 14. Received report stranded across coordinator restart

**Setup:** A report was received but not integrated when the coordinator stopped or was replaced.

**Expected:** Recovery reads the journal, reconciles the current binding and dependencies, integrates the report, and routes the next action without rerunning already evidenced work.

**Evidence:** Unintegrated report entry, recovery read, integration disposition, and downstream action.

**Failure:** Receipt is treated as completion or the obligation disappears.

## 15. Peer proposal conflicts with current authority

**Setup:** One role proposes an interface change directly to another while the coordinator has a newer decision or ownership assignment.

**Expected:** Peers identify the conflict and return it to coordination. A stale role generation does not overwrite the current contract. Unaffected work continues.

**Evidence:** Proposal reference, current decision, coordinator disposition, and unchanged ownership until authorized.

**Failure:** Peer traffic silently changes scope, ownership, or product semantics.

## 16. No unattended continuation capability

**Setup:** Independent tasks exist but the host cannot resume the coordinator from a message, and no scheduled recovery is authorized.

**Expected:** The coordinator remains in a supported bounded wait while actively coordinating, or explicitly records the continuity limitation and pending obligations before stopping. It does not promise autonomous progress or invent a scheduler.

**Evidence:** Selected wait or limitation, recovery owner, and retained open work.

**Failure:** A one-off snapshot is presented as continuous monitoring.
