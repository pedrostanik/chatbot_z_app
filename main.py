import requests
import os
from dotenv import load_dotenv

load_dotenv()

#Getting Env Variables
DEVICE_ID = str(os.getenv('DEVICE_ID'))
INTEGRATION_TOKEN = str(os.getenv('INTEGRATION_TOKEN'))
SECURITY_TOKEN = str(os.getenv('SECURITY_TOKEN'))

url = f"https://api.z-api.io/instances/{DEVICE_ID}/token/{INTEGRATION_TOKEN}/send-text"
headers = {
    "Client-Token": SECURITY_TOKEN
}
body = {
    "phone": "5514997703031",
    "message": "Hello, World!"
}

response = requests.post(url=url, headers=headers, data=body)
print(f'Response: {response.status_code}')
print(f'Response: {response.json()}')
