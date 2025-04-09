import datetime as dt
import random
import smtplib
# Get day
weekday = 2
today = dt.datetime.now().weekday()
# Check day if Tuesday
if today == weekday:
    # print("True")
    # if Tuesday load motivation qoutes
    with open('quotes.txt', 'r') as file:
        content = file.read()
    # print(content)
    items = content.split('\n')
    random_item = random.choice(items)
    # random_item_quote = (random_item.split('-'))[0]
    # random_item_quoteperson = (random_item.split('-'))[1]
    # print(random_item_quote)
    # print(random_item_quoteperson)


# email quote to myself
my_email = "barrysalmon36@gmail.com"
app_password = "zxxb nxnh xddr kitr"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    connection.sendmail(
        from_addr = my_email,
        to_addrs="salmon.barry1@gmail.com", 
        msg=f"Subject:Motivational Quote\n\n {random_item}"
    )

