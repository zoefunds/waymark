# Deployment and live proof

Network preflight was run immediately before deployment:

- Network alias: `studionet`
- Chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- Explorer: `https://explorer-studio.genlayer.com`
- Runtime header: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`
- Source commit: `035e8bd`

## Contract

- Address: `0xF3af2D9BFF8eb9Dc93A4617f046345D5CfbfFB2b`
- Deployment transaction: [0xe9a418c25338a8bcb988840c58221a7f62119b7d2ec6cf9cd023254031897465](https://explorer-studio.genlayer.com/tx/0xe9a418c25338a8bcb988840c58221a7f62119b7d2ec6cf9cd023254031897465)
- Finalized: yes
- Definition hash read from the latest route record: `e4f6938d0377a3f816efc1dcf0ea7a1dadb768c9d3a9e0d6de2ce042eb215486`

## Finalized lifecycle

The non-admin writes were executed with real domain data. `configure`, `activate`, `deactivate`, and `deactivate_policy` were intentionally excluded as administrative mutations.

| Method | Purpose | Finalized transaction |
|---|---|---|
| `register` | Climate-risk capability for flood, transition, and lender-review analysis | [0xcd295df15c1feae08fe2ba6c9f10d7f3b6a0e798bc496a092aab5efe986f4b69](https://explorer-studio.genlayer.com/tx/0xcd295df15c1feae08fe2ba6c9f10d7f3b6a0e798bc496a092aab5efe986f4b69) |
| `register` | Carbon-accounting capability for Scope 1/2 and reporting boundaries | [0x21d133e04caad0ffe9c575f0f17ebddf9542f79f9e569742a41f0666c6b1d288](https://explorer-studio.genlayer.com/tx/0x21d133e04caad0ffe9c575f0f17ebddf9542f79f9e569742a41f0666c6b1d288) |
| `register_policy` | Evidence-first routing policy | [0x234ab653d807efc5907928078e220318b15726386f29d635a96ff08615443160](https://explorer-studio.genlayer.com/tx/0x234ab653d807efc5907928078e220318b15726386f29d635a96ff08615443160) |
| `route` | Lagos food distributor climate-risk request | [0xf5aa6725d5a1df7f7c4fcc6ade4c9bb69957721098320340630d6d485964f4da](https://explorer-studio.genlayer.com/tx/0xf5aa6725d5a1df7f7c4fcc6ade4c9bb69957721098320340630d6d485964f4da) |
| `route_with_policy` | Nigerian manufacturer Scope 1/2 assurance request | [0x07cca860ef345bde1c857a03e7d6a8f90fa3bcb6b82f7c8b973e35fc665ceb24](https://explorer-studio.genlayer.com/tx/0x07cca860ef345bde1c857a03e7d6a8f90fa3bcb6b82f7c8b973e35fc665ceb24) |

The audit redeployment was followed by a fresh registration transaction [0x5b890ee6e4c4a3953d32ac7b19ee5eb0036e4c4da8fd5329567937ec22306491](https://explorer-studio.genlayer.com/tx/0x5b890ee6e4c4da8fd5329567937ec22306491) and a fresh semantic route transaction [0xf5bebbe4e01145bf088f15b4a0452967a96d4ec29f85785d367250d9ae17de0a](https://explorer-studio.genlayer.com/tx/0xf5bebbe4e01145bf088f15b4a0452967a96d4ec29f85785d367250d9ae17de0a). Both finalized with majority validator agreement.

## Linter proof

`genvm-lint check contracts/waymark.py` passed AST lint, SDK validation, and schema extraction. The project pins `genvm-linter==0.11.0` in `requirements-dev.txt`.

## Latest live test

The latest lint-clean deployment was tested with a new registration [0x400b10f646736f2a1ba74cf6e032fd2809022c53ed5369cadb31a1f067e62d6c](https://explorer-studio.genlayer.com/tx/0x400b10f646736f2a1ba74cf6e032fd2809022c53ed5369cadb31a1f067e62d6c) and a bounded, detailed Lagos cold-chain route [0x80a96b4828501055716483c453589ce3379ad985734eda49a4006db2d59b84ba](https://explorer-studio.genlayer.com/tx/0x80a96b4828501055716483c453589ce3379ad985734eda49a4006db2d59b84ba). Both finalized; `count_routes` read back as `1`, and `get_route("climate-risk-lagos-cold-chain")` returned status `FINAL`, capability `climate_risk`, and reason `canonical consensus`.

An intentionally overlong route prompt was also tested and correctly rolled back with `text bound`, proving the input guard is active. The accepted prompt stayed within the contract's 512-character bound.
