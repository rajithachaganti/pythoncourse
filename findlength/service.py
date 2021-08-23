
from findlength.dao import save_data


def get_data(in_str):
    data = {}
    for char in in_str:
        if char not in data.keys():
            data[char] = 1
        else:
            data[char] += 1
    f_word = ''
    for char, count in data.items():
        f_word += char+"-"+str(count)+' * '
    save_data(f_word, len(data.keys()))
    return data

