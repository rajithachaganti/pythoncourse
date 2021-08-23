'''
Select Odd items in the list
'''

lst2 = [22, 23, 24, 26, 28, 31, 33, 35, 37]


def odd_ele(l):
    odd_list = []
    for i in l:
        if i%2 == 1:
            odd_list.append(i)
    return odd_list

print(f'Odd elements - {odd_ele(lst2)}')