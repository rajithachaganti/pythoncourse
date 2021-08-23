'''
Convert an array to an ordinary list with the same items.
'''
import array as arr
arr_num = arr.array('i', [4, 8, 4, 9, 1,3, 5, 1, 6])
# method 1
list_num1 = arr_num.tolist()
print('list_num1 - using tolist() - ', list_num1)

# Appending one by one to list
list_num2 = []
for i in arr_num:
    list_num2.append(i)
print('list-num2 - appending one by one - ', list_num2)

# Using list() constructor
list_num3 = list(arr_num)
print('list_num3 -  using list constructor - ',list_num3)