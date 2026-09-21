import funservice


def test_version_is_public():
    assert funservice.__version__ == "0.0.2"


def test_version_is_semver_like():
    parts = funservice.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
