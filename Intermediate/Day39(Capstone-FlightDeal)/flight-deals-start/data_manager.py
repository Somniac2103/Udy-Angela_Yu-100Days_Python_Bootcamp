import os
import requests
from dotenv import load_dotenv

class DataManager:
    def __init__(self):   

        load_dotenv()

        self.SHEETY_API_URL = "https://api.sheety.co/"
        self.SHEETY_ACCOUNT = os.getenv("SHEETY_ACCOUNT")
        self.SHEETY_PROJECT = "flightDeals"
        self.SHEETY_ACCOUNT_SHEET = "prices"

        self.SHEETY_ENDPOINT = f"{self.SHEETY_API_URL}/{self.SHEETY_ACCOUNT}/{self.SHEETY_PROJECT}/{self.SHEETY_ACCOUNT_SHEET}"

    def get_prices(self):
        try:
            response = requests.get(url=self.SHEETY_ENDPOINT)
            print(response.status_code)
            print(response.text)
            data = response.json()
            results = data.get("prices", [])
            return (results)
        except requests.RequestException as e:
            print(f"[ERROR] Request Failed: {e}")
            return []