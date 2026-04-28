import os
import pandas as pd
import pytest

from pytest_param.FileUtils import get_csv_data


@pytest.mark.parametrize("map_data", get_csv_data("employee", "ReadDataFromCSVParams"))
def test_dynamic_csv(map_data):
    print(f"\nmap_data======== {map_data.values()}")
    for k, v in map_data.items():
        print(f"{k}======== {v}")
    map_dt = pd.DataFrame([map_data])
    map_dt.to_csv("data/export.csv", index=False)


    # df_new = pd.DataFrame(new_data)
    #
    # # Append new rows
    # df_updated = pd.concat([df_existing, df_new], ignore_index=True)
    #
    # # Save back to same CSV
    # df_updated.to_csv("data/test.csv", index=False)


from pathlib import Path

def dummy():
    print("os.getcwd(): ", os.getcwd())
    str1 = Path(os.getcwd()+"/data/employee.csv")

    print(f"str: {str1}")
    ####/Users/venug/PycharmProjects/pytestproj/pytest_param./data/employee.csv

    print(f"Path(__file__): {Path(__file__)}")
    ###/Users/venug/PycharmProjects/pytestproj/pytest_param/EmpData.py

    print(f"Path(__file__).parent: {Path(__file__).parent}")
    ##/Users/venug/PycharmProjects/pytestproj/pytest_param

    print(f"Path(__file__).parent.parent: {Path(__file__).parent.parent}")
    ##/Users/venug/PycharmProjects/pytestproj

    print(f"Path(__file__).parent: {Path(__file__).parent.parent/'data'/'employee.csv'}")
    ##/Users/venug/PycharmProjects/pytestproj/data/employee.csv

    if str1.exists():
        print(os.path)
        df = pd.read_csv(str1)
        print(df)
    else:
       print("test failed")


# dummy()