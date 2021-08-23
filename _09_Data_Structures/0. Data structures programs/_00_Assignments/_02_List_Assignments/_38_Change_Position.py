'''
Change the position of every nth value with (n+1)th value
'''

l1 = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]

def swap_ele(lst, n):
    for i in range(1, len(lst)+1):
        if i % n ==0:
            temp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = temp
    return lst

print('list after changing positions - ',swap_ele(l1, 3))