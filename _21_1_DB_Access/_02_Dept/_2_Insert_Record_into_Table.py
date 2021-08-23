'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
#Step1 : Get connection
try:
    conn = psycopg2.connect(database="postgres", 
                            user = "postgres", 
                            password = "1234",
                            host = "localhost", 
                            port = "5432")
    print("Conn type  :",type(conn))
    print("Connection :",conn)
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Insert records to DEPT Table
    records = [(30, 'ACCOUNTING', 'NEWYORK'), (40, 'RESEARCH', 'DALLAS')]
    cursor.executemany("insert into DEPT values(%s, %s, %s)", records)
    print("----Records inserted into DEPT successfully-----")
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()

'''
list1 = [1,2,3] # CREATE
print(list1)  # RETRIEVE
list1.append(100) # UPDATE
del list1[3]  # DELETE
'''
