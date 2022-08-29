import requests
import json

parameters = {
        "lat": 40.71, 
        "lon": -74
        }
response = requests.get("https://api.open-notify.org/iss-pass.json", params=parameters)

string = json.dumps(response.json(), indent=4, sort_keys=True)

print(string)
