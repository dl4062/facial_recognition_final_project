from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment

import requests
import json
import operator
from pprint import pprint

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")
image_url = 'https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman%2C_2006_%28cropped%29.jpg'

#https://api.imagga.com/v2/faces/detections?image_url=%s%https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman%2C_2006_%28cropped%29.jpg,auth=acc_9e32028a57242cd,59a2adc9efbe16b40d9df8132fe72c49



request_url = f'https://api.imagga.com/v2/faces/detections?image_url={image_url}&return_face_attributes=1'

response = requests.get(request_url,auth=(api_key, api_secret))

#print(type(response)) --> requests.models.Response

#changing data to dict from str
parsed_response = json.loads(response.text)
#pprint(parsed_response)

#Data Investigation
#print(type(parsed_response)) ---> dict
#print(parsed_response.keys()) #---> result, status
#print(parsed_response["result"])
#print(parsed_response["result"].keys()) #--> "faces"
#print(parsed_response["status"].keys()) #--> "text", "type"

results = parsed_response['result'] 
#pprint(results['faces'][0])

attribute = results['faces'][0]['attributes']
#pprint(attribute)

for p in attribute:
    pprint(['confidence']['label'][2])

















#pprint(parsed_response['result']['faces'][0])
#pprint(parsed_response['result']['faces'][0]['attributes'])

#print(face_results)
#print(type(face_results)) ---> list 
#print(type(face_results["faces"])) --> list 






#print(response.json())