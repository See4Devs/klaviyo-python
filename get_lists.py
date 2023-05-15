import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
API_KEY = config['API_KEY']
BASE_URL = config['BASE_URL']
Headers = {
    "accept": "application/json",
    "revision": "2023-05-11",
    "content-type": "application/json",
    "Authorization": "Klaviyo-API-Key "+ API_KEY
}

def get_lists():
    url = f'{BASE_URL}/lists/'
    response = requests.get(url, headers=Headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

lists = get_lists()
print(lists)

