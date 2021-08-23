str = "Rajitha"
n=len(str)

str1=str[-1]
str2=str[0]

print(str1,end='')
for i in range(1,n-1):
    print(str[i],end='')
print(str2)