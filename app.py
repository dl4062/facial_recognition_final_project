import os




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

