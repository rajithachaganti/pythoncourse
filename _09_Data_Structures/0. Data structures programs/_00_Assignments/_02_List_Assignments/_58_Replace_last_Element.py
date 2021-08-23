'''
Replace the last element in a list with another list
'''

colors = ['Rose', 'Lilly', 'Jasmine', 'Lotus', 'Daffodils', 'Water Lilly']
flowrs = ['Rose', 'Lilly', 'Chrysanthemum', 'Jasmine', 'Lotus', 'Marigold']


def replace_ele(l1, l2):
    l1[-1] = l2
    return l1

print(f'After Replacing - {replace_ele(flowrs, colors)}')