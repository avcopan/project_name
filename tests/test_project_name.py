"""project_name tests."""

import project_name


def test_stub() -> None:
    """Stub test to ensure the test suite runs."""
    print(project_name.__version__)  # noqa: T201


def test__greet() -> None:
    """Test the greet function."""
    assert project_name.greet("World") == "Hello, World!"


def test__greet_jim() -> None:
    """Test the greet_jim function."""
    assert project_name.greet_jim() == "Hello, Jim!"
