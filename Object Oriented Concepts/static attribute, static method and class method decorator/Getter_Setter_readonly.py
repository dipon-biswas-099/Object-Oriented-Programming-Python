#read only --> you can not set the value , value can not be changed 
#getter --> get a value of property through a method  . most of the time , you will get the value of a private attribute.
#setter --> set a value of property through a method. most of the time , you will set the value of a private property 

class User:
    def __init__(self,name, age, money ) -> None:
        self._name = name
        self._age = age
        self.__money= money

    #getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age

    @property #getter
    def salary(self):
        return self.__money

    @salary.setter  # salary is getter . 
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative '
        self.__money += value


samsu = User('samsu',21,1200)
#print(samsu.age)
#print(samsu.salary())
samsu.salary = 4500
print(samsu.salary)
samsu.salary = 100
print(samsu.salary)
