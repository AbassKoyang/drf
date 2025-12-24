import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username? \n")
password = getpass("What is your password? \n")
title = input("Enter product title \n")

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json());

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

    endpoint = "http://localhost:8000/api/products/"

    data = {
        'title': title
    }
    response = requests.post(endpoint, headers=headers, json=data);
    print(response.json())
    # print(response.text)
    # print(response.status_code)