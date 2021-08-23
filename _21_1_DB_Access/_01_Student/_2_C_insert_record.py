'''
Created on Mar 20, 2020

@author: madhu

import psycopg2

try:
    #Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user = "postgres", 
                            password = "1234",
                            host = "localhost", 
                            port = "5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Prepare sql query
    rec1 = "INSERT INTO STUDENT VALUES(101, 'MADHU', 'ABC')"
    rec2 = "insert into student values(102, 'Prakash', 'AREM')"
    rec3 = "insert into STUDENT values(103, 'Kiran', 'VN2')"
    # Step4 : Execute sql query
    cursor.execute(rec1)
    cursor.execute(rec2)
    res = cursor.execute(rec3)
    print("Insertion : ",res)
    #Step4: Commit the transaction
    conn.commit()
    print("Records inserted successfully")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()
'''


import psycopg2
try:
    connection = psycopg2.connect(host="localhost",
                                  database="postgres",
                                  user="postgres",
                                  password=1234,
                                  port=5432,
                                  )
    my_cursor = connection.cursor()
    records = [(1, 'rani', 'YGHS'), (5, 'ram', 'YGHS'), (6, 'radha', 'YGHS')]
    for each in records:
        my_cursor.execute("insert into student values(%s, %s, %s)", each)
        connection.commit()
except Exception as e:
    print('exception is', e)
finally:
    print("inserted successfully")
    my_cursor.close()
    connection.close()



