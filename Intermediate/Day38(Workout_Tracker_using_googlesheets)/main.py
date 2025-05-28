import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "Male"
WEIGHT_KG =  92
HEIGHT_CM =   176
AGE = 40

exercise_input = input("Tell me which exercises you did: ")

NUTRITIONIX_WEBSITE = "https://trackapi.nutritionix.com"

NUTRITIONIX_API_APP_ID=os.getenv("NUTRITIONIX_API_APP_ID")
NUTRITIONIX_API_APP_KEYS=os.getenv("NUTRITIONIX_API_APP_KEYS")


# Natural Language for Exercise ---->
NUTRITIONIX_ENDPOINT = NUTRITIONIX_WEBSITE + "/v2/natural/exercise"

nutritionix_params = {
    "query"  : exercise_input,
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

result = response.json()

# SHEETY POST ----->

SHEETY_API_WEBSITE = "https://api.sheety.co/"
SHEETY_ACCOUNT = "64c5e842b391c3c5f830594bcee9e8fb"
SHEETY_ACCOUNT_SHEET = "sheet1"
SHEETY_API_TOKEN = os.getenv("SHEETY_API_TOKEN")

SHEETY_ENDPOINT = F"{SHEETY_API_WEBSITE}{SHEETY_ACCOUNT}/workoutTracking/{SHEETY_ACCOUNT_SHEET}"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now(). strftime("%X")

for exercise in result["exercises"]:
    try:
        sheety_body = {
            SHEETY_ACCOUNT_SHEET: {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": round(exercise["duration_min"], 2),
                "calories": round(exercise["nf_calories"], 2)
            }
        }

        sheety_headers = {
            "Authorization": f"Bearer {SHEETY_API_TOKEN}"
        }


        print("Sending to Sheety:", sheety_body)

        sheet_response = requests.post(SHEETY_ENDPOINT, json=sheety_body, headers=sheety_headers)
        sheet_response.raise_for_status()  # Raises error if 4xx or 5xx
        print(sheet_response.status_code)
        print(sheet_response.text)
    except Exception as e:
        print("Error posting to Sheety:", e)