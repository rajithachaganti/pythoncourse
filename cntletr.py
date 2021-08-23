from numpy import *
lst=[i for i in input('enter names').split(',')]
print(lst)
n=len(lst)
print(n)
m=0
def count_ltrs(lst):
    for word in lst:
        c=0
        for i in word:
            c+=1
            if c>5:
                globals()['m']+=1
                print(word, m)
                break

    print('total words with more than 5 letters=',m)
count_ltrs(lst)



