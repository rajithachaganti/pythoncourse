# list is mutable , tuple is immutable

list1 = [1, 2, 3, 4, 5, 6]

# append(): It appends element at end of the list  (any value)
print("Before append : ",list1)
list1.append(10)
print("After append  : ",list1)
list1.append(10.4)
list1.append(True)
list1.append('Hello')
list1.append([1,2,3])
list1.append((10,20,30))
list1.append({1:1})
list1.append({100,200,300})
print("After append  :",list1)


# extend  # only sequence str,list,tuple
list1 = [1,2,3,4,5,6]
print("Before extend : ",list1)
list1.extend([10, 20, 30])
print("After extend  : ",list1)
list1.extend('Hello World')
list1.extend((1,2,3))
print("After extend  : ",list1)


# append vs extend

list1 = [1,2,3]
list1.append([10,20])
list1.extend([100,200])
print("List after append,extend : ",list1)

# pop remove
list1 = [23, 12, 46, 34, 14, 7, 2, 19, 25]
print("Before pop   : ",list1)
list1.pop(3)  # index
print("After  pop   : ",list1)
list1.pop()
print("After  pop   : ",list1)

list1 = [23, 12, 46, 34, 14, 7, 2, 19, 25]
print("Before removal : ",list1)
list1.remove(14)
print("After removal  : ",list1)

list1 = [23, 14, 12, 46, 34, 14, 7, 2, 14, 19, 25]
print("Before removal : ",list1)
#list1.remove(14)
list1.pop(5)
print("After removal  : ",list1)

# insert
list1 = [1, 2, 3, 4, 5]
print("Before index : ",list1)
list1[0] = 150
print("After index   : ",list1)
list1.insert(0,100)
print("After insert  : ",list1)
list1.insert(5,100)
print("After insert   : ",list1)

# count
list1 = [1,1,3,2,3,2,4,5,3,2,1]
print("List count : ",list1.count(1))
# index
list1 = [23,76,23,34,25,21,43,16,25,7,53,13,59]
print("List index : ",list1.index(53))

list1.sort()
print("List sort : ",list1)
list1.sort(reverse=True)
print("List sort : ",list1)

list1 = [23,76,23,23,34,25,21,43,16,25,25,7,53,13,59]
print("List before reverse : ",list1)
list1.reverse()
print("List after reverse : ",list1)






