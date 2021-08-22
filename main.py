import os
import requests
from datetime import datetime
from dotenv import load_dotenv


# Load .env file
load_dotenv("/Volumes/Workstation/Learning Center/Data Science/"
            "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")

# Constants
TODAY = datetime.today().strftime("%Y%m%d")
VARIABLE_DATE = datetime(year=2021, month=8, day=22).strftime("%Y%m%d")
HOURS = str(4)
USERNAME = "thewildmonk"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_API_KEY = os.getenv("PIXELA_API_KEY")
PIXELA_HEADER = {
    "X-USER-TOKEN": PIXELA_API_KEY,
}

# Crete Pixela user
PIXELA_PARAMS = {
    "token": PIXELA_API_KEY,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "message": "success",
}

# Create Pixela Graph
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_PARAMS = {
    "id": "htgraph",
    "name": "Habit Tracker Graph",
    "unit": "hr",
    "type": "float",
    "color": "sora",
}

# Post a Pixela pixel
PIXELA_POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_PARAMS['id']}"
POST_PIXEL_PARAMS = {
    "date": TODAY,
    "quantity": HOURS,
}

# # Create user & graph
# response = requests.post(url=PIXELA_ENDPOINT, json= PIXELA_PARAMS)
# print(response.text)
# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, headers=PIXELA_HEADER, json=GRAPH_PARAMS)
# print(response.text)

#  Post a pixel
response = requests.post(url=PIXELA_POST_PIXEL_ENDPOINT, headers=PIXELA_HEADER, json=POST_PIXEL_PARAMS)
print(response.text)

# # Update a pixel
# change_pixel_response = requests.put(url=f"{PIXELA_POST_PIXEL_ENDPOINT}/{VARIABLE_DATE}",
#                                      headers=PIXELA_HEADER, json=POST_PIXEL_PARAMS)
# print(change_pixel_response.text)

# # Delete a pixel
# delete_pixel_response = requests.delete(url=f"{PIXELA_POST_PIXEL_ENDPOINT}/{VARIABLE_DATE}", headers=PIXELA_HEADER)
# print(delete_pixel_response.text)
