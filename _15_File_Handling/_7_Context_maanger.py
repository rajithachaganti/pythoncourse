# https://www.geeksforgeeks.org/context-manager-in-python/
# Python program creating a
# context manager

class ContextManager:

    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')

print("---Before with-----")

with ContextManager() as f_ojb:
    print('with line 1')
    print('with line 2')
    print('with line 3')

print("---After with-----")

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    # loading a file


with FileManager('test.txt', 'w') as f_obj:
    f_obj.write('Test')

print("Is file closed ? ",f_obj.closed)