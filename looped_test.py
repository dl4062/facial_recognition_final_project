import os
import json
import requests
import itertools
from operator import itemgetter
import time
from collections import Counter

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
    # need timer due to concurrent facial recongition limits
    time.sleep(1) ## https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/



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

#https://stackoverflow.com/questions/23240969/python-count-repeated-elements-in-the-list/23240989

counted_gender = dict(Counter(conf_gender_list))
counted_eth = dict(Counter(conf_eth_list))

#print(counted_eth)
#print(counted_gender)

#print(conf_eth_list)
#print(conf_gender_list)


## gender data

percent_female = (float(counted_gender["female"]/len(conf_gender_list)))*100
percent_male = (float(counted_gender["male"]/len(conf_gender_list)))*100

diff_female = percent_female - 50.8
diff_male = percent_male - 49.2


print("Analysis Complete")
print("-----------------------------------")
print("Here is the data breakdown")
print("Female - US Average: 50.8%")
print(f"Female - Your Data: {percent_female:.2f}%")
print("Male - US Average: 49.2%")
print(f"Male - Your Data: {percent_male:.2f}%")
print(f"Your data for females differs from the national average by: {diff_female:.2f}%")
print(f"Your data for males differs from the national average by: {diff_male:.2}%")

## eth data




















## https://docs.imagga.com/#uploads



#https://api.imagga.com/v2/faces/detections?image_url=%s%https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman%2C_2006_%28cropped%29.jpg,auth=acc_9e32028a57242cd,59a2adc9efbe16b40d9df8132fe72c49

