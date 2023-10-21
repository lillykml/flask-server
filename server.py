from flask import Flask
import authenticate_user as au
import query_data as qd

app = Flask(__name__)

# Members API Route Example
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/auth")
def auth():
    return {"auth_url": [au.auth_url]}

@app.route("/weekly_heartrate")
def get_weekly_heartrate():
    return {"weekly_heartrate": qd.weekly_avg_heartrate}

@app.route("/weekly_stress")
def get_weekly_stress():
    return {"weekly_stress": qd.weekly_avg_stress}

@app.route("/weekly_calories")
def get_weekly_calories():
    return {"weekly_calories": qd.weekly_calories}

@app.route("/weekly_steps")
def get_weekly_steps():
    return {"weekly_steps": qd.weekly_calories}

@app.route("/weekly_mood")
def get_weekly_mood():
    return {"weekly_mood": qd.dummy_mood}

if __name__ == "__main__":
    app.run(debug=True)