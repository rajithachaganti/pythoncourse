'''
Split a list every Nth element
'''
lst2 = [22, 23, 24, 26, 28, 45, 28, 62, 95, 43, 31, 33, 35, 37]


def list_slice(S, step):
    lst_sliced = [S[i::step] for i in range(step)]
    return lst_sliced


print(list_slice(lst2,4))


