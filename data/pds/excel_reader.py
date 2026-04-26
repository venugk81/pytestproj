import os
from pathlib import Path

import pandas as pd
import pytest
#
# file_path = "/Users/venug/PycharmProjects/pytestproj/data/data.xlsx"
# df = pd.read_excel(file_path, "Employee")
#
# print(df.to_dict("records"))


def get_excel_test(file_name, test_name, sheet_name):
    df = pd.DataFrame()
    try:
        # file_path = "/Users/venug/PycharmProjects/pytestproj/data/data.xlsx"
        # file_path = Path(__file__).parent.parent / "data" / f"{file_name}.xlsx"
        file_path =  "../data.xlsx"
        if os.path.exists(file_path):
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            print(df)
    except FileNotFoundError as e:
        print(e)
    except Exception as exp:
        pytest.fail(str(exp), pytrace=False)
    if df is None:
        return None
    return df[df["ID"]==test_name].to_dict(orient="records")


x = get_excel_test("data", "E045", "Employee")
print(x)
