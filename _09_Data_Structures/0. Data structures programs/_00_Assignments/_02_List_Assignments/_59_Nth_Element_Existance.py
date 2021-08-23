'''
Check if the n-th element exists in a given list
'''

colors = ['Red', 'Orange', 'Indigo', 'Pink', 'White', 'Grey']
flowrs = ['Rose', 'Lilly', 'Chrysanthemum', 'Jasmine', 'Lotus', 'Marigold']


def nth_existance(l1, n):
    if len(l1) < n:
        return False
    else:
        return True


print(f'5th element exists in colors - {nth_existance(colors, 5)}')
print(f'7th element exists in colors - {nth_existance(flowrs, 7)}')

Find a tuple, the smallest second index value from a list of tuples