# Deployment and live proof

Network preflight was run immediately before deployment:

- Network alias: `studionet`
- Chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- Explorer: `https://explorer-studio.genlayer.com`
- Runtime header: `py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6`
- Source commit: `3d3f14f`

## Contract

- Address: `0x83cC3AB177CEFf2974fD4BFD9393693756bb7344`
- Deployment transaction: [0x0d5c4a554830169e836b09823c8722afc32f847b7c6cfcd26614f7a0cd9d8bfd](https://explorer-studio.genlayer.com/tx/0x0d5c4a554830169e836b09823c8722afc32f847b7c6cfcd26614f7a0cd9d8bfd)
- Finalized: yes
- Final definition hash after registration: `ccd4f1ee37c1eefe298425ba64a9c5936daf0158ed35be8cc765c7b5722bf9c4`

## Finalized lifecycle

The non-admin writes were executed with real domain data. `configure`, `activate`, `deactivate`, and `deactivate_policy` were intentionally excluded as administrative mutations.

| Method | Purpose | Finalized transaction |
|---|---|---|
| `register` | Climate-risk capability for flood, transition, and lender-review analysis | [0xcd295df15c1feae08fe2ba6c9f10d7f3b6a0e798bc496a092aab5efe986f4b69](https://explorer-studio.genlayer.com/tx/0xcd295df15c1feae08fe2ba6c9f10d7f3b6a0e798bc496a092aab5efe986f4b69) |
| `register` | Carbon-accounting capability for Scope 1/2 and reporting boundaries | [0x21d133e04caad0ffe9c575f0f17ebddf9542f79f9e569742a41f0666c6b1d288](https://explorer-studio.genlayer.com/tx/0x21d133e04caad0ffe9c575f0f17ebddf9542f79f9e569742a41f0666c6b1d288) |
| `register_policy` | Evidence-first routing policy | [0x234ab653d807efc5907928078e220318b15726386f29d635a96ff08615443160](https://explorer-studio.genlayer.com/tx/0x234ab653d807efc5907928078e220318b15726386f29d635a96ff08615443160) |
| `route` | Lagos food distributor climate-risk request | [0xf5aa6725d5a1df7f7c4fcc6ade4c9bb69957721098320340630d6d485964f4da](https://explorer-studio.genlayer.com/tx/0xf5aa6725d5a1df7f7c4fcc6ade4c9bb69957721098320340630d6d485964f4da) |
| `route_with_policy` | Nigerian manufacturer Scope 1/2 assurance request | [0x07cca860ef345bde1c857a03e7d6a8f90fa3bcb6b82f7c8b973e35fc665ceb24](https://explorer-studio.genlayer.com/tx/0x07cca860ef345bde1c857a03e7d6a8f90fa3bcb6b82f7c8b973e35fc665ceb24) |

All five lifecycle writes reached `FINALIZED` with majority validator agreement. Final reads returned `count_routes = 2`; both route records had `status = FINAL`, with `climate_risk` and `carbon_accounting` selected respectively.
