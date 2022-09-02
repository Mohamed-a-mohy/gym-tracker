import requests
from datetime import datetime
import os

HEADER_ID = os.environ["HEADER_ID"]
API_NEUTRATION = os.environ["API_NEUTRATION"]
END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_END_POINT = os.environ["SHEETY_END_POINT"]


query_text = input("what exercies  you did ?")
header = {
    "x-app-id": HEADER_ID,
    "x-app-key": API_NEUTRATION,
}
post_params = {
    "query": query_text,
    "gender": "male",
    "weight_kg": 72,
    "height_cm": 173,
    "age": 25
}

response = requests.post(url=END_POINT, json=post_params, headers=header)
result = response.json()
print(result)


today = datetime.now().strftime(("%d/%m/%Y"))
now_time = datetime.now().strftime("%X")

for exercie in result["exercises"]:
    sheety_header = {
        "Authorization": "Basic bW9oeTk3OjExMTE"
    }
    sheety_params = {
        "workout": {
            'date': today,
            'time': now_time,
            'exercise': exercie['name'],
            'duration': exercie['duration_min'],
            'calories': exercie['nf_calories'],
            'id': 2
        },
    }
    sheety_post = requests.post(url=SHEETY_END_POINT, json=sheety_params, headers=sheety_header)


