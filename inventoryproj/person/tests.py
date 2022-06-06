class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def __str__(self):
        return f'{self.name,self.age}'


    def __repr__(self):
        return 'hello word'


s=Student('pandit',32)
print(s)
print(s.__repr__())