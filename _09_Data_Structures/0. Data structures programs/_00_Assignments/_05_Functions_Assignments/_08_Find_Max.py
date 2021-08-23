'''
find the Max of three numbers
'''

n1 = int(input('Enter n1 : '))
n2 = int(input('Enter n2 : '))
n3 = int(input('Enter n3 : '))


def max_of_three(num1, num2, num3):
    return max( num1, max(num2, num3 ) )

if __name__ == '__main__':
    print(f'Max num : {max_of_three(n1, n2, n3)}')