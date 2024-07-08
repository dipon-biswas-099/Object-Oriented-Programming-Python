class Shopping:
    def __init__(self,name):
       self.name = name
       self.cart=[]

    def add_to_cart(self,item,price,quality):
        product ={'item':item,'price':price , 'quality':quality}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quality']

        print('total price ',total)
        if amount < total:
            print(f'please give more money {total - amount} tk')

    def remove_item(self,item):
        for i in self.cart:
            if i['item']== item:
                self.cart.remove(i)
                print(f'the product {item} is removed')
            else:
                print(f'the product isn.t exist')
            break

person = Shopping('dipon')
person.add_to_cart('alu',50,2)
person.add_to_cart('egg',40,3)
person.add_to_cart('coke',2,4)
person.add_to_cart('rice',10,6)
print(person.cart)
person.checkout(800)
person.checkout(50)
person.remove_item('egg')
person.remove_item('alu')