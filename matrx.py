from numpy import *

r1=int(input('enter row size for m1'))
c1=int(input('enter col size for m1'))
r2=int(input('enter row size for m2'))
c2=int(input('enter col size for m2'))
if c1 != r2:
    print('matrix multiplication not possible')
else:
    a1=array([int(i) for i in input('enter elements for m1').split()])
    a2 = array([int(i) for i in input('enter elements for m2').split()])
    m1=matrix(a1.reshape(r1,c1))
    m2=matrix(a2.reshape(r2,c2))
    print(m1)
    print(m2)
    sum=0
    m3=matrix(zeros((r1*c2),int))
    print(m3)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                sum=sum+m1[i,k]*m2[k,j]
            m3[i,j]=sum
            sum=0
    print(m3)
print(m1*m2)







