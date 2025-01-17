from flask import Flask, request, jsonify, render_template
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio credentials from config.py
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Home page
@app.route("/")
def home():
    return render_template("index.html")

# API to get a virtual number (Twilio number)
@app.route("/get-number", methods=["GET"])
def get_number():
    return jsonify({"virtual_number": TWILIO_PHONE_NUMBER})

# API to receive SMS
@app.route("/receive-sms", methods=["POST"])
def receive_sms():
    from_number = request.form.get("From")
    message_body = request.form.get("Body")
    return jsonify({"from": from_number, "message": message_body})

if __name__ == "__main__":
    app.run(debug=True)
