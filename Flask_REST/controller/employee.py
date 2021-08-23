from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


class EmployeeStore(Resource):

    def post(self, eid):
        print("------In post method executing------")
        e_data = request.get_json()
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
        return e_data
