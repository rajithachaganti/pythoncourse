''''''
'''
Service   :
---------------
             1. Receive the validated data from Controller
             2. If required interact with database for more data (dao layer call)
             3. Implement business logic as per give requirement
             4. Call dao layer(Pass the data) for data persistence
             5. Get response from DAO and send it to controller

'''
from _21_2_DB_String._1_CREATE_strs._3_dao import save_to_db
# Business logic
def get_len(str_val):
    le = 0
    for each in str_val:
        le += 1
    save_to_db(str_val, le)
    return le