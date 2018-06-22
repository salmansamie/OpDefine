#!/usr/bin/python

from flask import Flask

__authon__ = "salmansamie"


app = Flask(__name__)


@app.route("/")
def app_root():
    return "test deploy"


if __name__ == "__main__":
    app.run()
