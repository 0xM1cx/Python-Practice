from flask import Flask, jsonify
import requests
import json
from pyttsx3 import init

app = Flask(__name__)

def fetch_weather(api_key, location_key):
    # Your existing code for fetching weather information
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
            "Precipitation": weather_data[0].get('Precipitation'),
            "LocalObservationDateTime": weather_data[0]['LocalObservationDateTime']
        }

        return weather_info

    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching weather data:", e)


@app.route('/weather', methods=['GET'])
def get_weather():
    weather_info = fetch_weather(api_key, location_key)
    if weather_info:
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'Failed to fetch weather information'})

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' and 'LOCATION_KEY' with your actual values
    api_key = 'etBCpNG9NNkJJAeFkI6zGEMUX3tbJi3D'
    location_key = '759549'
    app.run(debug=True)