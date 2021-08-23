#person class
class Person:
    #class variable or static variable
    sal1=0
    sal=40000
    #parameterized constuctor method
    def __init__(self,nm,age,ht,wt):
        self.name=nm
        self.age=age
        self.height=ht
        self.weight=wt
        Person.sal1+=1
    @classmethod
    def sal_inc(cls):
        cls.sal+=10000

    @staticmethod
    def display1():
        print('count=',Person.sal1)

    # instance method
    def display(self):
        print('name={}\nage={}\nheight={}\nweight={}'.format(self.name, self.age, self.height, self.weight))
p=Person('raji',23,5.1,58)
p1=Person('raji',23,5.1,58)
p.display()
print(p.sal,p1.sal)
p1.sal_inc()
print(p.sal,p1.sal)
p.sal+=5000
print(p.sal,p1.sal)
p1.display1()

