from flask import Flask, request, jsonify
from controller.employee import EmployeeStore
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Employee Operations
api.add_resource(EmployeeStore, '/api/v1/emp_ops/<eid>')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port = "5555")