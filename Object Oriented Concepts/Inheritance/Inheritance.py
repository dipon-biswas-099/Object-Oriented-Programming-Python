# Base class , parent class, common attribute + functionality class
# derived class, child class , uncommon attribute + functionality 

class Device:
    def __init__(self,brand , price, color) -> None:
         self.brand = brand
         self.price = price
         self.color = color

    def run(self):
        return f'Running laptop : {self.brand}'


class Laptop:
    def __init__(self, memory ) -> None:
        self.memory = memory


    def coding(self):
        return f'learnign python and practicing'
    
class Phone:
    def __init__(self,dual_sim) -> None:
        self.dual_sim = dual_sim

       
        def call(self,number,text):
            return 'sending sms to : {number} with : {text}'
        

class Camera:
    def __init__(self,pixel) -> None:
        self.pixel = pixel


    def run(self):
        pass

    def change_lens(self):
        pass

    