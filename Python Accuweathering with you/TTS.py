import requests
import json

def fetch_weather(api_key, location_key):
    base_url = "http://dataservice.accuweather.com/currentconditions/v1/"
    endpoint = f"{location_key}?apikey={api_key}&details=true"

    try:
        response = requests.get(base_url + endpoint)
        response.raise_for_status()
        weather_data = json.loads(response.text)

        # Extract relevant information from the response
        weather_info = {
            "Humidity": weather_data[0]['RelativeHumidity'],
            "Temperature": weather_data[0]['Temperature']['Metric']['Value'],
            "Unit": weather_data[0]['Temperature']['Metric']['Unit'],
            "Precipitation": weather_data[0].get('Precipitation'),
            "LocalObservationDateTime": weather_data[0]['LocalObservationDateTime'],
            "Wind Speed": {weather_data[0]['Wind']['Direction']['Degrees'], weather_data[0]['Wind']['Direction']['Localized']}
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", e)

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'etBCpNG9NNkJJAeFkI6zGEMUX3tbJi3D'
# Replace 'LOCATION_KEY' with the location key of the desired location
location_key = '759549'

weather_info = fetch_weather(api_key, location_key)
if weather_info:
    print("Weather Information")
    print(f"Temperature: {weather_info['Temperature'], ['Unit']}")
    print(f"Humidity:, {weather_info['Humidity']}")
    precipitation = weather_info['Precipitation']
    if precipitation is not None:
        if 'Metric' in precipitation and 'Value' in precipitation['Metric']:
            precipitation_value = precipitation['Metric']['Value']
            print("Precipitation:", precipitation_value, "mm")

            if 'Probability' in precipitation:
                precipitation_probability = precipitation['Probability']
                print("Precipitation Probability:", precipitation_probability, "%")
        else:
            print("Precipitation information not available")
    else:
        print("Precipitation: No precipitation")
    print("Local Observation Date Time:", weather_info['LocalObservationDateTime'])
    print(f"Wind Speed: {weather_info['Wind Speed']}")
