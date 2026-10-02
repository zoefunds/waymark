# Current audited deployment and live proof

## Deployment

- Network: Studionet (chain ID 61999)
- Contract: [0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335](https://explorer-studio.genlayer.com/address/0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335)
- Deployment transaction: [0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb](https://explorer-studio.genlayer.com/tx/0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb)
- Deployment state: finalized, majority agreement
- Authenticated deployer and catalog owner: 0x82dcdc5b028a13f3475ddec31b5300acfe9815d1

The deployed source was read back from Studionet and matches
[contracts/waymark.py](contracts/waymark.py) exactly after removal of the
CLI response wrapper. Normalized SHA-256:
c4be668ca7918fd9064f539fb20881afd8bb8138833f51a00362ff9a6ba1ef7b.

## Owner-bound catalog configuration

The same on-chain owner registered and configured two active capabilities.
Each manifest stores its owner, canonical tags, capability policy, revision,
and manifest hash:

| Capability | Registration | Configuration |
|---|---|---|
| food_cold_chain | [0x344d1713fa0944ccb2d86a7c51e71181285cc5a9b4ebaa28c2f50658598b5565](https://explorer-studio.genlayer.com/tx/0x344d1713fa0944ccb2d86a7c51e71181285cc5a9b4ebaa28c2f50658598b5565) | owner-configured; verified by final manifest readback |
| carbon_assurance | [0xc4887dde72cce9f7a1b36efec33117a6b84ba8f6223cc33f51a7b4d8f79edcff](https://explorer-studio.genlayer.com/tx/0xc4887dde72cce9f7a1b36efec33117a6b84ba8f6223cc33f51a7b4d8f79edcff) | [0x29eb8f893a797e1f5179489b48780843b43b501a9688d1436b1ab2246341f98b](https://explorer-studio.genlayer.com/tx/0x29eb8f893a797e1f5179489b48780843b43b501a9688d1436b1ab2246341f98b) |

The deployed ABI confirms configure(key, tags, policy) has no owner parameter.
register, register_policy, configure, deactivate, and deactivate_policy derive
or enforce ownership from gl.message.sender_address.

On the final deployment, owner policy lifecycle was also finalized: policy
`evidence_router_final` was created in [0x47c7f6fd8f2ab5455ce7c32571f2fafcaecf8d9173fe54830de9462e7aae7a1d](https://explorer-studio.genlayer.com/tx/0x47c7f6fd8f2ab5455ce7c32571f2fafcaecf8d9173fe54830de9462e7aae7a1d), deactivated in [0xc380dd221a7020c318c8b922c2a54af973e71b4d50b4b272decfb2092ecba197](https://explorer-studio.genlayer.com/tx/0xc380dd221a7020c318c8b922c2a54af973e71b4d50b4b272decfb2092ecba197), and `policy_is_active` returned `false`.

The final-deployment unauthorized configuration attempt from
`0x8D4E752AE688C21eC7C7D4d8a232B5e0700DBf0f` finalized with `rollback: owner only`:
[0x3b1bde6ba577c3fe97d229ff26ccbcba52a0c74a73f89ff81ad566d5483404ee](https://explorer-studio.genlayer.com/tx/0x3b1bde6ba577c3fe97d229ff26ccbcba52a0c74a73f89ff81ad566d5483404ee).

## Finalized semantic routes

| Test | Finalized transaction | Persisted result |
|---|---|---|
| Detailed cold-chain resilience planning: temperature logs, generator contingency, reefer dispatch, spoilage containment, evidence checklist | [0x9b1c90f910cbf097a4e367b4ba3e08afbb3a3658ca43e01c51868563d267ebec](https://explorer-studio.genlayer.com/tx/0x9b1c90f910cbf097a4e367b4ba3e08afbb3a3658ca43e01c51868563d267ebec) | food_cold_chain, FINAL |
| Detailed carbon-assurance training: Scope 1, Scope 2, leased refrigeration boundary, evidence reconciliation, audit workpapers | [0xf9226a1707513deb5f7e9b37319da54bbdc9678c729c3579e19025a112de987d](https://explorer-studio.genlayer.com/tx/0xf9226a1707513deb5f7e9b37319da54bbdc9678c729c3579e19025a112de987d) | carbon_assurance, FINAL |

Both live receipts commit:

- catalog hash: 0500b5f7bace9e85bfb11b9a12bef20bccd8b337139e41a8f4a1ac9179e82566
- global policy name: __waymark_default_v1__
- global policy hash: 8dfed6e69284aec732f8cd6e8d827f4db398e393fad1bed455e69512055ba41b

The receipt also contains the request hash, selected capability, capability
version, selected manifest hash, creator, attempt, status, and reason.

## Finalized durable no-match

The unrelated public water-treatment maintenance training scenario finalized
with consensus result NONE:
[0xa0ae439c3e688137602d5557cf5df1bd12dcfc53d5be84c09850f4a754e88f6a](https://explorer-studio.genlayer.com/tx/0xa0ae439c3e688137602d5557cf5df1bd12dcfc53d5be84c09850f4a754e88f6a).

route_receipt("e2e_no_match_final_20261002") returns RETRYABLE, no
capability key, reason "no matching capability", and durable request/catalog/
global-policy commitments. count_routes() remains 2, demonstrating that the
attempt committed without reverting or being counted as a final route.

## Verification commands

    python3 -m pytest -q
    genlayer code 0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335
    genlayer schema 0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335
    genlayer call 0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335 route_receipt --args e2e_coldchain_final_20261002
    genlayer call 0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335 route_receipt --args e2e_no_match_final_20261002
