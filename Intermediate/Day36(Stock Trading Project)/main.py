import os
import requests
from datetime import datetime, timedelta

date = datetime.today().date() - timedelta(days=4)
yesterday = date - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=1)

string_date = str(date)
string_yesterday = str(yesterday)
string_day_before_yesterday = str(day_before_yesterday)

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
# print(stock_data['Time Series (Daily)'])

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
    print(news_data['articles'][i]['description'])
    print("------>")


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 



#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

