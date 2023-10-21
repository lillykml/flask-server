from terra.base_client import Terra
import datetime
import quickstart as qs

client = qs.terra

user = client.from_user_id("0b367074-3f27-49ee-968a-b0c68012e1ac")

start_date = datetime.datetime.now() - datetime.timedelta(days=1)
end_date = datetime.datetime.now()

activity_response = client.get_activity_for_user(user, start_date, end_date, to_webhook=False)

parsed_activities = activity_response.parsed_response.data
print(parsed_activities)

