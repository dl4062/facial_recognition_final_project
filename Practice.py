from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment

import requests


api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")
image_url = 'https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman%2C_2006_%28cropped%29.jpg'



request_url = f'https://api.imagga.com/v2/faces/detections?image_url={image_url}&return_face_attributes=1'

response = requests.get(request_url,auth=(api_key, api_secret))


print(response.json())