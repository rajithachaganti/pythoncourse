'''
Find the length of a set
'''
colors1 = {'Red', 'Indigo', 'Orange', 'Magenta', 'Yellow', 'Green'}
colors2 = {'Indigo', 'Pink', 'Maroon','Purple', 'Violet', 'Blue', 'Red', 'Green', 'Orange', 'White', 'Black'}
colors3 = {'Pink', 'Purple', 'Violet', 'Green', ''}
set1 = {45, 83, 64, 81, 73, 69, 39, 19, 71}
print('Length of set1 - ', len(set1))
print('Length of colors1 - ', len(colors1))
print('Length of colors2 - ', len(colors2))
print('Length of {} - ', len({}))
print('Length of union of colors1 and colors2 - ', len(colors2.union(colors1)))