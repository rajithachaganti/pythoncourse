from _21_2_myDB_String._1_CREATE_single_strs.utils import conn
try:
    cursor = conn.cursor()
    query = "create table STRING_DATA(str_name text, str_len int)"
    cursor.execute(query)
    conn.commit()
except Exception as e:
    print('exception=',e)
finally:
    cursor.close()
    conn.close
