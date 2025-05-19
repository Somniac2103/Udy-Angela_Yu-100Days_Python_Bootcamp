import requests
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_WEBSITE = "https://pixe.la"
PIXELA_USERNAME= os.getenv("PIXELA_USERNAME")
PIXELA_API_TOKEN = os.getenv("PIXELA_API_TOKEN")

# CREATE USER ---->
PIXELA_USER_ENDPOINT = PIXELA_WEBSITE + "/v1/users"
user_params = {
    "token" : PIXELA_API_TOKEN,
    "username" : PIXELA_USERNAME,
    "agreeTermsOfService"  : 'yes',
    "notMinor" : "yes"
}
# response = requests.post(url=PIXELA_USER_ENDPOINT, json=user_params)
# print(response.text)


# MAKE GRAPH ----->
PIXELA_GRAPH_ENDPOINT = f'{PIXELA_WEBSITE}/v1/users/{PIXELA_USERNAME}/graphs'
graph_params = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

graph_headers = {
    "X-USER-TOKEN" : PIXELA_API_TOKEN
}
# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, json=graph_params, headers=graph_headers)
# print(response.text)

# RECORD DATA ----->
PIXELA_GRAPH_NAME = "graph1"
PIXELA_DATA_ENDPOINT = f'{PIXELA_WEBSITE}/v1/users/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_NAME}'
data_body = {
    "date" : "20250519",
    "quantity" : "9.0",
}

data_headers = {
    "X-USER-TOKEN" : PIXELA_API_TOKEN
}
response = requests.post(url=PIXELA_DATA_ENDPOINT, headers=data_headers, data=data_body)
print(response.text)
