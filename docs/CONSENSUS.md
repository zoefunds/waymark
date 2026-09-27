# Consensus boundary

The leader and validators receive the same request and catalog. Each must return exactly one existing capability key. `gl.eq_principle_strict_eq` requires substantive output equality; JSON-shape agreement alone is not accepted. Deterministic code validates membership, replay, bounds, hashes, finality, and counters.

This is intentionally fail-closed: disagreement, unavailable web/LLM execution, `NONE`, extra prose, or a stale catalog produces no route record.
