import requests
import os
from datetime import datetime

today = datetime.now()
str_today = today.strftime("%d/%m/%Y")
str_time = today.strftime("%X")

APP_ID  = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")
sheet_name = "workouts"
project_name = "My_Workouts"
sheety_end_point = os.environ["SHEETY_ENDPOINT"]
bearer_token = os.environ["BEARER_TOKEN"]

bearer_headers={
    "Authorization": f"Bearer {bearer_token}"
}

headers = {
    "x-app-id"      : APP_ID,
    "x-app-key"     : APP_KEY
}

parms ={
    "query"     :exercise_input,
    "gender"    :"MALE",
    "weight_kg" :"55",
    "height_cm" :"165",
    "age"       :"23"
}

response = requests.post(url=exercise_endpoint,json=parms,headers=headers)
response.raise_for_status()
result = response.json()

for data in result["exercises"]:
    sheet_inputs = {
        "sheet1":{
            "date"    : str_today,
            "time"    : str_time,
            "exercise": data["name"].title(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
        }
    }
    sheety_response = requests.post(url=sheety_end_point,json=sheet_inputs,headers=bearer_headers)
    print(sheety_response.text)
