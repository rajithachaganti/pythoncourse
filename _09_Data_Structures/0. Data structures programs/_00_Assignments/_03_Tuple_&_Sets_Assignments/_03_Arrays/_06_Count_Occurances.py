'''
Get the number of occurrences of a specified element in an array
'''
import array as arr
arr1 = arr.array('i', [9, 9, 42, 95, 5, 72, 9, 95, 91])
print(arr1.count(95))


def ele_count(arr):
    count_dict = {}
    for i in arr:
        if i in count_dict.keys():
            pass
        else:
            count_dict[i] = arr.count(i)
    return count_dict


print('Element count in arr1 -', ele_count(arr1))