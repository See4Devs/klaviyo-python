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

def update_subscriber(list_id, subscriber_id, properties):
    url = f'{BASE_URL}/profiles/{subscriber_id}'

    payload = {
        "data": {
            "type": "profile",
            "id": subscriber_id,
            "attributes": properties
        }
    }
    
    response = requests.patch(url, json=payload, headers=Headers)
    print(response.json())
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None


def remove_subscriber_from_list(list_id, subscriber_id):
    url = f'{BASE_URL}/lists/{list_id}/relationships/profiles/'

    payload = {
        "data": [
        {
            "type": "profile",
            "id": subscriber_id
        }
    ]}
    response = requests.delete(url, json=payload, headers=Headers)

    if response.status_code == 204:
        print('Subscriber removed successfully')
    else:
        print(f'Error: {response.status_code}')

updated_subscriber = update_subscriber('your_list_id_here', 'your_subscriber_id_here', {'email': 'test@gmail.com'})
remove_subscriber_from_list('your_list_id_here', 'your_subscriber_id_here')

