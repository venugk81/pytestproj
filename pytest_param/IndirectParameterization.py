import pytest

@pytest.fixture
def db(request):
    print("\n============fixture==================")
    print("Executing DB fixture")
    print(f"DB fixture is returning: 'DB connection to: {request.param}'")
    return f"DB connection to: {request.param}"

@pytest.mark.parametrize("db", ["sqlite", "postgres"], indirect=True)
def test_db(db):
    print("\n============Test case==================")
    print("test_db- executing test_db testcase")
    print("test_db - Printing DB connection: ", db)
    assert "DB connection" in db

# fixture executes first but in this case, parameter data is passed to fixture.


"""" below is direct parameterization"""
import pytest
@pytest.mark.parametrize("data", [
    {"input": 1, "expected": 2},
    {"input": 2, "expected": 4},
])
def test_double(data):
    assert data["input"] * 2 == data["expected"]
# """