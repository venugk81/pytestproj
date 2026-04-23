import pytest


@pytest.fixture(scope="function")
def before_test():
    print("before test executed: ")
    yield
    print("after test executed: ")

def test_tc001_login(before_test):
    print("loging test 1")
    assert 1==2

def test_tc002_login(before_test):
    print("login test 2")
    assert 1==1