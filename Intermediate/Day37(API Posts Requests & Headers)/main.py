import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_WEBSITE = "https://pixe.la"
PIXELA_USERNAME= os.getenv("PIXELA_USERNAME")
PIXELA_API_TOKEN = os.getenv("PIXELA_API_TOKEN")

PIXELA_USER_ENDPOINT = PIXELA_WEBSITE + "/v1/users"
user_params = {
    "token" : PIXELA_API_TOKEN,
    "username" : PIXELA_USERNAME,
    "agreeTermsOfService"  : 'yes',
    "notMinor" : "yes"
}

# response = requests.post(url=PIXELA_USER_ENDPOINT, json=user_params)
