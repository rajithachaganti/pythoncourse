from requests import request

from flask import Flask, request, jsonify
from mydata.controller import HomePage
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

api.add_resource(HomePage, '/api/v1/datapart')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port = 5444)