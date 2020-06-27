from dotenv import load_dotenv
import os

load_dotenv() #> loads contents of the .env file into the script's environment

import requests
import json
import itertools
from operator import itemgetter
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

#print(type(attribute)) --> list

type = []

#for t in attribute:
 #   type.append(t["type"])
#pprint(type)

#for c in attribute:
 #   print(c['confidence'])

sorted_attribute = sorted(attribute, key=itemgetter("type"))
#pprint(sorted_attribute)

confidence_by_type = itertools.groupby(sorted_attribute, key=itemgetter("type")) 
for type, types in confidence_by_type:
    print("----------------------------")
    print(type + ":")
    for type in types:
        print(type["confidence"])




#print(response.json())
