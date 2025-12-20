import requests

product_id = input('Enter thr product id: \n')
try:
    product_id = int(product_id)
except:
    print("Invalid product id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    response = requests.delete(endpoint);
    print(response.status_code, response.status_code == 204)
    # print(response.text)
    # print(response.status_code)