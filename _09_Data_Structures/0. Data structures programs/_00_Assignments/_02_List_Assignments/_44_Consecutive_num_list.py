'''
Generate group of five consecutive numbers in a list
j holds nums from 1 to 5
and i holds 0 -4 and mutlipled by 5
'''

l = [[5*i + j for j in range(1,6)] for i in range(5)]
print(l)