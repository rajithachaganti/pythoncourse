class Myexception(Exception):
    def __init__(self,str):
        self.str=str
def bank(lst):
    for k,v in lst.items():

        if v<=2000:
            raise Myexception('amt is less for %s'%k)
            break
        print('%.15s %.2f'%(k,v))
lst={'raj':3450.00,'rani':1999.00,'ram':3000.00}
try:
    bank(lst)
except Myexception as me:
    print(me)
