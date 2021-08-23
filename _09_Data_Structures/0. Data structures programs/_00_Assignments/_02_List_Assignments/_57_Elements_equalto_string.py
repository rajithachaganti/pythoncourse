'''
check if all the items are equal to string
'''
li1 = ['sky', 'earth', 'moon', 'venus', 'mercury']
li2 = ['moon','moon','moon','moon','moon','moon',]
str1 = 'moon'


# Method 1
def ele_equals_str(li , s):
    for i in li:
        if i != s:
            return False
    return True


print(f'All items matched with string in li1 : {ele_equals_str(li1, str1)}')
print(f'All items matched with string in li2 : {ele_equals_str(li2, str1)}')
print()

# Method 2
def equal_check(li, s):
    return all(i== s for i in li)


print('Method 2')
print(f'All items matched with string in li1 : {equal_check(li1, str1)}')
print(f'All items matched with string in li2 : {equal_check(li2, str1)}')