class Family:
    def __init__(self,adress) -> None:
        self.adress = adress

    
class School:
    def __init__(self,id,level) -> None:
        self.level = level
        self.id = id

class Sports:
    def __init__(self,game) -> None:
        self.game = game


class Student(Family,School,Sports):
    def __init__(self, adress,id,level,game) -> None:
        School.__init__(self,id,self.level)
        Sports.__init__(self,game)
        Family.__init__(self,adress)
        super().__init__(  adress)
        super().__init__(id,level)