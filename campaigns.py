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


def get_campaigns():
    url = f'{BASE_URL}/campaigns'
    response = requests.get(url, headers=Headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

def create_campaign(name, list_id):
    url = f'{BASE_URL}/campaigns'
    payload = {"data": {
            "type": "campaign",
            "attributes": {
                "name": name,
                "channel": "email",
                 "audiences": {
                    "included": [list_id],
                    "excluded": []
                },
                "tracking_options": {"utm_params": [
                        {
                            "name": "utm_medium",
                            "value": "campaign"
                        }
                    ]}
            }
        }}
    response = requests.post(url, json=payload, headers=Headers)
    print(response.json())
    if response.status_code == 201:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

def update_campaign(campaign_id, data):
    url = f'{BASE_URL}/campaigns/{campaign_id}'
    response = requests.patch(url, json=data, headers=Headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(response.json())
        print(f'Error: {response.status_code}')
        return None

def delete_campaign(campaign_id):
    url = f'{BASE_URL}/campaigns/{campaign_id}'
    response = requests.delete(url, headers=Headers)

    if response.status_code == 204:
        print('Campaign deleted successfully')
    else:
        print(response.json())
        print(f'Error: {response.status_code}')


print("## Getting all campaigns ###")
campaigns = get_campaigns()
print(campaigns)
print("## End of -- Getting all campaigns ###")

print("## Creating a new campaign ###")
new_campaign = create_campaign('Test Random Campaign', 'your_list_id_here')
print(new_campaign)
print("## End of -- Creating a new campaign ###")

print("## Updating a campaigns ###")
updatedCampaign = {
"data": 
{"type": "campaign",
    "attributes": {
        "name": "My new campaign"
    },
    "id": 'your_campaign_id_here'
}}
updated_campaign = update_campaign('your_campaign_id_here', updatedCampaign)
print(updated_campaign)
print("## End ot -- Updating a campaigns ###")

print("## Deleteing a campaigns ###")
delete_campaign('your_campaign_id_here')
print("## End of -- Deleting a campaigns ###")
