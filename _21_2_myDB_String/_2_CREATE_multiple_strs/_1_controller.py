

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
from _21_2_myDB_String._2_CREATE_multiple_strs._2_service import get_len

# Controller
def get_str_len(in_str):
    if in_str == '':
        return "Enter valid string"
    else:
        # st_len = _2_service.get_len(in_str)
        st_len = get_len(in_str)
        return st_len


# UI Layer
str1 = input("Enter string : ")

resp = get_str_len(str1) # flask, django
for word,le in resp.items():
    print("String length of {}:{}".format(word,le))