import os
import requests
from datetime import datetime, timedelta

date = datetime.today().date() - timedelta(days=1)
yesterday = date - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)

string_date = str(date)
string_yesterday = str(yesterday)
string_day_before_yesterday = str(day_before_yesterday)

print(string_date)
print(string_yesterday)
print(string_day_before_yesterday)

ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
STOCK_NAME = "TSLA"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_params ={
    "function" : 'TIME_SERIES_DAILY',
    "symbol" : {STOCK_NAME},
    "apikey" : {ALPHA_API_KEY},
    "outputsize" : 'compact'
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()
print(stock_data['Time Series (Daily)'])

price_change = float(stock_data['Time Series (Daily)'][string_date]['4. close']) - float(stock_data['Time Series (Daily)'][string_yesterday]['4. close'])
print(price_change)
price_change_percentage = (price_change / float(stock_data['Time Series (Daily)'][string_date]['4. close'])) *100
print(price_change_percentage)

if abs(price_change_percentage) > 5:
    print("news")
else:
    print("nothing to report")



NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

news_params ={
    "q" : {COMPANY_NAME},
    "from" : {string_yesterday},
    "sortedBy" : 'publishedAt',
    "apiKey" : {NEWS_API_KEY}
}

# news_response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2025-04-12&sortBy=publishedAt&apiKey=7e01424168404b859dd8d907a33e02ab")


news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()

for i in range(3):
    print(news_data['articles'][i]['title'])
    print("------")
    print(news_data['articles'][i]['description'])
    print("------>")


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 


