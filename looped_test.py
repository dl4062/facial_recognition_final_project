import os
import json
import requests
import itertools
from operator import itemgetter
import time

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("api_key")
api_secret = os.environ.get("api_secret")


## photo locator

data = os.path.join(os.path.dirname(__file__), "Data", "Test_Folder_1")  ## TODO add folder selector code
gender_list = []
eth_list = []
## TODO add folder selector
### TODO count pictures in folder
## loops through folder, sends through API, and spits out data
picture_data = (os.listdir(data))
for single_pic in picture_data:
    image_location = os.path.join(os.path.dirname(__file__), "Data", "Test_Folder_1", single_pic)
    image_path = image_location
    response = requests.post(
        'https://api.imagga.com/v2/uploads',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})
    upload_response = json.loads(response.text)
    #print(upload_response)
    upload = upload_response['result']['upload_id']
    image_upload_id = str(upload)
    request_url = f'https://api.imagga.com/v2/faces/detections?image_upload_id={image_upload_id}&return_face_attributes=1'
    response = requests.get(request_url,auth=(api_key, api_secret))
    parsed_response = json.loads(response.text)
    results = parsed_response['result'] 
    attribute = results['faces'][0]['attributes']
    sorted_attribute = sorted(attribute, key=itemgetter("label"))
    for label in sorted_attribute:  
        if label["type"] == "gender":
            gender_list.append(label)
        if label["type"] == "ethnicity":
            eth_list.append(label)
    time.sleep(1)

conf_gender_list = []
conf_eth_list = []

for x in gender_list:
    if x["confidence"] < 75.00:
        conf_gender_list.append("Could not determine")
    else:
        conf_gender_list.append(x["label"])

for y in eth_list:
    if y["confidence"] < 75.00:
        conf_eth_list.append("Could not determine")
    else:
        conf_eth_list.append(y["label"])

print(conf_eth_list)
print(conf_gender_list)







## https://docs.imagga.com/#uploads



#https://api.imagga.com/v2/faces/detections?image_url=%s%https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman%2C_2006_%28cropped%29.jpg,auth=acc_9e32028a57242cd,59a2adc9efbe16b40d9df8132fe72c49

