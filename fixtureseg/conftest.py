import pytest

test_data = []

@pytest.fixture(scope="module")
def before_module():
    print("before module scope executed 2")
    yield
    print("after module scope executed")

@pytest.fixture(scope="session")
def before_suite():
    test_data = [10, 42, 52, 53, 664]
    print("before suite executed 1")
    yield
    print("after suite executed 2")

@pytest.fixture(scope="function")
def before_function():
    print("before function scope executed 3")
    yield
    print("after function scope executed 1")


