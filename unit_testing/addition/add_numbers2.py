
class Addition:
    def __init__(self):
        print("----__init__ method---")
        pass

    def add(self, num1, num2):
        print("----add method-----")
        num1 += 1
        num2 += 1
        res = num1 + num2
        return res

'''
if __name__ == '__main__':
    obj = Addition()  # 1
    n1 = 10
    n2 = 20  # 2
    output = obj.add(n1, n2)  # 3
    print("Addition is : ", output)

# 1 - Object creation for class
# 2 - Prepare input data to call function
# 3 - Function call
# 4 - Execute program and validate the output
'''