import pytest
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_multiply(x, y):
    print(x, " * ", y, ' = ', x*y)
    assert x * y in [10, 20, 41]