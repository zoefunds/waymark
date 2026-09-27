# Architecture

Waymark turns an open-ended intent into a canonical capability key. Registration and all state mutation are deterministic. Only the semantic mapping from request text to one registered key is delegated to GenLayer consensus.

Actors are capability providers, callers, and validators. State consists of immutable capability descriptors, one-shot route records, and a bounded counter. A route is `FINAL` or absent; final records cannot be rewritten. The definition hash pins the active catalog used by the semantic decision.

Validators independently inspect the same bounded catalog and request. Strict equality rejects disagreement, malformed output, `NONE`, inactive keys, and prompt-injection attempts. Consumers must pin both the contract address and returned definition hash.

Non-goals: identity, payments, ranking by model confidence, private evidence, arbitrary callbacks, and a product UI.
