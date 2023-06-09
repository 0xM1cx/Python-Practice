import requests
from bs4 import BeautifulSoup

URL = "http://dataservice.accuweather.com/forecasts/v1/minute"
resp = requests.get(URL)
param = ""
key = "KmUdYvB1ux8HrJHotWMYctgbAiEokWde"
# try:
#     page = requests.get(URL)
#     soup = BeautifulSoup(page.content, "html.parser")
# except:
#     print("Wa gumana")
print(resp.status_code)


# tac_ID = soup.find_all("td", string="5131")
# print(tac_ID)