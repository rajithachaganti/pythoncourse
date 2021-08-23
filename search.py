from array import *
arr=array('i',[])
n=int(input('enter length of array'))
for i in range(n):
    x=int(input('enter array values'))
    arr.append(x)
print(arr)
val=int(input('enter element to search'))
k=0
for e in arr:
    if e==val:
        print('found','element=',val)
        print('index=', k)
        break
    k+=1
else:
    print('not found')
print(arr.index(val))

