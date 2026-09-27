# Waymark

Waymark is a reusable semantic capability-routing primitive. A caller submits an intent and a bounded set of registered capability descriptors; GenLayer validators independently classify which descriptor is the best fit. The contract then records a canonical route, definition hash, and deterministic usage counters.

Ordinary contracts can compare identifiers, but cannot safely decide whether an open-ended request matches a capability description. Waymark makes that semantic boundary consensus-backed while keeping registration, authorization, replay protection, limits, counters, and state transitions deterministic.

Status: deployed and exercised on stable Studionet. The lint-clean canonical deployment is `0xF3af2D9BFF8eb9Dc93A4617f046345D5CfbfFB2b`.

## Quick start

```bash
python3 -m pytest
.venv-linter/bin/genvm-lint check contracts/waymark.py
python3 scripts/check_studionet.py
```

The official linter is pinned in `requirements-dev.txt`. Install it with `python3 -m venv .venv-linter && .venv-linter/bin/python -m pip install -r requirements-dev.txt`.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/CONSENSUS.md](docs/CONSENSUS.md), and [docs/INTEGRATION.md](docs/INTEGRATION.md).

## Live proof

The lint-clean final source is commit `035e8bd`. Deployment transaction: [0xe9a418c25338a8bcb988840c58221a7f62119b7d2ec6cf9cd023254031897465](https://explorer-studio.genlayer.com/tx/0xe9a418c25338a8bcb988840c58221a7f62119b7d2ec6cf9cd023254031897465). Schema extraction and validation pass; see [DEPLOYMENT.md](DEPLOYMENT.md) for prior live route evidence.
