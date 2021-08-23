'''
Converting multiple integers into single integer
'''
l1 = [12, 14, 16, 20, 18]


# Method1
def single_num(lst):
    sing_no1 = ''
    for i in lst:
        sing_no1 += str(i)
    return sing_no1


print('After converting to Single Integer ', int(single_num(l1)))

def single_map(lst):
    single_no2 = ''.join(map(str, lst))
    return single_no2

print('After converting to Single Integer using map method - ',int(single_map(l1)))


