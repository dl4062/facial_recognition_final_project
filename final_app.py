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

print("Please wait while the data is processing, it will take approx 1 second per picture")
## photo locator

data = os.path.join(os.path.dirname(__file__), "Data", "Test_Folder_1")  ## TODO add folder selector code
gender_list = []
eth_list = []
## TODO add folder selector
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

## gender data

counted_gender = dict(Counter(conf_gender_list))
counted_eth = dict(Counter(conf_eth_list))

percent_female = (float(counted_gender["female"]/len(conf_gender_list)))*100
percent_male = (float(counted_gender["male"]/len(conf_gender_list)))*100

diff_female = percent_female - 50.8
diff_male = percent_male - 49.2

print("Analysis Complete")
print("-----------------------------------")
print("Here is the gender data breakdown")
print("Female - US Average: 50.8%")
print(f"Female - Your Data: {percent_female:.1f}%")
print("Male - US Average: 49.2%")
print(f"Male - Your Data: {percent_male:.1f}%")
print(f"Your data for females differs from the national average by: {diff_female:.1f}%")
print(f"Your data for males differs from the national average by: {diff_male:.1f}%")

## eth data

percent_caucasian = (float(counted_eth["caucasian"]/len(conf_eth_list)))*100
percent_afroamerican = (float(counted_eth["afroamerican"]/len(conf_eth_list)))* 100
percent_latino = (float(counted_eth["latino"]/len(conf_eth_list)))*100
percent_CND = (float(counted_eth["Could not determine"]/len(conf_eth_list)))* 100
percent_asian = (float((counted_eth["east asian"]+counted_eth["east indian"])/len(conf_gender_list)))* 100

diff_caucasian = percent_caucasian - 60.4
diff_afroamerican = percent_afroamerican - 13.4
diff_latino = percent_latino - 18.3
diff_asian = percent_asian - 5.9

print("Here is the ethniticy data breakdown")
print("Caucasian - US Average: 60.4%")
print(f"Caucasian - Your Data: {percent_caucasian:.1f}%")
print("Afroamerican - US Average: 13.4%")
print(f"Afroamerican - Your Data: {percent_afroamerican:.1f}%")
print("Latino - US Average: 18.3%")
print(f"Latino - Your Data: {percent_latino:.1f}%")
print("Asian - US Average: 5.9%")
print(f"Asian - Your Data: {percent_asian:.1f}%")
print(f"Your data for Caucasians differs from the national average by: {diff_caucasian:.1f}%")
print(f"Your data for Afroamercians differs from the national average by: {diff_afroamerican:.1f}%")
print(f"Your data for Latinos differs from the national average by: {diff_latino:.1f}%")
print(f"Your data for Asians differs from the national average by: {diff_asian:.1f}%")
print(f"The API could not determine the following ethnicity for {percent_CND:.1f}% of the data")

## recommendation
threshold = 5
print("Final Recommendations")
print("-----------------------")
if diff_female > threshold or diff_male > threshold:
    print("This data does not have the recommended gender mix, cannot recommend this data")
else:
    print("This data has the recommended gender mix")

if diff_caucasian > threshold or diff_afroamerican > threshold or diff_latino > threshold or diff_asian > threshold:
    print("This data's diversity does not mirror that of the the US, we cannot recommend you use this data")
else:
    print(f"This data has the recommended data mix, however {percent_CND:.1f}% of the data could not be determined")

## https://docs.imagga.com/#uploads
#https://api.imagga.com/v2/faces/detections?image_url=%s%https://upload.wikimedia.org/wikipedia/commons/0/06/Morgan_Freeman%2C_2006_%28cropped%29.jpg,auth=acc_9e32028a57242cd,59a2adc9efbe16b40d9df8132fe72c49

