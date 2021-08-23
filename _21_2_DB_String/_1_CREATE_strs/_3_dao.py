


''''''

'''
DAO  Data Access Object: 
                1. Receive the data from service
                2. Get db connection,cursor etc.,
                3. Prepare and execute the sql query with data 
                4. Send response to Service
'''
from _21_2_DB_String._1_CREATE_strs.utils import conn

def save_to_db(i_str, le):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO STRING_DATA VALUES(%s,%s)"
        cursor.execute(query,(i_str,le))
        conn.commit()
    except Exception as e:
        print("Exception details : ",e)
    finally:
        cursor.close()
        conn.close()
