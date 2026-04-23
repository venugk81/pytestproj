from os.path import samefile

import pytest

# Assertions:
# compare data to be samefile, different and display custom message in case of failure

act_res1 = 100
act_res2 = "testing"
act_res3 = True
act_res4 = 10.43

@pytest.mark.Assertions
def test_tc001_assert_test():
    print("test case assert 1")
    assert act_res1 == 102, "100 != 102 so throwing exception.."
    assert act_res3 == False

@pytest.mark.Assertions
def test_tc002_assert_test():
    print("test case assert 1")
    assert act_res2 == "testing"
    assert act_res4 == 10.431
    assert act_res1 == 100
#Command to execute :  pytest -s -v -m "Assertions" tests