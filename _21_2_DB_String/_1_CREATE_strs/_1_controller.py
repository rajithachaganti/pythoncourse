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
REQ:  Find length of the strings given by customer and save into db 

CRUD           - R
Datattypes     - int string
STATE,BEHVAIOR -
'''
from _21_2_DB_String._1_CREATE_strs._2_service import get_len

# Controller
def get_str_len(in_str):
    if in_str == '':
        return "Enter valid string"
    else:
        # st_len = _2_service.get_len(in_str)
        st_len = get_len(in_str)
        return st_len


# UI Layer
str1 = input("Enter string details  : ")

resp = get_str_len(str1) # flask, django

print("String length :", resp)