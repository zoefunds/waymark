# Waymark

Waymark is a reusable semantic capability-routing primitive. A caller submits an intent and a bounded set of registered capability descriptors; GenLayer validators independently classify which descriptor is the best fit. The contract then records a canonical route, definition hash, and deterministic usage counters.

Ordinary contracts can compare identifiers, but cannot safely decide whether an open-ended request matches a capability description. Waymark makes that semantic boundary consensus-backed while keeping registration, authorization, replay protection, limits, counters, and state transitions deterministic.

Status: deployed and exercised on stable Studionet. The audited canonical deployment is `0xFDe49237D70bA9F69594A395902FAE30F870Ae47`.

## Quick start

```bash
python3 -m pytest
genvm-linter contracts/waymark.py
python3 scripts/check_studionet.py
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/CONSENSUS.md](docs/CONSENSUS.md), and [docs/INTEGRATION.md](docs/INTEGRATION.md).

## Live proof

The audited final source is commit `2ee53bd`. Deployment transaction: [0xaeaa64f2e6f7528fb62a043db0fc4ea89228dc2651d293d98b3db6f047cc7a7f](https://explorer-studio.genlayer.com/tx/0xaeaa64f2e6f7528fb62a043db0fc4ea89228dc2651d293d98b3db6f047cc7a7f). A fresh semantic route finalized with status `FINAL`; see [DEPLOYMENT.md](DEPLOYMENT.md) for audit evidence.
