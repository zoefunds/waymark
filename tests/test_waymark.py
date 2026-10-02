from pathlib import Path


SOURCE = Path(__file__).parents[1] / "contracts" / "waymark.py"


def source() -> str:
    return SOURCE.read_text()


def test_authenticated_ownership_is_part_of_the_contract_surface():
    code = source()
    assert "owner: Address" in code
    assert "return gl.message.sender_address" in code
    assert "def configure(self, key: str, tags: str, policy: str)" in code
    assert "def _require_owner(self, owner: Address)" in code
    assert code.count("self._require_owner(") >= 2


def test_selection_inputs_are_committed_in_receipt_fields_and_hashes():
    code = source()
    assert "policy_name: str" in code
    assert "policy_hash: str" in code
    assert '"tags": item.tags' in code
    assert '"policy": item.policy' in code
    assert '"policy_name": policy_name' in code
    assert '"policy_hash": policy_hash' in code
    assert "catalog_hash: str" in code


def test_none_is_validated_then_persisted_as_retryable_without_revert():
    code = source()
    assert 'chosen != "NONE" and chosen not in valid' in code
    assert 'validator_choice == chosen and (chosen == "NONE" or chosen in valid)' in code
    assert 'if selected == "NONE":' in code
    assert '"no matching capability"' in code
    assert "STATUS_RETRYABLE" in code
    assert 'raise gl.vm.UserError("no canonical route")' not in code


def test_deactivated_policy_can_be_read_as_inactive():
    code = source()
    start = code.index("def policy_is_active")
    end = code.index("def active_keys", start)
    section = code[start:end]
    assert "return self.policies[name].active" in section
