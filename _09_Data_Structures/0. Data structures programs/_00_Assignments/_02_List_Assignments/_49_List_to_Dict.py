'''
Convert list to list of dictionaries
'''
flowrs = ['Rose', 'Lilly', 'Chrysanthemum', 'Jasmin', 'Lotus', 'Marigold']
colors = ['Red', 'White', 'Mixed', 'White', 'Pink', 'yellow']


def list_of_dicts(f, c):
    list_of_dict = [{'color': i, 'flower' : j } for i,j in zip(c, f)]
    return list_of_dict


if __name__ == '__main__':
    print(list_of_dicts(flowrs, colors))