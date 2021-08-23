'''
Issubset and issuperset. 
'''
colors1 = {'Red', 'Indigo', 'Orange', 'Magenta', 'Yellow', 'Green'}
colors2 = {'Indigo', 'Pink', 'Maroon','Purple', 'Violet', 'Blue', 'Red', 'Green', 'Orange', 'White', 'Black'}
colors3 = {'Pink', 'Purple', 'Violet', 'Green', ''}
print('Checking for subsets')
print('colors1 issubset of colors2 -', colors1 <= colors2)
print('colors3 issubset of colors2 - ', colors3 <= colors2)
print('{"Green"} issubset of colors3 - ',{'Green'} <= colors3)
print('Checking for supersets')
print('colors2 issuperset of colors1 -',colors2 <=colors1)
print('colors2 issuperset of colors3-',colors2 <=colors3)
print("colors2 issuperset of {'Purple'}-",colors2 <= {'Purple'})
print('colors1 issuperset of empty set-',colors1 <= {})

