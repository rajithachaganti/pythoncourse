list1 = [1,2,3,5]
list2 = [1,2,4,5]
union = set(list1).union(list2)
print('union=',union)
for ele in union:
    if ele in list1 and ele in list2:
        print('yes',ele)
    elif ele not in list1 or ele not in list2:
        print('no', ele)





name = r"to_date('20-05-2021','dd-mm-yyyy')"
print(name)

a = 'hello world'
print(a.upper().replace('H','J'))
print('JELLOW\rWorld')