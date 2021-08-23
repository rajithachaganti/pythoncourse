from _21_2_DB_String._2_CREATE_mul_strs.utils import conn
try:
    cursor = conn.cursor()
    cursor.execute("create table USER_DATA(Uid varchar(100),data text,length integer)")
    conn.commit()
    print("table successfuly created")
except Exception as e:
    print(e)
finally:
    print("closing connections")
    cursor.close()
    conn.close()

