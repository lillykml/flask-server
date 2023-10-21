from flask import Flask

app = Flask(__name__)

# Members API Route Example
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/avgheartrate")
def getavgheartrate():
    return {"avgheartrate": [98, 64, 66, 68, 71]}

if __name__ == "__main__":
    app.run(debug=True)