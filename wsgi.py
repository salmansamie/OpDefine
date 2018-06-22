#!/usr/bin/python

from flask import Flask

__authon__ = "salmansamie"


application = Flask(__name__)


@application.route("/")
def app_root():
    return "test deploy"


if __name__ == "__main__":
    application.run()
