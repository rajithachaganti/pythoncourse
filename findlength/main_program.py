
# REQ: Find char count in string


from findlength.controller import get_char_count
in_str = 'dffdf23434dfsddsf' #input("Enter string to find length: ")

if __name__ == '__main__':
    char_count = get_char_count(in_str)
    if type(char_count) == str:
        print(char_count)
    else:
        for char, count in char_count.items():
            print(char, count)