'''
Remove a specified item using the index from an array.
'''
import array as arr
arr_num = arr.array('i',[4, 8, 4, 9, 1, 6])
arr_num.remove(1)   # remove particular item
print('Removed specified item -', arr_num)
arr_num.pop(2)       # Remove from particular index
print('After removing element of index 2 -', arr_num)