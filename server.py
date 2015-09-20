import smtplib
import sys
from flask import Flask, request
from email.mime.text import MIMEText
from validate_email import validate_email


app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    return "Hooktest requires the target email to be specified in the URL - i.e. \"https://my.hooktest.url/my.email.address@gmail.com\""


@app.route("/<path:path>", methods=["GET", "POST"])
def check_email(path):
    msg = MIMEText(request.data)
    path_is_valid_email = validate_email(path, verify=True)
    if path_is_valid_email:
        return "True"
    else:
        return "Specified email address {} is not valid.".format(path)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
