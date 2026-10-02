# Waymark

Waymark is a reusable semantic capability-routing primitive. A caller submits an intent and a bounded set of registered capability descriptors; GenLayer validators independently classify which descriptor is the best fit. Capability and global-policy ownership is bound to the authenticated on-chain sender, and every receipt commits the complete router input set: request, catalog, tags, capability policies, global-policy name, and global-policy hash.

Ordinary contracts can compare identifiers, but cannot safely decide whether an open-ended request matches a capability description. Waymark makes that semantic boundary consensus-backed while keeping registration, authorization, replay protection, limits, counters, and state transitions deterministic.

Status: deployed and finalized on Studionet at [`0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335`](https://explorer-studio.genlayer.com/address/0x8a75685ae363d46fd0f259FEbfe9Ba86112EC335).

## Quick start

```bash
python3 -m pytest
.venv-linter/bin/genvm-lint check contracts/waymark.py
python3 scripts/check_studionet.py
```

The official linter is pinned in `requirements-dev.txt`. Install it with `python3 -m venv .venv-linter && .venv-linter/bin/python -m pip install -r requirements-dev.txt`.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/CONSENSUS.md](docs/CONSENSUS.md), and [docs/INTEGRATION.md](docs/INTEGRATION.md).

## Ownership and retry semantics

`register` and `register_policy` bind the owner to `gl.message.sender_address`. Only that address may call `configure`, `deactivate`, or `deactivate_policy`; `configure` no longer accepts an owner string. A consensus `NONE` result is a successful, durable `RETRYABLE` attempt rather than a reverted transaction. Read it through `route_receipt(request_id)` or `get_latest_attempt(request_id)` and retry the same ID up to the bounded attempt limit.

## Deployment

The current deployment transaction is [`0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb`](https://explorer-studio.genlayer.com/tx/0xfba60164eceac7d90409d87cfa1ffc9b9d2e3df8c0b156de1fa523c0230f4bfb). Two finalized E2E routes, a finalized durable no-match, and finalized owner-negative/lifecycle checks are recorded in [DEPLOYMENT.md](DEPLOYMENT.md).
