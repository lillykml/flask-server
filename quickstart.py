from terra.base_client import Terra
import os

api_key = os.getenv('API_KEY')
dev_id = os.getenv('DEV_ID')

terra = Terra(api_key=api_key, dev_id=dev_id, secret="YOUR TERRA SECRET")

widget_response = terra.generate_widget_session(
    reference_id="USER ID IN YOUR APP",
    providers=["CRONOMETER", "OURA", "GARMIN", "APPLE"],
    auth_success_redirect_url="https://example.com/success",
    auth_failure_redirect_url="https://example.com/failure",
    language="en"
).get_parsed_response()

auth_url = widget_response.url
print(widget_response.url)