'''
Combine two dictionary adding values for common keys.
'''
d1 = {'a': 12, 'b': 25, 'c': 9}
d2 = {'d': 10, 'c': 20, 'a': 30}


def combine_dict(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict2[key] = dict2[key] + dict1[key]
        else:
            pass
    return dict2


print(combine_dict(d1, d2))