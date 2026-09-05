# Fictional Communication Walkthrough

This example uses imaginary role and task references. It is not a runtime execution log.

A catalog builder and frontend builder are working in separate visible tasks. The coordinator uses explicit result notification; the adapter has confirmed that the host can resume the coordinator when notified.

| Step | Observable event | Coordinator disposition |
|---|---|---|
| 1 | Dispatch catalog work to catalog-role generation 1; report target is task-coordinator | Record notification route; coordinator owns recovery on the next agreed check |
| 2 | Catalog builder writes artifact catalog-contract-v1 and ends locally without sending | Produced only; frontend remains blocked |
| 3 | Recovery retrieves report catalog-turn-7 from the catalog task | Received; do not repeat the catalog investigation |
| 4 | Coordinator checks the contract against current requirements | Integrated; product and technical acceptance remain separate |
| 5 | Coordinator sends the contract and frontend assignment to task-frontend | Routed; frontend begins consuming the contract |
| 6 | Catalog builder retries report catalog-turn-7 after an uncertain earlier send | Recognize the existing reference; no duplicate frontend assignment |
| 7 | Frontend requests a shared-field change | Coordinator records the decision before directing either owner to change the contract |

An equivalent successful path sends catalog-turn-7 at step 2, resumes coordination, and proceeds directly to integration and routing. Merely recording the notification route does not prove it worked.

If the host cannot resume the coordinator and no coordinator wait or authorized follow-up remains active, record the continuity limitation rather than describing the team as autonomously progressing.

The coordinator's compact journal preserves the selected route, report reference, observed receipt, integration decision, next owner, and any pending check. Existing JSON acceptance fields are untouched. See the [communication protocol](../protocols/communication.md) and [evaluation scenarios](../evals/scenarios.md).
