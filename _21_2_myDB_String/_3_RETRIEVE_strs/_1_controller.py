

'''
UI --1-->                    Python                                   ----> Database
         --2.1-->  Controller  --2.2-->  Service  --2.3-->  DAO -->
         <--3.3--              <--3.2--           <--3.1--      <--
'''


'''
Mobileno : Client validations --> 10 digit,all numbers  
           Server validations --> valid no or not  

'''

'''
Controller   :
---------------
             1. Receive the request data from UI,     (json,xml to dict) 
           2.1. Perform server side validations and
                 if success: Pass the data to Service layer
                 else      : Send error response details
           2.2. Pass the data to Service layer
             3. Receive response from Service layer 
             4. Prepare resp data and send to UI
             
'''

'''
REQ:  Find length of the string

CRUD           - R
Datattypes     - int string
STATE,BEHVAIOR -
'''
from _21_2_myDB_String._3_RETRIEVE_strs._2_service import get_str_details

# Controller
def get_str_data():
    # st_len = _2_service.get_len(in_str)
    st_data = get_str_details()
    return st_data


# UI Layer
option = input("Do you want to retrieve string info ? If YES enter 1 If NO enter 2:")
if int(option) == 1:
    resp = get_str_data() # flask, django
    print("Final response data : ")
    resp.update({'status_code':200})
    print('dict=',resp.items())
    for each in resp['response']:
        print(each[0]," **  ", each[1])
else:
    print("Please try again !! ")
