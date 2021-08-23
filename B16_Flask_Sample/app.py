
'''
UI --->   PYTHON
   <--   Controller

Local DEV TEST UAT PRODUCTION

'''
# Controller

from flask import Flask
from service_code import find_sum

app = Flask(__name__)

@app.route('/')
def index_page():
    return "Hello World.Welcome to Python world."
'''
Requirement: Find sum of digits of mobile number

Analysis : Functional/Technical
           Techincal analysis : API Call prep:
                                
Design : 
Development:
Testing:
Production:
'''

@app.route('/getlen/<in_no>')
def get_length(in_no):
    print("Received number ", in_no)  # logging mechanism
    # server side validations
    # if success
        # call service layer and pass data
    # else
        # return error message
    return {"add_mob_digits": 32}

@app.route('/addnum/<mob_no>')   #   %10 *123
def get_digits_sum(mob_no):
    print("Mobile number data:  ", mob_no)
    sum = find_sum(mob_no)
    return {"result": str(sum), "status_code": 200}




@app.route('/getallnumbers')
def get_mobile_info():
    # service layer
    # return data
    pass


if __name__ =='__main__':
    app.run(host='localhost', port=5433, debug=True)
    # app.run()
    # app.run(host='localhost', port=4000)
    # app.run(debug=True)
    # app.run(port = '4050', debug=True)
