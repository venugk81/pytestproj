from ctypes.wintypes import tagSIZE
from os import terminal_size

import pytest

# write tags to the test cases
# execute test cases with single tag
# skip execution of test cases y giving tag names(write multiple tags on test cases
# execute test cases using more than 1 tag (or and )

@pytest.mark.Smoke
def test_tc001_group1():
    print("login test 1- group")
    assert 2==2

@pytest.mark.Smoke
def test_tc002_group2():
    print("login test 2- group")
    assert 1==2, "Values are not matching.."

@pytest.mark.Mandatory
def test_tc003_group3():
    print("login test 3- group")

@pytest.mark.Sanity
def test_tc004_group4():
    print("login test 3- group")

# if you want to execute test based on groups but want to execute this test in every goup, then:
@pytest.mark.Smoke
@pytest.mark.Regression
@pytest.mark.Sanity
def test_tc006_important_test():
    print("THis is very important test case so execute it as part of both smoke and regression")


# -m = to execcute tests based on tags
# pytest -s -v -m Smoke <Foldername>
# pytest -s -v -m  Regression tests
# = 1 failed, 1 passed, 11 deselected, 3 warnings

# if you want to execute all except one group. use the command
# pytest -s -v -m "not Smoke" <folder name>
# Results
# 2 failed, 7 passed, 2 skipped, 2 deselected, 4 warnings

# if you want to execute tests groups - smoke or regression then
# pytest -v -s -m "smoke or sanity" <folder name>

# if you want to execute both smoke and regression: use and
# pytest -v -s -m "Smoke and Sanity" <folder name>

# When we are using custom specific group names like moke regression, system throws warnings in the terminal
# HOw to disable them ?
#
# 1. Disable pytest-warnings : pytest -s -v --disable-pytest-warnings -m "Smoke" test<folder name>
# 2. Register the custom marker.:
#     create Pytest.ini file at the folder and then add below:
#     [pytest]
#     markers =
#         smoke: This is for smoke test cases execution
#         Sanity: This is for Sanity test cases execution
#         TopPriority: This is for TopPriority test cases execution
#         Regression: This is for Regression test cases execution
#         Mandatory: This is for Mandatory test cases execution
#  pytest -s -v -m "Smoke or Sanity" tests   - Command.
# When you register custom tags, you will not get any warnings.