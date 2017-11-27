import pytest

@pytest.mark.vcr()
def test_instance(mastodon):
    instance = mastodon.instance()

    assert isinstance(instance, dict)  # hehe, instance is instance

    expected_keys = set(('description', 'email', 'title', 'uri', 'version', 'urls'))
    assert set(instance.keys()) >= expected_keys
