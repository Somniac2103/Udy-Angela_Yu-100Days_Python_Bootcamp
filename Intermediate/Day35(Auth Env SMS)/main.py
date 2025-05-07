import requests
from twilio.rest import Client
import os

# lat = 51.507351
# lon = -0.127758
# api = os.environ.get("OWM_API_KEY")

# endpoint = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api}'

# response = requests.get(url=endpoint)
# response.raise_for_status()
# data = response.json()

# print(data['cod'])
# print(data)

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params ={
    "lat" : 51.507351,
    "lon" : -0.127758,
    "appid" : os.environ.get("OWM_API_KEY"),
    "cnt" : 4,
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
# print(response.status_code)
data = response.json()
for hour_data in data["list"]:
    if hour_data['weather'][0]['id'] < 700:
        print("Bring umbrella")
        break

