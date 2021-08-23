'''
Set Difference
'''
colors1 = {'Red', 'Indigo', 'Orange', 'magenta', 'Yellow', 'Green'}
colors2 = {'Indigo', 'Pink', 'Maroon', 'Blue', 'Red', 'Green', 'Orange', 'White', 'Black'}
set_diff1 = colors2 & colors1
print('set Difference - ', set_diff1)
# Using -
# - returns elements in colors2 that are not in colors1
set_diff2 = colors2 - colors1
print('colors2 - colors1 =', set_diff2)
set_diff3 = colors1 - colors2
print('colors1 - colors2 =',set_diff3)