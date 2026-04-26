import json
from xml.etree.ElementTree import indent

import pytest
import pandasfiles as pd
from pathlib import Path

with open(Path(__file__).parent.parent / "data" / "credentials.json") as f:
    test_dt = json.load(f)
    print(test_dt)
    user_credentials_list = test_dt["user_credentials"]

@pytest.mark.parametrize("user_data", user_credentials_list)
def test_execute(user_data):
    print("Testing execute")
    print("Username: ", user_data["user"])
    print("password: ", user_data["password"])
    print("======== ******************** =========")

