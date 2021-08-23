'''
 sum all the numbers in a list
 '''
n = int(input('Enter the length of the list :'))
list_of_numbers = []
 
for i in range(0,n):
    ele = int(input('enter list element'))
    list_of_numbers.append(ele)


def sum_of_ele(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


if __name__ == '__main__':
    print('Sum of elements - ', sum_of_ele(list_of_numbers))