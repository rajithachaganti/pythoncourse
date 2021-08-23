from flask import Flask, request, jsonify
from controller.employee import EmployeeStore
from controller.test import WelcomePage
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Employee Operations
api.add_resource(WelcomePage, '/')
api.add_resource(EmployeeStore, '/api/v1/emp_ops/<eid>') # /api/v1/emp_ops/10  /api/v1/emp_ops/11

'''
1. When Client sends request with 
     '/' as suffix url and 
     GET as request method 

2. Flask with REST api integration
     I . Flask framework will load the respective resource clasas i.e,  WelcomePage 
     II. Create the object for WelcomePage class   
            obj = WelcomePage()
     III.Based on request method,
            GET    - obj.get()
            POST   - obj.post()
            PUT    - obj.put()
            DELETE - obj.delete()
'''

if __name__ == '__main__':
    app.run(host="127.0.0.1", port = "5555")