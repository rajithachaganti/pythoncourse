'''
Create a union of sets
'''
colors1 = {'Red', 'Indigo', 'Orange', 'magenta', 'Yellow', 'Green'}
colors2 = {'Indigo', 'Pink', 'Maroon', 'Blue', 'Red', 'Green', 'Orange', 'White', 'Black'}
set_union = colors1 | colors2
print('union of both sets - ', set_union)
# Adds elements of colors1 to colors2
x = colors2.union(colors1)
print('Union of both sets in colors2 - ', colors2)
print('Union of both sets in colors2 - ', x)