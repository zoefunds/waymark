# Consensus boundary

The leader and validators receive the same request, selected global policy, and catalog. The leader returns one key through `gl.nondet.exec_prompt`; validators independently execute the same bounded decision and compare the canonical output through `gl.vm.run_nondet_unsafe`. A validator rejects non-`Return` values, non-string values, inactive keys, and keys outside the catalog. `NONE` is explicitly valid when both executions agree, so deterministic code can commit a retryable no-match receipt. Deterministic code validates membership, bounds, ownership, hashes, finality, and counters.

This is intentionally fail-closed for disagreement, unavailable LLM execution, extra prose, malformed output, and stale/malformed catalog data. A consensus `NONE` is different: it deliberately creates a durable `RETRYABLE` attempt containing request, catalog, and global-policy commitments while leaving no final route record.
