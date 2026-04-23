import pytest

@pytest.mark.parametrize("a,b,expected", [
    pytest.param(1, 2, 3, id="valid"),
    pytest.param(1, 0, None, marks=pytest.mark.xfail, id="xfail_case"),
])
def test_cases(a, b, expected):
    if b == 0:
        assert False  # expected failure
    else:
        assert a + b == expected