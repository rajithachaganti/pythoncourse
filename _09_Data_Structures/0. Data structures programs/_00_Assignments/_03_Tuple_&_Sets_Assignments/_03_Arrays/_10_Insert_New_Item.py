'''
Insert a new item before the second element in an existing array.
'''
import array as arr
arr1 = arr.array('i', [64, 8, 5, 7, 3])
print('Before inserting - ', arr1)
arr1.insert(3, 2)
print('After inserting - ', arr1)