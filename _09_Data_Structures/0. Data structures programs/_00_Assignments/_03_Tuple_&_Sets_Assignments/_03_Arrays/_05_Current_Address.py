'''
Get the current memory address and the length in elements of the buffer
used to hold an arrays? contents and also find the size

buffer_info() returns array of memory address and no of elements
'''
import array as arr
arr1 = arr.array('d', [65, 83, 42, 94, 63, 96])
arr2 = arr.array('d', [54, 82, 52, 85, 93, 53, 98])
print('arr1 - ')
print('Current memory address of arr1 - ', arr1.buffer_info()[0])
print('Elements length in Buffer - ', arr1.buffer_info()[1])
print('Size of element in arr1 -',arr1.itemsize)
print('Size of memory buffer - ', arr1.buffer_info()[1]* arr1.itemsize)
print('\n')
print('arr2 - ')
print('Current memory address of arr2 - ',arr2.buffer_info()[0])
print('Elements length in Buffer - ', arr2.buffer_info()[1])
print('Size of element in arr2 - ', arr2.itemsize)
print('Size of memory buffer - ', arr2.buffer_info()[1] * arr2.itemsize)