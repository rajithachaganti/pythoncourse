str = "Rani pani kani poni"
n=len(str)

#length of string
n=len(str)
print(n)
c=0
for i in str:
    c+=1
print(c)

#count characters in string
c=0
d=0
for i in str:
    if i.isalpha():
        c+=1
    elif i.isdigit():
        d+=1

print(c,d)

#string slicing
a=str[0:]
b=str[::-1]
print(b)

#swap first and last char in the string
str1=str[n-1]
str2=str[0]
str1,str2 = str2,str1
print(str1,end='')
for i in range(1,n-1):
    print(str[i],end='')
print(str2)

#removing odd indexes
str1=str[0:n:2]
print(str1)

#count words in str
c=str.count('ni')
print(c)

#upper lower of str
str1=str.upper()
str2=str.lower()
print(str1,str2)



