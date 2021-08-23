def fib(n):
    a=0
    b=1
    if n<=0:
        print('enter no. greater than 0')
    elif n==1:
        print(a)
    else:
        print('first {} numbers in fibonocci series'.format(n))
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
n=int(input('enter no.'))
fib(n)

def fib1(n):
    a=0
    b=1
    if n<=0:
        print('enter no. greater than 0')
    elif n==1:
        print(a)
    else:
        print('fibonocci series less than {}'.format(n))
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c>=n:
                break
            print(c)
fib1(n)