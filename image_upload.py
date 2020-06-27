import os

import requests

from dotenv import load_dotenv
load_dotenv()

image_location = os.path.join(os.path.dirname(__file__), "Data", "Test_Folder_1", "Morgan_Freeman.jpg")

api_key = "acc_ec2f68ce46a3237"
api_secret = "af7a1f3ca8999e0d4e541ebb2323cd43"


image_path = image_location
response = requests.post(
    'https://api.imagga.com/v2/uploads',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
print(response.json())