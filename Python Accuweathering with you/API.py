import requests
import json
from pyttsx3 import init

	# etBCpNG9NNkJJAeFkI6zGEMUX3tbJi3D
    # 349727
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
            "LocalObservationDateTime": weather_data[0]['LocalObservationDateTime']
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
    print("Weather Information:")
    print("Temperature:", weather_info['Temperature'], ['Unit'])
    print("Humidity:", weather_info['Humidity'])
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

speech = init()

def main(text):
    text.say('Weather Information:')
    text.say(f"Temperature: {weather_info['Temperature']} degrees", )
    text.say(f"Humidity: {weather_info['Humidity']} percent")
    precipitation = weather_info['Precipitation']
    if precipitation is not None:
        if 'Metric' in precipitation and 'Value' in precipitation['Metric']:
            precipitation_value = precipitation['Metric']['Value']
            text.say("Precipitation:", precipitation_value, "mm")

            if 'Probability' in precipitation:
                precipitation_probability = precipitation['Probability']
                text.say("Precipitation Probability:", precipitation_probability, "%")
        else:
            text.say("Precipitation information not available")
    else:
        text.say("Precipitation: No precipitation")
    text.say(f"Local Observation Date Time: {weather_info['LocalObservationDateTime']}")
    text.runAndWait()


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



if __name__ == "__main__":
    main(speech)