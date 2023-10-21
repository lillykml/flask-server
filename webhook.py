import logging
import flask
from flask import request
from terra.base_client import Terra
import quickstart as qs

logging.basicConfig(level=logging.INFO)

terra = Terra(api_key= qs.api_key, dev_id=qs.dev_id, secret="SIGNING-SECRET")

app = flask.Flask(__name__)

@app.route("/consumeTerraWebhook", methods=["POST"])
def consume_terra_webhook() -> flask.Response:
    body = request.get_json()
    verified = terra.check_terra_signature(
        request.get_data().decode("utf-8"), request.headers['terra-signature']
    )
    if verified:
      return flask.Response(status=200)
    else:
      return flask.Response(status=403)


if __name__ == "__main__":
    app.run(host="localhost", port=8080)