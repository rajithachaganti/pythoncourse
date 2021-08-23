'''
Concatenate elements of a list
'''
flowrs = ['Rose', 'Lilly', 'Chrysanthemum', 'Jasmine', 'Lotus', 'Marigold']
colors = ['Rose', 'Lilly', 'Jasmine', 'Lotus', 'Daffodils', 'Water Lilly']


def join_lists(l1):
    joined = '-'.join(l1)
    return joined

print(f'After concat - {join_lists(flowrs)}')
print(f'After concat - {join_lists(colors)}')