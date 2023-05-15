import requests
from dotenv import dotenv_values

config = dotenv_values(".env")
API_KEY = config['API_KEY']
BASE_URL = config['BASE_URL']

payload = {
    "data": {
        "type": "profile",
        "attributes": {
            "email": "test1@gmail.com",
            "phone_number": "+15003330001",
            "external_id": "1100111",
            "first_name": "John",
            "last_name": "Doe",
            "organization": "Draft",
            "title": "Designer",
            "location": {
                "address1": "89 E 42nd St",
                "address2": "1st floor",
                "city": "New York",
                "country": "United States",
                "region": "NY",
                "zip": "10017",
                "timezone": "America/New_York"
            }
        }
    }
}

Headers = {
    "accept": "application/json",
    "revision": "2023-05-11",
    "content-type": "application/json",
    "Authorization": "Klaviyo-API-Key "+ API_KEY
}

def create_subscriber():
    url = f'{BASE_URL}/profiles'
    
    response = requests.post(url, json=payload, headers=Headers)

    if response.status_code == 201:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

new_subscriber = create_subscriber()
print(new_subscriber)
