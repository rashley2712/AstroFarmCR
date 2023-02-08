import os

import flask
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")

@app.route("/<page>")
def page(page):
    print("page:", page)
    return flask.render_template(page)

@app.route("/robots.txt")
def robot():
    return """User-agent: Googlebot
        Disallow: /nogooglebot/

        User-agent: *
        Allow: /

    """

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

