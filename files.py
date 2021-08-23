with open('example.txt', 'w+b') as f:
    str=input('enter string')
    #f.write(str)
    f.write(str.encode())
    n=f.tell()
    print(n)
    f.seek(-6,1)
    n1=f.tell()
    print(n1)
    d=f.read()
    #print(d)
    print(d.decode())


