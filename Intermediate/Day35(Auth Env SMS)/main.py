import requests

# lat = 51.507351
# lon = -0.127758
# api = "04fab6cbc8cd4b52e350ccd0913e52e0"

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
    "appid" : "04fab6cbc8cd4b52e350ccd0913e52e0"
}

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)
data = response.json()
print(data)

