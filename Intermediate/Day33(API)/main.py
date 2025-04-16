import requests
from datetime import datetime
import smtplib

#email credentials
my_email = "barrysalmon36@gmail.com"
app_password = "zxxb nxnh xddr kitr"

# My Position
MY_LAT = 50
MY_LONG = -65

print("My lats and longs")
print(f'{MY_LAT}, {MY_LONG}')

# ISS Position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

print("ISS position")
print(f"{iss_latitude}, {iss_longitude}")

# Night time at my position
parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted" : 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(f'Local Sunrise = {sunrise}')
print(f'Local Sunset = {sunset}')

# My Current Time
time_now = datetime.now().hour

print(f'Current Local Time = {time_now}')

# check if ISS and my position is within 5 degrees
MY_LONG_upper_limit = MY_LONG + 5
MY_LONG_lower_limit = MY_LONG - 5
MY_LAT_upper_limit = MY_LAT + 5
MY_LAT_lower_limit = MY_LAT - 5

if iss_latitude <= MY_LAT_upper_limit and  iss_latitude >= MY_LAT_lower_limit:
    print("ISS within latitude tolerance")
    if iss_longitude <= MY_LONG_upper_limit and iss_longitude >= MY_LONG_lower_limit:
        print("ISS within lonogtitude tolerance")
        # check if it is dark if within 5 degrees
        if time_now < sunrise or time_now > sunset:
            print("it is between sunset and sunrise at local position")
            # send email if wthin 5 degrees and dark
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=app_password)
                connection.sendmail(
                    from_addr = my_email,
                    to_addrs="salmon.barry1@gmail.com", 
                    msg=f"Subject:ISS Alert\n\n The ISS is overhead and can be seen"
                )
            print("Email sent")

