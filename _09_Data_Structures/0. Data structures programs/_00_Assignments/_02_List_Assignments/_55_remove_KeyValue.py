'''
Remove key values pairs from a list of dictionaries
'''
list1 = [{"id" : 1, "data" : "Happy"}, {"id" : 2, "data" : "Beautiful"}, {"id" : 3, "data" : "Sky"}]


def rem_key_val(l1):
    for i in range(len(l1)):
        if l1[i]['id'] == 2:
            del l1[i]
            break
    return l1


# printing result
print("List after deletion of dictionary : ", rem_key_val(list1))