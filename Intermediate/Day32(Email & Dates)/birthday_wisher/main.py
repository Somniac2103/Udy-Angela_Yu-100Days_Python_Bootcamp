import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "barrysalmon36@gmail.com"
app_password = "zxxb nxnh xddr kitr"

current_month = dt.datetime.today().month
# print(current_month)
current_day = dt.datetime.today().day
# print(current_day)

birthdays_df = pd.read_csv("birthdays.csv")
# print(birthdays_df)

for index, row in birthdays_df.iterrows():
    if row['month'] == current_month and row['day'] == current_day:
        # print(f"Row {index}: Name = {row['name']}, email = {row['email']}")
        letter_format = f"letter_{random.choice([1,2,3])}.txt"
        with open(f"letter_templates/{letter_format}") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", row['name'])
            # print(letter) 
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(
                from_addr = my_email,
                to_addrs="salmon.barry1@gmail.com", 
                msg=f"Subject:Happy Birthday\n\n {letter}"
            )
        print("Email sent")




