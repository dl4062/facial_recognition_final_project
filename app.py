import os

import requests

from dotenv import load_dotenv
load_dotenv()



## pulling key from .env file
API_KEY = os.environ.get("rapid_api_key")


## code snippet taken from luxand.cloud facial recognition

url = "https://luxand-cloud-face-recognition.p.rapidapi.com/photo/detect"

payload = "photo=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2F0%2F06%2FMorgan_Freeman%252C_2006_%2528cropped%2529.jpg"    ## add photo file name/path here - will need to connect to file structure eventually using code at the bottom
headers = {
    'x-rapidapi-host': "luxand-cloud-face-recognition.p.rapidapi.com",
    'x-rapidapi-key': API_KEY,
    'content-type': "application/x-www-form-urlencoded"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

'''


## connecting code to folder stucture where picture data sits

data = os.path.join(os.path.dirname(__file__), "data")

face_data = (os.listdir(data))
for folder in face_data:
    print(folder)

choice = input("Please select a data package to analyze: ")

## data validation part

while os.path.exists(os.path.join(data, choice)) == False:
    if os.path.exists(os.path.join(data, choice)) == False:
        choice = input("This data package does not exist in the Data folder - Please select a data package from the specified list, or add a new data package and run the application again: ")
    else:
        break

print(choice)

'''
