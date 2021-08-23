'''
Print all unique values in a dictionary.
'''

count_of_color_shades = [{'red': 7}, {'yellow':4},{'green': 8}, {'blue' :7}, {'orange' :2}, {'indigo' : 9}]

res = list(set(val for dic in count_of_color_shades for val in dic.values()))

print("The unique values in list are : " + str(res))