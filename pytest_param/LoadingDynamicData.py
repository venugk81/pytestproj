import pytest
# def get_test_data():
#     return [
#         (1, 2, 3),
#         (3, 4, 7),
#     ]
#
# @pytest.mark.parametrize("a,b,expected", get_test_data())
# def test_dynamic(a, b, expected):
#     assert a + b == expected
import os


def get_csv_data(test):
    # filename = os.path.basename(__file__)
    # print(filename)
    print("Test--------------: ", test)
    print("\n******************* How many times it is coming to get_csv_data**************")
    return [
        {"id": 1, "name": "venu", "grade": 500},
        {"id": 2, "name": "gopi", "grade": 480},
        {"id": 4, "name": "varun", "grade": 360},
        {"id": 3, "name": "vikas", "grade": 590},
    ]

@pytest.mark.parametrize("map_data", get_csv_data("value passed "))
def test_dynamic_csv(map_data):
    print(f"\nmap_data======== {map_data.values()}")
    for k, v in map_data.items():
        print(f"{k}======== {v}")
