# More-information request review

## Purpose

This document records the complete remediation of the team’s more-information request:

1. bind capability and policy lifecycle operations to authenticated on-chain owners;
2. commit every routing input that can affect selection in persisted hashes and receipts; and
3. make a no-match result testable and durable without validator rejection or transaction reversion.

The source, deployment, tests, and live evidence described here are aligned to the same final release.

## Final release identity

- Network: Studionet, chain ID `61999`
- Contract: [`0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335`](https://explorer-studio.genlayer.com/address/0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335)
- Deployment transaction: [`0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb`](https://explorer-studio.genlayer.com/tx/0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb)
- Deployment status: finalized with majority agreement
- Deployed-source normalized SHA-256: `c4be668ca7918fd9064f539fb20881afd8bb8138833f51a00362ff9a6ba1ef7b`
- Workspace source: [contracts/waymark.py](contracts/waymark.py)

The deployed source was read back from Studionet and matched the workspace source after removing the CLI response wrapper. This prevents the documentation, source, and deployed contract from describing different releases.

## Request item 1: authenticated ownership

### Problem addressed

Ownership must not be supplied as arbitrary caller text. A caller-supplied owner field can be forged, can diverge from the transaction signer, and makes authorization difficult to audit.

### Source changes

- `Capability.owner`, `Manifest.owner`, and `Policy.owner` are typed as on-chain `Address` values.
- `_sender()` returns `gl.message.sender_address`, the authenticated sender for the current transaction.
- `register` stores the authenticated sender as the capability owner.
- `register_policy` stores the authenticated sender as the policy owner.
- `configure(key, tags, policy)` no longer accepts an owner argument. It loads the persisted capability and requires the authenticated sender to equal its owner.
- `deactivate(key)` requires the authenticated sender to equal the persisted capability owner.
- `deactivate_policy(name)` requires the authenticated sender to equal the persisted policy owner.
- Ownership is included in manifest, policy, and catalog commitments so a change of owner cannot be hidden from consumers.

### Live evidence

The final deployer/catalog owner was `0x82dcdc5b028a13f3475ddec31b5300acfe9815d1`.

- `food_cold_chain` registration: [`0x344d1713fa0944ccb2d86a7c51e71181285cc5a9b4ebaa28c2f50658598b5565`](https://explorer-studio.genlayer.com/tx/0x344d1713fa0944ccb2d86a7c51e71181285cc5a9b4ebaa28c2f50658598b5565)
- `carbon_assurance` registration: [`0xc4887dde72cce9f7a1b36efec33117a6b84ba8f6223cc33f51a7b4d8f79edcff`](https://explorer-studio.genlayer.com/tx/0xc4887dde72cce9f7a1b36efec33117a6b84ba8f6223cc33f51a7b4d8f79edcff)
- Unauthorized configure attempt from `0x8D4E752AE688C21eC7C7D4d8a232B5e0700DBf0f`: [`0x3b1bde6ba577c3fe97d229ff26ccbcba52a0c74a73f89ff81ad566d5483404ee`](https://explorer-studio.genlayer.com/tx/0x3b1bde6ba577c3fe97d229ff26ccbcba52a0c74a73f89ff81ad566d5483404ee). Finalized leader result: `rollback: owner only`.
- Post-attempt manifest readback confirmed the original owner, tags, policy, revision, and manifest hash were unchanged.

Policy lifecycle was also exercised with the owner-created `evidence_router_final` policy:

- creation: [`0x47c7f6fd8f2ab5455ce7c32571f2fafcaecf8d9173fe54830de9462e7aae7a1d`](https://explorer-studio.genlayer.com/tx/0x47c7f6fd8f2ab5455ce7c32571f2fafcaecf8d9173fe54830de9462e7aae7a1d)
- owner deactivation: [`0xc380dd221a7020c318c8b922c2a54af973e71b4d50b4b272decfb2092ecba197`](https://explorer-studio.genlayer.com/tx/0xc380dd221a7020c318c8b922c2a54af973e71b4d50b4b272decfb2092ecba197)
- `policy_is_active("evidence_router_final")` returned `false` without reverting.

## Request item 2: complete routing commitments

### Problem addressed

A route commitment is incomplete if a validator-visible input can change selection without changing the persisted receipt hash. The remediation covers the request, complete catalog, tags, per-capability policy, owner, revision, manifest hash, and selected global policy identity/content.

### Catalog commitment

`_catalog_hash` serializes the active candidates in canonical key order. For each candidate it commits:

- capability key;
- description;
- version;
- canonical tags;
- capability-specific policy;
- authenticated owner;
- revision; and
- the persisted manifest/definition hash.

Tags are validated, deduplicated, sorted, and persisted by `configure`, so equivalent tag inputs produce one canonical representation.

### Request and global-policy commitment

`_request_hash` serializes:

- request ID;
- request text;
- global policy name; and
- global policy hash.

The default route path uses the fixed identity `__waymark_default_v1__` and commits its content hash. Named policies use their persisted policy hash. This prevents a caller or consumer from treating two different policy definitions as the same routing context.

### Persisted receipt fields

Both `RouteAttempt` and `RouteReceipt` persist `request_hash`, `catalog_hash`, `policy_name`, and `policy_hash`. Final receipts additionally persist the selected key, selected capability version, selected manifest hash, attempt number, creator, status, and reason. A consumer can therefore verify the exact selection context without reconstructing undocumented inputs.

The final live catalog hash is:

`0500b5f7bace9e85bfb11b9a12bef20bccd8b337139e41a8f4a1ac9179e82566`

The default global policy hash is:

`8dfed6e69284aec732f8cd6e8d827f4db398e393fad1bed455e69512055ba41b`

## Request item 3: durable retryable no-match

### Problem addressed

Previously, a no-match could be rejected by validation or treated as an exception, which prevented a caller from recording a retryable outcome. That made “no suitable capability” indistinguishable from a failed transaction.

### Validation and state-transition changes

- The leader may return the exact canonical string `NONE`.
- The validator accepts `NONE` only when the validator independently returns the same exact `NONE` value.
- A validator still rejects malformed output, extra prose, inactive keys, unknown keys, and disagreement.
- When consensus selects `NONE`, the write appends a `RouteAttempt` with status `RETRYABLE`, empty selected key, and reason `no matching capability`.
- The same attempt stores request, catalog, global-policy name, and global-policy hash commitments.
- No final route is created and `route_count` is not incremented.
- The attempt is retriable under the bounded `MAX_ATTEMPTS` limit instead of reverting.

### Live no-match evidence

Request ID: `e2e_no_match_final_20261002`

- Transaction: [`0xa0ae439c3e688137602d5557cf5df1bd12dcfc53d5be84c09850f4a754e88f6a`](https://explorer-studio.genlayer.com/tx/0xa0ae439c3e688137602d5557cf5df1bd12dcfc53d5be84c09850f4a754e88f6a)
- Consensus result: `NONE`
- Persisted receipt status: `RETRYABLE`
- Selected capability: none
- Reason: `no matching capability`
- `count_routes()`: `2`, proving the attempt was committed without being counted as a final route

## Regression coverage

`tests/test_waymark.py` contains four source-level regression tests covering:

1. authenticated ownership and the owner-free `configure` signature;
2. tags, capability policy, global policy identity/hash, and catalog-hash receipt fields;
3. validated `NONE` and durable `RETRYABLE` persistence; and
4. readable inactive-policy state after deactivation.

Verification completed:

```text
python3 -m pytest -q
4 passed
git diff --check
clean
```

The official linter command remains documented in `README.md`. The deployed-source readback, AST/source checks, and live finalized transactions are the release evidence used for this submission.

## Final reviewer conclusion

All three requested remediation areas are implemented in the same source that is deployed at the final Studionet address. Ownership is signer-derived and enforced, every routing input that can affect selection is committed and exposed in receipts, and a consensus-agreed no-match is durably recorded as a retryable attempt without validator rejection or transaction reversion.
