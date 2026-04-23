import pytest
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 5, 35)
])

def test_fixture_method(a, b, expected):
    assert a+b == expected, "Values are not equal"
