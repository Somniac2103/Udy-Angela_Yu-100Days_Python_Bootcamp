#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch

load_dotenv()

dm = DataManager()
fs = FlightSearch()

prices = dm.get_prices()

for item in prices:
    if item["iataCode"] is None:
        item["iataCode"] = fs.get_code(item["city"])



