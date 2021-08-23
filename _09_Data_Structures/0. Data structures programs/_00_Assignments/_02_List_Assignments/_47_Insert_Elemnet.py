'''
Insert an element before each element of a list
'''

lst2 = [22, 23, 24, 26, 28, 31, 33, 35, 37]
ele = 'a'


# def insert_ele(l1, element):
#     length = len(l1)
#     for i in range(0, length):
#         length += 1
#         i += 1
#         l1.insert(i, element)
#     return l1
#
# print(f'After inserting - {insert_ele(lst2, ele)}')

def insert_into(l1, element):
    # l1 = [i for i in l1 for i in (c, elt)]
    l1 = [i for elt in l1 for i in (element, elt)]
    return l1

print(f'After inserting - {insert_into(lst2, ele)}')