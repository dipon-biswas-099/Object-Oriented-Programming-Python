class Vehicle:
    def __init__(self,name,price) -> None:
        self.name = name
        self.price = price

    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)


class Truck(Vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight = weight
        super().__init__(name, price)

class PickUp(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)

class ACbus(Bus):
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)
        
    def __repr__(self) -> str:
        return f'bus name : {self.name}, price : {self.price}, seat : {self.seat}, temperature : {self.temperature}'

greenline = ACbus('Green line',500000,52,'18 degree')
print(greenline)