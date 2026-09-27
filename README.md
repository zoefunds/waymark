# Waymark

Waymark is a reusable semantic capability-routing primitive. A caller submits an intent and a bounded set of registered capability descriptors; GenLayer validators independently classify which descriptor is the best fit. The contract then records a canonical route, definition hash, and deterministic usage counters.

Ordinary contracts can compare identifiers, but cannot safely decide whether an open-ended request matches a capability description. Waymark makes that semantic boundary consensus-backed while keeping registration, authorization, replay protection, limits, counters, and state transitions deterministic.

Status: implementation and local verification complete. Stable Studionet deployment requires a funded account and a concrete target repository.

## Quick start

```bash
python3 -m pytest
genvm-linter contracts/waymark.py
python3 scripts/check_studionet.py
```

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [docs/CONSENSUS.md](docs/CONSENSUS.md), and [docs/INTEGRATION.md](docs/INTEGRATION.md).

