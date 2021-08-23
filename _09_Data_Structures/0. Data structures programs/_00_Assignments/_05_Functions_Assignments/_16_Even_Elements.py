'''
print the even numbers from a given list
'''
li1 = [46, 83, 82, 93, 62, 75, 53, 97,43]
li2 = [74, 94, 73, 49, 42, 96, 42, 97, 52.9, 6.42]

def even(l):
    even_lis = []
    for i in l:
        if i % 2 == 0:
            even_lis.append(i)
    return even_lis


def even1(l):
    el = [i for i in l if i % 2 == 0]
    return el


print('Even Elements with fun2 for li1 - ', even1(li1))
print('Even Elements with fun1 for li1- ', even(li1))
print('Even Elements with fun2 for li2- ', even1(li2))
print('Even Elements with fun1 for li2- ', even(li2))