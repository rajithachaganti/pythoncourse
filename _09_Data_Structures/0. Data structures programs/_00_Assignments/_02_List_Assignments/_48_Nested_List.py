'''
Print a nested lists (each list on a new line) using the print() function
'''

lst2 = [22, 23, 24, 26, 28, 31, 33, 35, 37]


def nested(l1):
    l2 = ('\n'.join([str(lst) for lst in l1]))
    return l2


print(nested(lst2))
