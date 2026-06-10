import pytest
from main import hello


def test_hello_with_name():
    assert hello("Anas") == "Hello, Anas!"


def test_hello_with_empty_string():
    assert hello("") == "Hello, !"


@pytest.mark.parametrize("name,expected", [
    ("World", "Hello, World!"),
    ("GitHub", "Hello, GitHub!"),
    ("123", "Hello, 123!"),
])
def test_hello_parametrized(name, expected):
    assert hello(name) == expected

