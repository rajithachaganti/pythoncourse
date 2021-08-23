from numpy import *
arr1=array([1,2,3,4,5])
arr2=arr1
arr1[1]=6
print('aliasing')
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)
print('shallow copy')
arr2=arr1.view()
arr1[1]=7
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)
print('deep copy')
arr2=arr1.copy()
arr1[1]=8
print(id(arr1))
print(id(arr2))
print(arr1)
print(arr2)
