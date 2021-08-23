from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


class WelcomePage(Resource):

    def get(self):
        print("------In WelcomePage GET method ------")
        return {'message': "GET: Hello World", 'status_code': 200}


    def post(self):
        print("------In WelcomePage POST method ------")

        return {'message': "POST: Welcome to python world", 'status_code': 200}


    def put(self):
        print("------In WelcomePage PUT method ------")

        return {'message': "PUT: Update the data", 'status_code': 200}
