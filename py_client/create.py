import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title": "This new field is done",
    "price": 12.54,
    "sale_price": 10.00,
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())
