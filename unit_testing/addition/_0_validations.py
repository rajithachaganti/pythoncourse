'''
Client side validations : html,css,javascript 
Server side validations

clinet -- server
'''
'''
Unit Testing:
---------------
TDD : Test Driven Development 
    : coding/test cases
    
REQUIREMENT:
------------
1. First write the test case.Code will fail
2. Then as per test case,write the code
3. Again run the test case. Test case should pass


But in realtime:
--------------------
1. Implement code as per requirement
2. After testing in local system, then start writing the test cases

Local - DEV - TEST - UAT - PROD

'''

'''
UI --->   Python ---> Databse

STORY:
-------
- Find student grade based on given marks.

Client side - 1. input should be valid 
              2. input no. should be between 0 to 100
              
'''
def get_student_result(marks):
    # client side validations
    if type(s_marks) != int:
        return "Invalid input data"
    if marks < 0 or marks > 100:
        return "Please enter valid marks between 0 to 100"
    # Business logic
    if marks >= 90 and marks <= 100:
        return "DISTINCTION"
    elif marks >= 60 and marks < 90:
        return "First class"
    elif marks >= 50 and marks < 60:
        return "Second class"
    elif marks >= 35 and marks < 50:
        return "Third class"
    else:
        return "Fail"

s_marks = int(input("Enter marks: "))

print("Student result : ", get_student_result(s_marks))

'''
Test scenario : Get student result based on marks 
    Testcases : 1. When marks >= 90
                2.
                3.
                4.
                5.
                6.
    Negative testcases : 1. When marks > 100
                         2. When marks < 0 
                         3. Should be number 

'''