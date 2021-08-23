'''
Find missing and additional values
'''
lst1 = [23, 25, 27, 29, 31, 33, 35, 37]
lst2 = [22, 23, 24, 26, 28, 31, 33, 35, 37]

def missing_ele(l1, l2):
    missed_in_1 = list(set(l2) - set(l1))
    missed_in_2 = list(set(l1) - set(l2))
    print(f'Elements missed in first list = {missed_in_1}')
    print(f'Elements missed in Second list = {missed_in_2} ')


# Function call
missing_ele(lst1, lst2)