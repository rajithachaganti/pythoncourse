'''
Created on Mar 20, 2020

@author: madhu
'''
from _21_1_DB_Access._03_EMP_Refactored.utilities import conn, emp_data_sel

try:
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM EMP")
    cursor.execute(emp_data_sel)
    print("\n-----Retrieving records from db table DEPT-------")
    records = cursor.fetchall()
    for each in records:
        print(each)
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("\nClosing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()