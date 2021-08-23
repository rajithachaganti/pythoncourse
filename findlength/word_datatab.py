from findlength.utils import conn
try:
    cursor = conn.cursor()
    query = "create table WORD_DATA(str_name text, str_len int)"
    cursor.execute(query)
    conn.commit()
    print("table created successfully")
except Exception as e:
    print('exception=',e)
finally:
    cursor.close()
    conn.close