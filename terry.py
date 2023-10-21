import os
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
    print(widget_response)

def list_users():
    res = terra.list_users()
    print(res.json)

list_users()

# Create a user object
#This is the userid from the user I just created
# USER_ID = "fb0eb88d-12cc-493a-ba25-536b7cda8eac"
# terra_user = terra.from_user_id(USER_ID)

# res = terra.get_user_info(terra_user)
# print(res.json)
 
# Get the nutrition data from start date to current time
# res = terra_user.get_daily(start_date=datetime(2023, 10, 19), end_date=datetime(2023, 10, 21), to_webhook=True, with_samples=True)
# print(res.json)