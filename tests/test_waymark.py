import hashlib
import json
import pytest

from contracts.waymark import Waymark, Capability


def test_definition_hash_is_order_independent():
    a = [Capability("a", "one", "1", True), Capability("b", "two", "1", True)]
    b = list(reversed(a))
    assert Waymark._definition_hash(a) == Waymark._definition_hash(b)


def test_definition_hash_pins_semantics():
    a = [Capability("a", "one", "1", True)]
    b = [Capability("a", "changed", "1", True)]
    assert Waymark._definition_hash(a) != Waymark._definition_hash(b)


def test_bounds_reject_untrusted_text():
    with pytest.raises(ValueError):
        Waymark._check_text("x" * 513)

