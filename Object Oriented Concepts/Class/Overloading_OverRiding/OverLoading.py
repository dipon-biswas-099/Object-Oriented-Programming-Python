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

    # + sign operation overload
    def __add__(self,other):
        return self.age + other.age

sakib = Cricketer('sakib','6.5',40,60,'BD')
mushi = Cricketer('mushi','6.5',50,50,'BD')

sakib.eat()
sakib.exercise()
print(sakib + mushi)

#plus sign overload

print(40+50)
print('sk'+'bk')
print([12,96]+[1,2,5,6])