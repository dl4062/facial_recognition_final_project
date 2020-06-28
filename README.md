# Facial Recognition Freestyle Project

This repo will help you determine the diversity a group of photos using the imagga API. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

After cloning the repo, you will need to set up a virtual environment on your machine. 

The requirements.txt file includes the modules you will need to install to run this program.  Enter the below code in your command line to set up the appropriate virtual environment. 

```
conda create -n project-env python=3.7 # (first time only)
conda activate project-env
pip install -r requirements.txt
```

### Set-up

Request an API key from the following website: https://imagga.com/

Once you have your API key and API secret, create a .env file and add the keys in the appropriate global variables:

```
api_key = 'Enter your API key here'
api_secret = 'Enter your API secret here'
```

Create a subfolder in the Data folder and place the photo set you would like to analyze in your subfolder. You can create as many subfolders as you would like but you can only analyze one folder at a time. 

The app is configured to have an even split of ethnicities and genders so that the photo set can test a diverse group of pictures.

Please give the program some time to run, it will take approximately 1 second per photograph due to API constraints. 

Once the program is complete, it will tell you the demographics of your photo set broken down by ethnicity and gender, and if there were any pictures where the ethnicity could not be determined.  At the end, there will be recommendation telling you if the data set was diverse enough for facial recognition testing.  

'''


