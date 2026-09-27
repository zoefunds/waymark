# Waymark

Waymark is a reusable semantic capability-routing primitive. A caller submits an intent and a bounded set of registered capability descriptors; GenLayer validators independently classify which descriptor is the best fit. The contract then records a canonical route, definition hash, and deterministic usage counters.

Ordinary contracts can compare identifiers, but cannot safely decide whether an open-ended request matches a capability description. Waymark makes that semantic boundary consensus-backed while keeping registration, authorization, replay protection, limits, counters, and state transitions deterministic.

Status: deployed and exercised on stable Studionet. The canonical deployment is `0x83cC3AB177CEFf2974fD4BFD9393693756bb7344`.

## Quick start

```bash
python3 -m pytest
genvm-linter contracts/waymark.py
python3 scripts/check_studionet.py
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/CONSENSUS.md](docs/CONSENSUS.md), and [docs/INTEGRATION.md](docs/INTEGRATION.md).

## Live proof

The final source is commit `3d3f14f`. Deployment transaction: [0x0d5c4a554830169e836b09823c8722afc32f847b7c6cfcd26614f7a0cd9d8bfd](https://explorer-studio.genlayer.com/tx/0x0d5c4a554830169e836b09823c8722afc32f847b7c6cfcd26614f7a0cd9d8bfd). Two real semantic routes finalized with status `FINAL`; see [DEPLOYMENT.md](DEPLOYMENT.md) for every transaction and resulting state.
