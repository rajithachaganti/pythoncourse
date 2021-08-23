
from findlength.service import get_data
# Controller
def get_char_count(word):
    # Validate input data
    if len(word) == 0:
        return "Invalid string!"
    else:
        result = get_data(word)
        return result
