'''
Remove the first occurrence of a specified element from an array.
'''
import array as arr
arr_num = arr.array('i',[4, 8, 4, 9, 1,3, 5, 1, 6])
arr_num.remove(1)   # remove particular item
print('Removed specified item -', arr_num)
# remove() by default remove first occurance in array