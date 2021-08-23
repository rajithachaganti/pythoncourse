''''''

'''
50% of projects used to implement unit testing

Unit Testing : Should be done by developer
             : unit wise testing
For ex: Username,Password :
    Test Scenario :Testing the login functionality
        Test cases : 1. Correct username, Correct password 
                     2. Correct username,Wrong password 
                     3. Wrong username,Correct password 
                     4. Wrong username,Wrong password 
                     5. Don't give username,password
'''

def add(num1, num2):
    res = num1 + num2 + 1
    return res

# static code
if __name__ == '__main__':
    n1 = int(input("Enter number1 :"))
    n2 = int(input("Enter number2 :"))

    print("Result : ", add(n1, n2))
'''
Expected result : Result :  30
Actual   result : Result :  31

Test fails : There is something wrong in your logic.
             Fix that one 

'''


'''
100 methods
new func : 5 methods new 
          10 method modification

Regression Testing : 
'''
# excel file data read database save it
