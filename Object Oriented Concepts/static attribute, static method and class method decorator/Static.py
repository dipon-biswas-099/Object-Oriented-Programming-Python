#static attribute (class attribute)
#static method @staticmethod
#class method @classmethod
class Shopping:
    cart = []#class attribute # static attribute. change kora jai emn sob kisu static 
    origin = 'china'

    def __init__(self,name,location) -> None:
        self.name = 'jamu na city '#intance attribute
        self.location = 'jam er maj khane'


    def purchease(self,item,price, amount):
        remaining = amount - price
        print(f'buying {item} for price {price} and remaining {remaining}')

    @staticmethod
    def multiply(a,b): # self deya lage na staticmethod use korle 
        result = a*b
        print(result)

    @classmethod
    def hudai_dekhi(self,item):
        print('kinbo just hudai dekhi ', item)



Shopping.purchease('a',2,3,4)

basundhara = Shopping('basundhara','gate')
basundhara.purchease('phone',35000,40000)
basundhara.hudai_dekhi('laptop')
Shopping.multiply(4,5)
