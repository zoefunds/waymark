# Consensus boundary

The leader and validators receive the same request and catalog. The leader returns one key through `gl.nondet.exec_prompt`; validators independently execute the same bounded decision and compare only the canonical key through `gl.vm.run_nondet_unsafe`. A validator rejects non-`Return` values, non-string values, `NONE`, inactive keys, and keys outside the catalog. Deterministic code validates membership, replay, bounds, hashes, finality, and counters.

This is intentionally fail-closed: disagreement, unavailable web/LLM execution, `NONE`, extra prose, or a stale catalog produces no route record.
