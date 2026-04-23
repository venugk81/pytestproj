import pytest
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (2, 2, 4),
        # (2, 2, 4),      ## if we have extra data set: In test_add_ids:
        # 3 parameter sets specified, with different number of ids: 2
    ],
    ids=["one_plus_two", "two_plus_two"]
)
def test_add_ids(a, b, expected):
    assert a + b == expected

###
# pytest_param/IDsForUsability.py::test_add_ids[one_plus_two] PASSED       [ 50%]
# pytest_param/IDsForUsability.py::test_add_ids[two_plus_two] PASSED       [100%]
###