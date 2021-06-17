import requests
import json


URL = "http://127.0.0.1:8000/student_create/"

data ={
    'name': 'Rushikesh Bhavsar',
    'roll_no': 54,
    'city': 'Nashik'
}

json_data = json.dumps(data)
request = requests.post(url=URL, data=json_data)
print(request)
print(request.json())

