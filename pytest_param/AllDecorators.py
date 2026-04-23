import pytest

# BeforeSuite equivalent
@pytest.fixture(scope="session", autouse=True)
def before_suite():
    print("\nBefore Suite")
    yield
    print("\nAfter Suite")

# BeforeTest equivalent (approx → module level)
@pytest.fixture(scope="module", autouse=True)
def before_test():
    print("\nBefore Test")
    yield
    print("\nAfter Test")

# BeforeClass equivalent
@pytest.fixture(scope="class", autouse=True)
def before_class():
    print("\nBefore Class")
    yield
    print("\nAfter Class")

# BeforeMethod equivalent
@pytest.fixture(scope="function", autouse=True)
def before_method():
    print("\nBefore Method")
    yield
    print("\nAfter Method")


class TestSample:

    def test_1(self):
        print("Test 1")

    def test_2(self):
        print("Test 2")

'''
2. Autouse Fixtures
autouse=True makes fixture behave like annotations
Without it → must explicitly pass fixture
==========

3. Dependency Injection (Powerful Pytest Feature)
@pytest.fixture
def db():
    return "db_connection"

def test_user(db):
    assert db == "db_connection"

👉 No equivalent clean pattern in TestNG

==========
Execution Order Comparison
TestNG
BeforeSuite
  BeforeTest
    BeforeClass
      BeforeMethod → Test → AfterMethod
Pytest
session fixture
  module fixture
    class fixture
      function fixture → test → teardown
============
When to Use What
Scenario	Pytest          Fixture Scope
Global      setup (DB, env)	session
Per file    setup	        module
Per class   setup	        class
Per test    setup	        function
=============

Quick Summary
@BeforeSuite → session fixture
@BeforeTest → ❗ No exact equivalent (use module)
@BeforeClass → class fixture
@BeforeMethod → function fixture
Teardown → yield
Pytest is more flexible but less rigid than TestNG
==============
Fixture Design for LLM WebSocket Testing
Layer	            Pytest Scope	    Purpose
Global infra	    session	            Start LLM service / config
Connection	        module or class	    Open WebSocket
Test interaction	function	        Send prompt, validate response
Cleanup	            yield	            Close connections

'''