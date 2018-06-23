#!/usr/bin/python

from flask import Flask
from flask_restful import Resource, Api
from OpDefine import DFX

__authon__ = "salmansamie"


application = Flask(__name__)
fsk_api = Api(application)


class OpenDefineApi(Resource):
    def get(self):
        return {
            "project author": "Salman Rahman (salmansamie)",
            "source code": "https://github.com/salmansamie/OpDefine.git",
            "license": "GNU GPL v3.0"
        }


class GetMultipart(Resource):
    def get(self, param):
        return DFX(param).define()


if __name__ == "__main__":
    fsk_api.add_resource(OpenDefineApi, '/')
    fsk_api.add_resource(GetMultipart, '/api/v3/<str:param>')
    application.run(debug=True)
