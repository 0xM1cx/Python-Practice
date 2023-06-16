import requests
import json

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'etBCpNG9NNkJJAeFkI6zGEMUX3tbJi3D'
# Replace 'LOCATION_KEY' with the location key of the desired location
location_key = '759549'

url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={api_key}&details=true'

try:
    response = requests.get(url)
    data = response.json()
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)

    if data and 'Alerts' in data[0]:
            alerts = data[0]['Alerts']
            for alert in alerts:
                if alert['Category'] == 'Typhoon':
                    typhoon_name = alert['Event']
                    severity = alert['Severity']
                    wind_speed = alert['WindSpeed']['Value']
                    location = alert['Area']['Name']
                    message = f"There is a typhoon named {typhoon_name} in {location}. Severity: {severity}. Wind speed: {wind_speed} mph."
                    print(message)  # Replace with your desired action or notification method
        
except requests.exceptions.RequestException as e:
    print("Error: ", e)