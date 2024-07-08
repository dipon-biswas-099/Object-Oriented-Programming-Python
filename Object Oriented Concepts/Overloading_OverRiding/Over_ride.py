#parent class e je method ache same method jodi child class e thake taile seta override
class Person:#parent class
    def __init__(self,name,height,age,weight) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.weight  = weight

    def eat(self):
        print('vat mangop polau')
    def exercise(self): # jor kore overriding kora
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, height, age, weight,team) -> None:
        self.team = team
        super().__init__(name, height, age, weight)

    #override
    def eat(self):
        print('vegetable')

    def exercise(self):
        print('gym is need')


sakib = Cricketer('sakib','6.5',40,60,'BD')
sakib.eat()
sakib.exercise()