import requests

response = requests.get("http://api.open-notify.org/astros.json")
with open("data.json", "w") as f:
    f.write(str(response.json()))

