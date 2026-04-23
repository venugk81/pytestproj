import pytest

a = 90
@pytest.mark.skip(reason="not implemented")
def test_tc001_login():
    print("loging test 1" )
    assert 1==1

#Skip this test if a>100 and print the reason="a is > 100 so skipped"
@pytest.mark.skipif(a>100, reason="if a>100 and print the reason=a is > 100 so skipped")
def test_tc002_login():
    print("login test 1")
    assert 1==1

def test_tc003_login():
    print("only 1 test to run and remaining skipped.. ")


#Skip this test if a<100 and print the reason="a is < 100 so skipped"
@pytest.mark.skipif(a<100, reason="if a<100 and print the reason=a is < 100 so skipped")
def test_tc004_login():
    print("login test 1")
    assert 1==1

@pytest.mark.Regression
def test_tc005_login():
    print("test 5 execution..")

# -k is to give specific test for execution - specitic test method will be executed.
# pytest -s -v -k test_tc05_login tests<this is folder name>
# pytest -s -v tests/test_First.py

# if you want to execute all the test method which has specific test in name- use:
#     pytest -s -v -k 005 tests
#     here -k is to execute specific methods
#     we gave 005 text so it will execute all the methods which contains 005 in test methods
#     tests: is the test folder name.

# if you want to execute all except one group. use the command
# pytest -s -v -m "not Smoke" <folder name>

#  2 failed, 7 passed, 2 skipped, 2 deselected, 4 warnings