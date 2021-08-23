'''
Convert a pair of values into a sorted unique list
'''
lst1 = [(13, 2), (3, 34), (14, 23), (85, 62), (37, 8), (81, 2), (63, 24), (23, 84)]


def unique_lst(l1):
    s1 = set(set().union(*l1))
    s_sorted = sorted(s1)
    return s_sorted


print(f'Sorted single list - {unique_lst(lst1)}')