'''
Create a shallow copy of sets.
Read deep copy and shallow copy
////////
shallow copy not implemented correctly
'''
import copy

colors1 = {'Indigo', 'Pink', 'Maroon', 'Purple', 'Violet', 'Blue', 'Red', 'Green', 'Orange', 'White', 'Black'}
# colors2 = copy.copy(colors1)
colors2 = colors1.copy()
print(colors2)
colors2.remove('Maroon')
print(colors2)
print(colors1)