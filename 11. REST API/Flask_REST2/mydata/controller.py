from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
import requests,json
from flask_restful import Resource, Api

class HomePage(Resource):

    def get(self):
        print("------In WelcomePage GET method ------")
        url = "https://jsonplaceholder.typicode.com/todos"
        # Doing external service rest api call
        res = requests.get(url)
        data = json.loads(res.text)
        print("----Data retrieved from jsonplaceholder----")
        for rec in data:
            print(rec)
        return {'message': data, 'status_code': res.status_code}


    def post(self):
        print("------In WelcomePage POST method ------")
        u_data = request.get_json()
        print("POST API Call Data : ", u_data)

        # server side validations
        if not (type(u_data['userId']) == int and type(u_data['title']) == str and type(u_data['body']) == str):
            return {'message': "Please enter valid data",  'status_code':  300}
        url = "https://jsonplaceholder.typicode.com/posts"

        # REST API Call
        '''
        Request URL : https://jsonplaceholder.typicode.com/posts
        Request method: post()
        Payload : data = {  "userId": 101,
                            "title" : "Madhu Nettem Software Engineer",
                            "body" : "Sample Data"
                        }
        '''
        res = requests.post(url, data = u_data)
        data = json.loads(res.text)
        return {'message': "Successfully Inserted", "data":data, 'status_code':  res.status_code}


    def put(self):
        print("------In WelcomePage PUT method ------")
        obj = request.get_json()
        #print(obj["id"])
        # value = requests.args
        url = "https://jsonplaceholder.typicode.com/posts/"+ str(obj['userId'])
        #print(url)
        res = requests.put(url, data=obj)
        #print(res.text)
        data = json.loads(res.text)
        return {'message': "successfully updated", "data": data, 'status_code': res.status_code}

    def delete(self):
        print(request.form.get("id"))
        value = request.form.get("id")
        url = "https://jsonplaceholder.typicode.com/posts/" + str(value)
        #print(url)
        res = requests.delete(url)
        #print(res.text)
        data = json.loads(res.text)
        return {'message': "record deleted",'status_code': res.status_code}


