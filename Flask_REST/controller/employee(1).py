from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import requests


class EmployeeStore(Resource):

    def post(self, eid):
        e_data = request.get_json()
        # print("DEBUG ::In post method executing for customer------", e_data)
        print("INFO ::In post method executing for customer------", eid)
        # Validate the data
        # Pass this to service layer,persist in db
        return {'message':"Successfully store the data ",'status_code':200}


    def get(self, eid):  # eid = 7839
        print("----I am in get method---------", eid)
        # Call service layer and get data
        # e_data = get_edata(eid)
        e_data = {'empno':7839,
                  'ename': 'KING',
                  'job': 'PRESIDENT',
                  'mgr': None,
                  'hiredate': '17-11-1981',
                  'sal': 5000,
                  'comm': None,
                  'deptno': 10,
                  }
        url = 'https://rapidprod-sendgrid-v1.p.rapidapi.com/alerts'
        data = requests.get(url)
        print(data)
        return e_data

'''
# Specification
class Animal:
    def sleeping(self):
        pass
    def eating(self):
        pass
'''


