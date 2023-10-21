import terry
import authenticate_user as au
from terra.base_client import Terra
from datetime import datetime, timedelta

uid = terry.get_uid_from_name(au.USERNAME)

# Create a user object
#This is the userid from the user I just created
terra_user = terry.terra.from_user_id(uid)
 
# want data for the past week
end_date = datetime.now()
week_ago = end_date - timedelta(days=7)

weekly = terra_user.get_daily(start_date=week_ago, end_date=end_date, to_webhook = False)
weekly_data = weekly.json["data"]

# functions for adding all data from a week
def add_weekly3(weekly_data, data_list, field, subfield, subsubfield):
    for i in range(7):
        data_list.append(weekly_data[i][field][subfield][subsubfield])

def add_weekly2(weekly_data, data_list, field, subfield):
    for i in range(7):
        data_list.append(weekly_data[i][field][subfield])

def add_weekly1(weekly_data, data_list, field):
    for i in range(7):
        data_list.append(weekly_data[i][field])
        
weekly_avg_heartrate = []
add_weekly3(weekly_data, weekly_avg_heartrate, "heart_rate_data", "summary", "avg_hr_bpm")
# print(weekly_avg_heartrate)

weekly_avg_stress = []
add_weekly2(weekly_data, weekly_avg_stress, "stress_data", "avg_stress_level")
# print(weekly_avg_stress)

weekly_calories = []
add_weekly2(weekly_data, weekly_calories, "calories_data", "total_burned_calories")
# print(weekly_calories)

weekly_steps = []
add_weekly2(weekly_data, weekly_steps, "distance_data", "steps")
# print(weekly_steps)

dummy_mood = ['sad', 'happy', 'sad', 'neutral', 'neutral', 'happy', 'neutral']