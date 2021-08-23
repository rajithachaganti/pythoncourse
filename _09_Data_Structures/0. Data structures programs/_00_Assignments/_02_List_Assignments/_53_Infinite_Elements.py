'''
Create a list with infinite elements
'''
import itertools
c = itertools.count()
print(f' type - {type(c)}')
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# print(len(c))