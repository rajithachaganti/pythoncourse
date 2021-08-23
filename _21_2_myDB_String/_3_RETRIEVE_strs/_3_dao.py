


''''''

'''
DAO  Data Access Object: 
                1. Receive the data from service
                2. Get db connection,cursor etc.,
                3. Prepare and execute the sql query with data 
                4. Send response to Service
'''
from _21_2_myDB_String._3_RETRIEVE_strs.utils import conn

def ret_strs_db():
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM  STRING_DATA"
        cursor.execute(query)
        data = cursor.fetchall() # list of tuples
        # print('data=',data)
        return data
    except Exception as e:
        print("Exception details : ",e)
    finally:
        cursor.close()
        conn.close()
