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
    
class Phone(Device):#inherit relation 
    def __init__(self,brand,price ,color,dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand,price,color)


       
    def call(self,number,text):
        return 'sending sms to : {number} with : {text}'

    def __repr__(self) -> str:
        return f'phone :{self.brand},{self.price} {self.color} ,{self.dual_sim}'
        


class Camera:
    def __init__(self,pixel) -> None:
        self.pixel = pixel


    def run(self):
        pass

    def change_lens(self):
        pass


#inheritance
my_phone = Phone('samsung',50000,'black',True)
print(my_phone)