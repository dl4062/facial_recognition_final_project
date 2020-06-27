import os
import json
import requests
import itertools
from operator import itemgetter

from dotenv import load_dotenv
load_dotenv()

image_location = os.path.join(os.path.dirname(__file__), "Data", "Test_Folder_1", "Morgan_Freeman.jpg")

## https://docs.imagga.com/#uploads

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")

image_path = image_location
response = requests.post(
    'https://api.imagga.com/v2/uploads',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
#print(response.json())
upload_response = json.loads(response.text)
#upload_id = upload_response['upload_id']
upload = upload_response['result']['upload_id']
#print(upload)


## adding in code from "practice.py" to test

image_upload_id = str(upload)

#https://api.imagga.com/v2/faces/detections?image_url=%s%https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman%2C_2006_%28cropped%29.jpg,auth=acc_9e32028a57242cd,59a2adc9efbe16b40d9df8132fe72c49

request_url = f'https://api.imagga.com/v2/faces/detections?image_upload_id={image_upload_id}&return_face_attributes=1'


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

sorted_attribute = sorted(attribute, key=itemgetter("label"))
#pprint(sorted_attribute)

confidence_by_label = itertools.groupby(sorted_attribute, key=itemgetter("label")) 
for label, labels in confidence_by_label:
    print("----------------------------")
    print(label + ":")
    for label in labels:
        print(label["confidence"])




#print(response.json())
