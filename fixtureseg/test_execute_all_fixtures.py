
import pytest


def test_tc001_login(before_suite, before_module, before_function):
    print("login test 1")
    assert True

def test_tc002_logout(before_module, before_function):
    print("logout test 2")

def test_tc003_register(before_module,before_function):
    print("register test 3")
    assert 1==2

##   pytest -s -v fixtureseg/test_execute_all_fixtures.py

###
# Output

# collected 3 items
#
# fixtureseg/test_execute_all_fixtures.py::test_tc001_login before suite executed 1
# before module scope executed 2
# before function scope executed 3
# login test 1
# PASSEDafter function scope executed 1
#
# fixtureseg/test_execute_all_fixtures.py::test_tc002_logout before function scope executed 3
# logout test 2
# PASSEDafter function scope executed 1
#
# fixtureseg/test_execute_all_fixtures.py::test_tc003_register before function scope executed 3
# register test 3
# FAILEDafter function scope executed 1
# after module scope executed
# after suite executed 2

###
