'''
Convert an array to an array of machine values and return the bytes representation
'''
import array as arr
print("Bytes to String: ")
x = arr.array('b', [119, 118, 78, 81, 97, 101, 99, 111, 98, 81])
s = x.tobytes()
print(s)
