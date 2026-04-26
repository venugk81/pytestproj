import os
from csv import excel
from pathlib import Path
from unittest.result import failfast

import pytest
import pandas as pd

def get_csv_data():
    df = pd.DataFrame()
    try:
        file_path = Path(__file__).parent.parent / "data" / "employee.csv"

        # file_path = "/Users/venug/PycharmProjects/pytestproj/data/employee.csv"
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            print(df)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        pytest.fail(e, pytrace=False)
    if df is None:
        return None
    return df.to_dict(orient='records')


# def get_csv_data(test):
#
#     print("Test--------------: ", test)
#     print("\n******************* How many times it is coming to get_csv_data**************")
#     return [
#         {"id": 1, "name": "venu", "grade": 500},
#         {"id": 2, "name": "gopi", "grade": 480},
#         {"id": 4, "name": "varun", "grade": 360},
#         {"id": 3, "name": "vikas", "grade": 590},
#     ]

@pytest.mark.parametrize("map_data", get_csv_data())
def test_dynamic_csv(map_data):
    print(f"\nmap_data======== {map_data.values()}")
    for k, v in map_data.items():
        print(f"{k}======== {v}")


##### Example 2

def get_data1(test_name):
    try:
        file_path = Path(__file__).parent.parent / "data" / "employee.csv"
        # dt= pd.read_csv("/Users/venug/PycharmProjects/pytestproj/data/employee.csv")
        dt= pd.read_csv(file_path)
        return dt[dt["Name"]==test_name].to_dict(orient="records")
    except Exception as exp:
        pytest.fail(f"Exception Occurred: {exp}", pytrace=False)


@pytest.mark.parametrize("test_data", get_data1("ReadDataFromCSVParams"))
def test_login(test_data):
    username = test_data["Name"]
    gender = test_data["Gender"]
    id = test_data["ID"]
    print("\n=================== Username: ", username, ", Gender: ", gender, ", ID: ", id)
    if id == 8:     ##Intentionally Failing the test here
        pytest.fail(f"Username already exists: {id}", pytrace=False)
    print(test_data)

