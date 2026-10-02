# Integration

The current deployed address is `0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335` on Studionet.

1. Register a capability with a stable key and version. Its owner is the transaction sender. The live fixture uses `food_cold_chain` and `carbon_assurance`.
2. As that owner, call `configure(key, tags, capability_policy)`. There is no owner argument. Tags are canonicalized and persisted in the manifest.
3. Register a global policy from its owner, then route with `route_with_policy(request_id, request, policy_name)`. The default `route` path commits the fixed identity `__waymark_default_v1__` and its content hash.
4. Read `route_receipt(request_id)`. A `FINAL` receipt must be verified with its catalog hash, key, policy name, and policy hash. A `RETRYABLE` receipt is a committed no-match and may be retried using the same ID within the attempt limit.

The live final routes are `e2e_coldchain_final_20261002 → food_cold_chain` and `e2e_carbon_final_20261002 → carbon_assurance`. The live no-match `e2e_no_match_final_20261002` returns `RETRYABLE` and leaves `count_routes()` at `2`.

Never consume an unknown route, silently accept a changed catalog or global policy, or treat a failed transaction as a negative route. Only a committed `RETRYABLE` receipt is a no-match outcome.
