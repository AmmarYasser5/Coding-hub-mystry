from flask import Flask
import hashlib
import time
import os

app = Flask(__name__)

VALID_KEY = "PUT_YOUR_KEY_HERE"
CLAIM_FILE = "/tmp/claimed.txt"

@app.route("/")
def home():
    return """
    <html>
    <head>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <div class='terminal'>
            <h2>Cyber Ramadan Portal</h2>
            <p>Awaiting Key...</p>
        </div>
    </body>
    </html>
    """

@app.route("/<key>")
def check(key):

    if os.path.exists(CLAIM_FILE):
        return render_message("Access Already Claimed.")

    if key == VALID_KEY:
        with open(CLAIM_FILE, "w") as f:
            f.write(str(time.time()))
        return render_message("Access Granted. Points Locked.")

    return render_message("Invalid Key.")

def render_message(msg):
    return f"""
    <html>
    <head>
        <link rel="stylesheet" href="/style.css">
    </head>
    <body>
        <div class='terminal'>
            <h2>{msg}</h2>
        </div>
    </body>
    </html>
    """

app = app