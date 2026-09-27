# Threat model

Untrusted request and descriptions are data, and the prompt explicitly ignores embedded instructions. A malicious leader cannot invent a key because strict equality and deterministic membership checks reject it. A caller cannot replay a request ID, mutate a final route, or substitute a different definition hash. Deactivation affects only future routes; historical records remain immutable.

The protocol does not solve provider Sybil identity, semantic ambiguity, validator collusion, or liveness outages. Inputs and catalog size are bounded to control state growth and prompt cost. It has no funds, so there are no stranded-bond or double-withdrawal paths.
