#!/usr/bin/python

from flask import Flask
from flask_restful import Resource, Api
from OpDefine import DFX
import json

__authon__ = "salmansamie"


application = Flask(__name__)
fsk_api = Api(application)


class OpenDefineApi(Resource):
    @staticmethod
    def get():
        return {
            "project author": "Salman Rahman (salmansamie)",
            "source code": "https://github.com/salmansamie/OpDefine.git",
            "license": "GNU GPL v3.0"
        }


class GetMultipart(Resource):
    @staticmethod
    def get(param):
        return json.dumps(DFX(param).define())          # type: dict


if __name__ == "__main__":
    fsk_api.add_resource(OpenDefineApi, '/')
    fsk_api.add_resource(GetMultipart, '/api/v3/<string:param>')
    application.run(debug=True)
