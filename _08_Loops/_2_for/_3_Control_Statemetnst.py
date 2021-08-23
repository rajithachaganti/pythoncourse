#15 decisions

# break continue pass

# Will use control statements in  while for loops
'''
# print numbers from 1 to 100. Stop iteration after getting first  7 even values
1. Get all numbers from 1 to 100
2. Filter only even numbers
3. Get only first 7 even numbers

1    2  3  4  5  6  7  8  9 10
11  12 13 14 15 16 17 18 19 20
21  22 23 24 25 26 27 28 29 30

first 3 even numbers
   solution               roguht work                count
  | 2 4 6                    | 1%2 == 0 2%2 == 0     3
                              3%2 == 0 4%2 == 0
                              5%2 == 0 6%2 == 0  Stops here
                              7%2 == 0  8%2 == 0  XXX



'''
'''
Problem with below solutions is,even after getting our results
loop is still iterating till last element 
'''
num = 1
count = 1
while num <= 100:
    if count <= 7  and num % 2 == 0:
        print(num)
        count += 1
    num += 1
    print("Iterating")


# Print first 7 even numbers between 1 to 100

'''
From 1 to 100
1.  Print numbers  
2.  Print even numbers
3.  Get only first 7 even nos
4.  Break the loop 
'''
print("----Print only first 7 numbers-------")
num = 1
counter = 0
while num <= 100:
    if counter > 7:
        break
    if num % 2 == 0:
        print(num)
        counter += 1
    num += 1
print("Exited while loop")

