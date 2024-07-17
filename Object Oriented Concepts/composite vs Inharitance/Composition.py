class Engine:
    def __init__(self) -> None:
        pass

    def start(self): # Engine er start method
        return "engine started"
        

# cas "has a" engine => has a relation 

class Driver:
    def __init__(self) -> None:
        pass

class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self): #method 
        self.engine.start()
        