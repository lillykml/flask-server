import os
import json
from dotenv import load_dotenv
from terra.base_client import Terra
from datetime import datetime
 

# Load environment variables from .env file
load_dotenv()

# Use the loaded variables
database_uri = os.getenv("DATABASE_URI")
secret_key = os.getenv("SECRET_KEY")

TERRA_API_KEY = os.getenv("TERRA_API_KEY")
TERRA_DEV_ID = os.getenv("TERRA_DEV_ID")
TERRA_SECRET = os.getenv("TERRA_SECRET")

terra = Terra(api_key=TERRA_API_KEY, dev_id=TERRA_DEV_ID, secret=TERRA_SECRET)

# Print a Provider List
def get_provider_list():
    api_response = terra.list_providers()
    parsed_api_response = api_response.get_parsed_response()
    return parsed_api_response
 
# Get a Connect Device URL
def generate_widget_url(userid): 
    widget_response = terra.generate_widget_session(
        reference_id=userid,
        providers=["CRONOMETER", "OURA", "GARMIN", "APPLE"],
        auth_success_redirect_url="https://example.com/success",
        auth_failure_redirect_url="https://example.com/failure",
        language="en"
    ).get_parsed_response()
    #TODO just return the url and access it somehow in the frontend
    return widget_response.url

def list_users():
    res = terra.list_users()
    print(res.json)

def get_uid_from_name(ref_id):
    users = terra.list_users()
    for i in range(len(users.json["users"])):
        if users.json["users"][i]["reference_id"] == ref_id:
            return users.json["users"][i]["user_id"]

list_users()

# generate_widget_url("test_user")

