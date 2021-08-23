'''
Use of frozensets
Frozen Sets are similar to any other normal sets
but, the difference is that frozen sets are immutable
'''
# Operations like removing and adding elements cannot be performed with Frozen sets
colors1 = frozenset(('Red', 'Indigo', 'Orange', 'Magenta', 'Yellow', 'Green'))
colors2 = frozenset(('Pink', 'Purple', 'Violet'))
print('colors1 disjoint of colors2 -', colors1.isdisjoint(colors2))