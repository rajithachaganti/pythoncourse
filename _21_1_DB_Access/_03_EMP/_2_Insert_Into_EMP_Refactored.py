'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
#Step1 : Get connection
def _getdata_from_textfile():
    emp_records = []
    with open("emp_data.txt", 'r') as emp_details:
        data = emp_details.read().split('\n')
        print('data is:', data)
    for each in data:
        emp_records.append(each.split(', '))
        li1 = []
    for each in emp_records:
        print('each=', each)
        empno = int(each[0])
        ename = each[1]
        job = each[2]
        if each[3] == 'null':
            mgr = None
        else:
            mgr = int(each[3])
        hiredate = each[4]
        sal = int(each[5])
        if each[6] == 'null':
            comm = None
        else:
            comm = int(each[6])
        deptno = int(each[7])
        li = []
        li.extend((empno, ename, job, mgr, hiredate, sal, comm, deptno))
        print('li=', li)
        li1.append(tuple(li))
    return li1


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
    records = _getdata_from_textfile() # list of tuples
    print('records=',records)
    query = "insert into emp values(%s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(query,records)

    #Step4: Commit the transaction
    conn.commit()
    print("----Records inserted into EMPLOYEE successfully-----")
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()