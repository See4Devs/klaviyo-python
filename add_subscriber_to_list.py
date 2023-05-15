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


def add_subscriber_to_list(subscriber_id, list_id):
    url = f'{BASE_URL}/lists/{list_id}/relationships/profiles/'
    payload = {
        "data": [
            {
                "type": "profile",
                "id": subscriber_id
            }
        ]}
    response = requests.post(url, json=payload, headers=Headers)

    if response.status_code == 204:
        print("Subscriber added successfully")
    else:
        print(f'Error: {response.status_code}')
        return None

add_subscriber_to_list('your_subscriber_id','your_list_id')

