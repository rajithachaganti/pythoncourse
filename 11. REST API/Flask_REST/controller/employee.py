from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


class EmployeeStore(Resource):

    def post(self,eid):
        print("------In post method executing------")
        e_data = request.get_json()
        print(e_data)
        # Validate UI data
        if len(e_data['mobile']) == 10:
            e_data['mobile'] = '+91-'+e_data['mobile']
        if e_data.get('loc') == None:
            e_data['loc'] = 'HYD'
        if e_data.get('gender') == None:
            e_data['gender'] = 'F'
        print(e_data)
        # Pass this to service layer,persist in db
        return {'message':"Success",'status_code':200}


    def get(self,eid):
        print("----I am in get method---------",eid)
        return 'Hello World'
