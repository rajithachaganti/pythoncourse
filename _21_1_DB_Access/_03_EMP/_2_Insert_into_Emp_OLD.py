'''
Created on Mar 20, 2020

@author: madhu
emp_records = []
    with open('emp_data.txt') as e_data:
        data = e_data.read().split('\n')
        for each in data:
            emp_records.append(each.split(', '))
    print(emp_records)
    for each in emp_records:
        print(each)
        empno = int(each[0])
        ename = each[1]
        job = each[2]
        if each[3] == 'null':
            mgr = None
        else:
            mgr = each[3]
        hiredate = None
        sal = int(each[5])
        if each[6] =='null':
            comm = None
        else:
            comm = int(each[6])
        deptno = int(each[7])
        li = []
        li.extend([empno,ename,job,mgr,hiredate,sal,comm,deptno])
        print(li)
        query = 'INSERT INTO EMP VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(query,tuple(li))
        # 'INSERT INTO EMP_30 VALUES('7839', 'KING', 'PRESIDENT', 'null',
        #            "'17-11-1981,dd-mm-yyyy'", '5000', 'null', '10')
    print("----Records inserted into DEPT successfully-----")
'''
import ast
import datetime

import psycopg2
from distutils.dist import command_re
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
    #Step3 : Retrieve emp data

    emp_details = []
    with open('emp_data.txt') as emp_record:
        data = emp_record.read().split('\n')
        print('data=',data)
        for each in data:
            emp_details.append(each.split(', '))
        print('emp_details=',emp_details)
        for each in emp_details:
            print('each=',each)
            empno = int(each[0])
            ename = each[1]
            job = each[2]
            if each[3] == 'null':
                mgr = None
            else:
                mgr = int(each[3])
            hiredate = each[4]
            print('date=',hiredate)
            sal = int(each[5])
            if each[6] == 'null':
                comm = None
            else:
                comm = int(each[6])
            deptno = int(each[7])
            li = []
            li.extend([empno, ename, job, mgr, hiredate, sal, comm, deptno])
            print('li=',li)
            query = "INSERT INTO EMP VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(query, tuple(li))
    #query = "INSERT INTO EMP VALUES(7934,'MILLER','CLERK',7782,to_date('19-05-2021','dd-mm-yyyy'),1300,10)"
    #cursor.execute(query)
    print("----Records inserted into emp successfully-----")

    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()