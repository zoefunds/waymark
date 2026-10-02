# Architecture

Waymark turns an open-ended intent into a canonical capability key. Registration and all state mutation are deterministic. Registration binds each capability and policy to `gl.message.sender_address`; configuration and deactivation compare that authenticated address to the persisted owner. Only the semantic mapping from request text to one registered key is delegated to GenLayer consensus.

Actors are capability providers, callers, and validators. State consists of immutable capability descriptors, retryable attempts, final route records, and a bounded counter. A catalog hash pins the complete active catalog used by the semantic decision.

Validators independently inspect the same bounded catalog and request. Strict equality rejects disagreement, malformed output, inactive keys, and prompt-injection attempts. `NONE` is deliberately valid when both leader and validator select it: the write commits a `RETRYABLE` attempt with request, catalog, policy-name, and policy-hash commitments, rather than reverting. The catalog hash includes descriptions, versions, tags, capability policies, owners, revisions, and manifest hashes. Consumers must pin the contract address, catalog hash, selected key, and global policy identity/hash.

Non-goals: identity, payments, ranking by model confidence, private evidence, arbitrary callbacks, and a product UI.
