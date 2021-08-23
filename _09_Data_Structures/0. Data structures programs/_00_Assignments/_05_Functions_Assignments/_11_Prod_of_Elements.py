'''
multiply all the numbers in a list
'''
n = int(input('Enter the length of the list :'))
 
list_of_numbers = []
 
for i in range(0,n):
    ele = int(input('enter list element'))
    list_of_numbers.append(ele)


def prod_of_ele(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod


if __name__ == '__main__':
    print('Product of elements - ', prod_of_ele(list_of_numbers))