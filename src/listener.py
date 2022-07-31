"""Listener module."""
from sys import platform as _platform
from os import environ

from flask import Flask, request

from pprint import pprint
app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    """Endpoint for the root of the Flask app."""
    return "OK"

@app.route("/webhook", methods=["GET", "POST"])
def tracking():
    """Endpoint for receiving webhook from bitbucket."""
    if request.method == "POST":
        data = request.get_json()
        pprint(data)
        return "OK"
    else:
        return "Error"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
