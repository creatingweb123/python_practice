import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

api_key=os.environ.get("API_KEY")

lat = 35.8713
longt=128.6018

api_url = f"https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat":lat,
    "lon":longt,
    "appid":api_key   
}

response = requests.get(url=api_url,params=parameters)
response.raise_for_status()

will_rain = False
twelve_weather_data = response.json()["list"][:4]
for hour_data in twelve_weather_data:
    if hour_data["weather"][0]["id"]<700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages\
    .create(
        body    ="It'll rain today. Bring an umbrella",
        from_   =os.environ.get("FROM_NUMBER"),
        to      =os.environ.get("TO_NUMBER")
    )
    print(message.sid)
