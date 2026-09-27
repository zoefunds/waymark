# Reviewer demo

Normal case: register `translate` and `summarize`, then route a request that clearly asks for a translation; the finalized route is `translate`.

Adversarial case: include instructions inside a capability description attempting to alter the classifier. Validators must treat it as data; disagreement or a non-key result fails closed.

Composition case: a consumer pins the definition hash, reads a finalized route, and dispatches only to the registered key. Deactivate the key and show that new routing cannot use it while the old record remains immutable.
