import requests

endpoint = f"http://localhost:8000/api/products/2/update/"

data = {
    'title': "This is an updated title field",
    'price': 500.00
}
response = requests.put(endpoint, json=data);
print(response.json())
# print(response.text)
# print(response.status_code)