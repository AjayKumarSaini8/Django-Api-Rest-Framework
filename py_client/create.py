import requests

headers = {"Authorization": "Bearer 3c8cf90392edea3ffd2ed44b2b6a2b22230a2f19"}
endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This new field is done",
    "price": 12.54,
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())
