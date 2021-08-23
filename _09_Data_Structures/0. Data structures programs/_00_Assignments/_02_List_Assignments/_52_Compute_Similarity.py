'''
Compute the similarity between two lists
'''
# MEthod - 1
from collections import Counter

flowrs = ['Rose', 'Lilly', 'Chrysanthemum', 'Jasmine', 'Lotus', 'Marigold']
colors = ['Rose', 'Lilly', 'Jasmine', 'Lotus', 'Daffodils', 'Water Lilly']

counter1 = Counter(flowrs)
counter2 = Counter(colors)

# print(counter1)
# print(counter2)

print('flowrs - colors  = ', list(counter1- counter2))
print('colors - flowrs  = ', list(counter2-counter1))
print()


# Method 2 using sets
def diff(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    diff_list1 = list(s2 - s1)
    diff_list2 = list(s1 - s2)
    print(f'l2 - l1 = {diff_list1}')
    print(f'l1 - l2 = {diff_list2}')


diff(flowrs,colors)