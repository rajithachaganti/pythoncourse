
from mydao import persist_sum

def find_sum(in_no):
    total = 0
    for num in in_no:
        total += int(num)
    res = persist_sum(in_no, total)
    if res:
        return total
    else:
        return "Exception occured"