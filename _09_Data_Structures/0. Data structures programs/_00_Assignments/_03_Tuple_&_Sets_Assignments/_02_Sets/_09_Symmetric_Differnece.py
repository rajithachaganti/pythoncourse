'''
Create a symmetric difference. 
'''
# Symmetric difference returns elements are that are in set1 and set2 but not the elements in both the sets
colors1 = {'Red', 'Indigo', 'Orange', 'magenta', 'Yellow', 'Green'}
colors2 = {'Indigo', 'Pink', 'Maroon', 'Blue', 'Red', 'Green', 'Orange', 'White', 'Black'}
sym_diff = colors1 ^ colors2
print('Symmetric Difference of both the sets - ', sym_diff)