'''
Created on Mar 20, 2020

@author: madhu

https://www.tutorialspoint.com/postgresql/postgresql_python.htm
https://pynative.com/python-postgresql-tutorial/

'''
#Step1 : Get connection
#Step2 : Get cursor on db connection
#Step3: Prepare SQL Query
#Step3 : Execute sql query
#Step4: Commit the transaction

import psycopg2
#Step1 : Get connection
try:
    conn = psycopg2.connect(database="postgres",
                            user = "postgres",
                            password = "1234",
                            host = "localhost",
                            port = "5432")
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    query = """
            create table EMP(empno INT, 
                                ename TEXT, 
                                job TEXT,
                                mgr INT,
                                hiredate date,
                                sal INT,
                                comm INT,
                                deptno INT,
                                primary key(empno),  
                                foreign key(deptno) references dept(deptno))
            """
    #Step3 : Execute sql query 
    cursor.execute(query)
    print("Employee Table Created")
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()