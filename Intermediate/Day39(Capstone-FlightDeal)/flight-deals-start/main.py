#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_API_URL = "https://api.sheety.co/"
SHEETY_ACCOUNT = os.getenv("SHEETY_ACCOUNT")
SHEETY_PROJECT = "flightDeals"
SHEETY_ACCOUNT_SHEET = "prices"

SHEETY_ENDPOINT = f"{SHEETY_API_URL}/{SHEETY_ACCOUNT}/{SHEETY_PROJECT}/{SHEETY_ACCOUNT_SHEET}"


# sheety_params = {
#     "query"  : exercise_input,
#     "weight_kg" : 90,
#     "height_cm" : 176,
#     "age" : 40
# }

# sheety_headers = {
#      'x-app-id' : NUTRITIONIX_API_APP_ID,
#      'x-app-key' : NUTRITIONIX_API_APP_KEYS
# }
response = requests.get(url=SHEETY_ENDPOINT)
print(response.status_code)
print(response.text)


