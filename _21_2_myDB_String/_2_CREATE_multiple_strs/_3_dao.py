


''''''

'''
DAO  Data Access Object: 
                1. Receive the data from service
                2. Get db connection,cursor etc.,
                3. Prepare and execute the sql query with data 
                4. Send response to Service
'''
from _21_2_myDB_String._2_CREATE_multiple_strs.utils import conn

def save_to_db(word_data):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO STRING_DATA VALUES(%s,%s)"
        print(word_data)
        for word,le in word_data.items():
            cursor.execute(query,(word,le))
        conn.commit()
    except Exception as e:
        print("Exception details : ",e)
    finally:
        cursor.close()
        conn.close()
