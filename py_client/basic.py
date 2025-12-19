import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, params={"abc": 123}, json={"title": "Hello world!"});
print(response.json())
# print(response.text)
# print(response.status_code)