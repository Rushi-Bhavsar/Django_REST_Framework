import requests
import json


URL = 'http://127.0.0.1:8000/studentapi/'


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    response = requests.get(url=URL, data=json_data)
    print(response.json())


get_data()


def post_data():
    data = {
        'name': 'Rushikesh Bhavsar',
        'roll': 43,
        'city': 'Nashik'
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    print(response.json())


# post_data()


def update_data():
    data = {
        'id': 4,
        'name': 'Harshal Wagh',
        'city': 'Pune'
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    print(response.json())


# update_data()


def delete_data():
    data = {
        'id': 6
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    print(response.json())


# delete_data()
