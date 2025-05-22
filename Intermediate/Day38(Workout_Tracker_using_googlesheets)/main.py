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

# SHEETY POST ----->
SHEETY_API_WEBSITE = "https://api.sheety.co/"
SHEETY_ACCOUNT = "64c5e842b391c3c5f830594bcee9e8fb"
SHEETY_ACCOUNT_SHEET = "sheet1"

SHEETY_ENDPOINT = F"{SHEETY_API_WEBSITE}{SHEETY_ACCOUNT}/workoutTracking/{SHEETY_ACCOUNT_SHEET}"

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
response = requests.post(url=SHEETY_ENDPOINT,headers=nutritionix_headers, json=nutritionix_params)
print(response.status_code)
print(response.text)

  let body = {
    sheet1: {
      ...
    }
  }
  fetch(url, {
    method: 'POST',
    body: JSON.stringify(body)
  })
  .then((response) => response.json())
  .then(json => {
    // Do something with object
    console.log(json.sheet1);
  });