from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import requests

class WelcomePage(Resource):

    def get(self):
        print("------In WelcomePage GET method ------")
        url = 'https://reqres.in'  # hdfcbank.com
        print("---------Get all users information-----------")
        # Prepare API CALL    f_url get
        suf = '/api/users?page=2'
        f_url = url + suf
        data = requests.get(f_url)  # Web service call
        print(data.json())
        data = data.json()
        for key, val in data.items():
            print(key, val)
            if key == 'data':
                for record in val:
                    print(record)
        return {'data': data, 'status_code': 200}


    def post(self):
        print("------In WelcomePage POST method ------")

        return {'message': "POST: Welcome to python world", 'status_code': 200}


    def put(self):
        print("------In WelcomePage PUT method ------")

        return {'message': "PUT: Update the data", 'status_code': 200}
