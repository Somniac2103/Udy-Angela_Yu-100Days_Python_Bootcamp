import requests
from datetime import datetime

# My Position
MY_LAT = 51.507351
MY_LONG = -0.127758

print(f'{MY_LONG}, {MY_LAT}')

# ISS Position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_longitude = float(data["iss_position"]["longitude"])
iss_latitude = float(data["iss_position"]["latitude"])

iss_position = (iss_longitude, iss_latitude)

print(iss_position)

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

print(sunrise)
print(sunset)

# My Current Time
time_now = datetime.now().hour

print(time_now)

# check if ISS and my position is within 5 degrees
MY_LONG_upper_limit = MY_LONG + 5
MY_LONG_lower_limit = MY_LONG - 5
MY_LAT_upper_limit = MY_LAT + 5
MY_LAT_lower_limit = MY_LAT - 5

if iss_latitude <= MY_LAT_upper_limit and  iss_latitude >= MY_LAT_lower_limit:
    if iss_longitude <= MY_LONG_upper_limit and iss_longitude >= MY_LONG_lower_limit:

        # check if it is dark if within 5 degrees
        if time_now <= sunrise or time_now <= sunset:
            
            # send email if wthin 5 degrees and dark

