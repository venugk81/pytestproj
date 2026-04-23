import pytest
@pytest.mark.parametrize("data", [
    {"input": 1, "expected": 2},
    {"input": 2, "expected": 4},
])
def test_double(data):
    assert data["input"] * 2 == data["expected"]