import platform
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
def send_post_data(path):
    path_is_valid_email = validate_email(path, verify=True)
    if path_is_valid_email:
        send_email(path, request.data)
        return request.data
    else:
        return "Specified email address {} is not valid.".format(path)


def send_email(recipient, message):
    me = "hooktest@{}".format(platform.node())
    message = MIMEText(message)
    message["Subject"] = "Incoming Request Data"
    message["From"] = me
    message["To"] = recipient
    smtp_server = smtplib.SMTP('localhost')
    smtp_server.sendmail(me, [recipient], message.as_string())
    smtp_server.quit()


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
