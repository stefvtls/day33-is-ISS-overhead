import tkinter.messagebox
import requests
import datetime as dt
import time


# Amsterdam longitutde and latitude
lat = 52.370216
lng = 4.895168

parametry = {
    "lat": lat,
    "lng": lng,
    "formatted": 0,
}
response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parametry)
response_sun.raise_for_status()
data_sun = response_sun.json()
sunrise = data_sun["results"]["sunrise"]
sunset = data_sun["results"]["sunset"]
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
sunset_hour = int(sunset.split("T")[1].split(":")[0])
now = dt.datetime.now()

while True:
    time.sleep(60)
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    iss_longitude = float(data_iss["iss_position"]["longitude"])
    iss_latitude = float(data_iss["iss_position"]["latitude"])
    # print(iss_longitude, iss_latitude)
    if (sunset_hour < now.hour) or (now.hour < sunrise_hour):
        if (lng + 5 >= iss_longitude >= lng - 5) and (lat - 5 <= iss_latitude <= lat + 5):
            tkinter.messagebox.showinfo(title="look up!", message="iss station above you")
