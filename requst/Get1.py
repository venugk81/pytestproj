import json
from xml.etree.ElementTree import indent

import requests

nu = 2
res = requests.get(f"https://jsonplaceholder.typicode.com/users/{nu}")
print(res.json())
print(json.dumps(res.json(), indent=4))


res = requests.get(f"https://jsonplaceholder.typicode.com/users")
print(res.json())
print(json.dumps(res.json(), indent=4))

# json.dump(res.json(), open("data.json", "w"), indent=4)