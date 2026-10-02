# Threat model

Untrusted request, descriptions, tags, and policies are data, and the prompt explicitly ignores embedded instructions. A malicious leader cannot invent a key because strict equality and deterministic membership checks reject it. A caller cannot mutate another owner's catalog entry or policy because ownership is taken from the transaction sender and enforced for configuration/deactivation. A caller cannot replace a final route or substitute a catalog/global-policy commitment. Deactivation affects only future routes; historical records remain immutable.

The protocol does not solve provider Sybil identity, semantic ambiguity, validator collusion, or liveness outages. Inputs and catalog size are bounded to control state growth and prompt cost. It has no funds, so there are no stranded-bond or double-withdrawal paths.
