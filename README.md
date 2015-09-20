# Hooktest

Hooktest is a utility service for testing webhooks. Say you are creating a webhook for your service, and you need an easy way to make sure it is firing off properly during development. Hooktest is a service you can run which will send you an email containing the data it received.

# Example

Say you have a flask site and you want to send some form data you get to another service. If you have Hooktest running somewhere your application can reach (whether locally on a different port, or somewhere else in your network), you can point your webhook to Hooktest during development. Once you do this, you will receive emails containing the body of the POST request at the specified email address every time the webhook is called.

```
import requests
from flask import Flask, request


app = Flask(__name__)


@app.route("/form", methods=["POST"])
def form():
    try:
        requests.post("https://my.hooktest.url/my.email.address@gmail.com", data=request.json)
        return "Data received."
    except:
        return "Unexpected error."


if __name__ == "__main__":
    app.run()
```

# Usage

Hooktest's usage is simple - if Hooktest is running at "https://my.hooktest.url", then make your POST request to "https://my.hooktest.url/my.email.address@gmail.com" where "my.email.address@gmail.com" is the email address you want the data sent to.
