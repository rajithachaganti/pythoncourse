'''
@author: madhu
This is Controller layer

'''

import json
from _21_3_EMP_DETAILS.service.emp_service import EmpService


def save_emp_data():
    # 1. Receive data from UI (Here from json file)
    with open('in_emp_data.json') as file_obj:
        data = json.load(file_obj)
    print("Data received from employee :", data)
    # 2. Extract the data
    e_code = data["eCode"]
    user_id = data['userId'].capitalize()
    full_name = data["fullName"]
    tech = data['tech']
    role = data['role']
    region = data['region'].capitalize()
    mobile = data['mobile']
    email = data['email'].upper()
    emp = EmpService(e_code, user_id,full_name, tech, role, region, mobile, email)
    # 3. Perform server side validations
    res = emp.validate_uid()
    print("res=",res)
    if res:
        # 4.2. send exception message to UI
        return "User already exists"
    else:
        # 4.1. pass data to SERVICE layer
        res = emp.save_emp_details()
        # 13. Receive the data from Service, and send to UI
        return res
    
if __name__ == '__main__':
    output = save_emp_data()
    if output:
        print("***** Congratulations! Your signup completed ***** ")
        # return "Congratulations! Your signup completed"
    else:
        print("***** User already exists with this ID. ***** ")
        #return "Invalid login Attempt . Please provide valid credentials to prevent your login from being disabled."
