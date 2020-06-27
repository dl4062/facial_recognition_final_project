import os

import requests

from dotenv import load_dotenv
load_dotenv()

image_location = os.path.join(os.path.dirname(__file__), "data", "Test_Folder_1")



api_key = "api_key"
api_secret = "api_secret"
image_path = image_location

response = requests.post(
    'https://api.imagga.com/v2/uploads',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
print(response.json())