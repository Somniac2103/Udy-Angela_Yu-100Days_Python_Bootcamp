import requests
import os
from dotenv import load_dotenv

load_dotenv()

NUTRITIONIX_WEBSITE = "https://trackapi.nutritionix.com"

NUTRITIONIX_API_APP_ID=os.getenv("NUTRITIONIX_API_APP_ID")
NUTRITIONIX_API_APP_KEYS=os.getenv("NUTRITIONIX_API_APP_KEYS")


# Natural Language for Exercise ---->
NUTRITIONIX_ENDPOINT = NUTRITIONIX_WEBSITE + "/v2/natural/exercise"

nutritionix_params = {
    "query"  : 'I ran 1 mile',
    "weight_kg" : 90,
    "height_cm" : 176,
    "age" : 40
}

nutritionix_headers = {
     'x-app-id' : NUTRITIONIX_API_APP_ID,
     'x-app-key' : NUTRITIONIX_API_APP_KEYS
}
response = requests.post(url=NUTRITIONIX_ENDPOINT,headers=nutritionix_headers, json=nutritionix_params)
print(response.status_code)
print(response.text)