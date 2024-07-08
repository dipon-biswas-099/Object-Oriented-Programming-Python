#base class or parent class
class BasedClass:
    def __init__(self) -> None:
        pass

# derived class or childClass

class ChildClass(BasedClass):
    def __init__(self) -> None:
        super().__init__()

#simple inheritance : parent class --> child class (devoce ---> phone) (device --> laptop)

# Multi-level inheritance : grand ---> parent ----> child (vehicle --> bus ---> ACBus)
#multiple inharitance : Student(Family, School, Game)
#Hybrid: granda --> Father ,uncle , uncty ---> Child(Father, Uncle)


