'''
function to check whether a string is a pangram or not
'''
import string

str1 = 'the quick brown fox jumps over the lazy dog'
str2 = 'The dark wolf growls'

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True


print('str1 is pangram - ', ispangram(str1))
print('str2 is pangram - ',ispangram(str2))