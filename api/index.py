from flask import Flask
import os
import time

app = Flask(__name__)

VALID_KEY = "test123"
CLAIM_FILE = "/tmp/claimed.txt"

@app.route("/")
def home():
    return "Cyber Ramadan Portal - Awaiting Key"

@app.route("/<key>")
def check(key):

    if os.path.exists(CLAIM_FILE):
        return "Access Already Claimed."

    if key == VALID_KEY:
        with open(CLAIM_FILE, "w") as f:
            f.write(str(time.time()))
        return "Access Granted."

    return "Invalid Key."

app = app