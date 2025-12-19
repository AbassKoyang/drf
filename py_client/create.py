import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    'title': "This is the title field"
}
response = requests.post(endpoint, json=data);
print(response.json())
# print(response.text)
# print(response.status_code)