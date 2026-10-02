# Reviewer demo — final Studionet deployment

All commands below target the current finalized deployment:

- Contract: `0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335`
- Deployment: [`0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb`](https://explorer-studio.genlayer.com/tx/0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb)
- Source hash read back from chain: `c4be668ca7918fd9064f539fb20881afd8bb8138833f51a00362ff9a6ba1ef7b`

## Owner-bound catalog

The deployer `0x82dcdc5b028a13f3475ddec31b5300acfe9815d1` registered two real operational capabilities: `food_cold_chain` for temperature excursions, generator contingency, reefer dispatch, and spoilage evidence; and `carbon_assurance` for Scope 1/2 inventories, leased-refrigeration boundaries, evidence reconciliation, and audit workpapers. Both manifests persist that owner, canonical tags, capability policy, revision `2`, and a definition hash.

An unauthorized `configure` from `0x8D4E752AE688C21eC7C7D4d8a232B5e0700DBf0f` finalized with `rollback: owner only` in [`0x3b1bde6ba577c3fe97d229ff26ccbcba52a0c74a73f89ff81ad566d5483404ee`](https://explorer-studio.genlayer.com/tx/0x3b1bde6ba577c3fe97d229ff26ccbcba52a0c74a73f89ff81ad566d5483404ee).

## Semantic routes

- Cold-chain resilience planning selected `food_cold_chain`, `FINAL`: [`0x9b1c90f910cbf097a4e367b4ba3e08afbb3a3658ca43e01c51868563d267ebec`](https://explorer-studio.genlayer.com/tx/0x9b1c90f910cbf097a4e367b4ba3e08afbb3a3658ca43e01c51868563d267ebec)
- Carbon-assurance training selected `carbon_assurance`, `FINAL`: [`0xf9226a1707513deb5f7e9b37319da54bbdc9678c729c3579e19025a112de987d`](https://explorer-studio.genlayer.com/tx/0xf9226a1707513deb5f7e9b37319da54bbdc9678c729c3579e19025a112de987d)

Both receipts commit catalog hash `0500b5f7bace9e85bfb11b9a12bef20bccd8b337139e41a8f4a1ac9179e82566` and default-policy hash `8dfed6e69284aec732f8cd6e8d827f4db398e393fad1bed455e69512055ba41b`.

## Durable no-match

An unrelated municipal water-treatment maintenance training request finalized with consensus `NONE` and persisted `RETRYABLE` in [`0xa0ae439c3e688137602d5557cf5df1bd12dcfc53d5be84c09850f4a754e88f6a`](https://explorer-studio.genlayer.com/tx/0xa0ae439c3e688137602d5557cf5df1bd12dcfc53d5be84c09850f4a754e88f6a). Its receipt has no selected key, retains all commitments, and `count_routes()` remains `2`.

## Policy lifecycle

The owner-created `evidence_router_final` policy was finalized and then owner-deactivated in [`0xc380dd221a7020c318c8b922c2a54af973e71b4d50b4b272decfb2092ecba197`](https://explorer-studio.genlayer.com/tx/0xc380dd221a7020c318c8b922c2a54af973e71b4d50b4b272decfb2092ecba197). The corrected `policy_is_active` view returned `false` rather than reverting.
