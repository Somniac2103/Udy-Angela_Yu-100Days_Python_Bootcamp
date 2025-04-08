import datetime as dt
# Get day
weekday = 1
today = dt.datetime.now().weekday()
# Check day if Tuesday
if today == weekday:
    # print("True")
    # if Tuesday load motivation qoutes
    with open('quotes.txt', 'r') as file:
        content = file.read()
    # print(content)
    items = content.split('-')
    print(items)
       
# # Pick motivation quote
# # email myself motivation quote