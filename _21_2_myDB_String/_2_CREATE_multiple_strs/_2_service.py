'''
Service   :
---------------
             1. Receive the validated data from Controller
             2. If required interact with database for more data (dao layer call)
             3. Implement business logic as per give requirement
             4. Call dao layer(Pass the data) for data persistence
             5. Get response from DAO and send it to controller

'''
from _21_2_myDB_String._2_CREATE_multiple_strs._3_dao import save_to_db
# Business logic
def get_len(str_val):
    print(str_val)
    words = {}
    for word in str_val.split(','):
        le = 0
        for char in word:
            le += 1
        words[word] = le
    save_to_db(words)
    return words
