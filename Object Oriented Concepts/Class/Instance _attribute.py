class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute

    def add_cart(self,item):
        self.cart.append(item)

dipon = Shop('dipon')
dipon.add_cart('phone')
dipon.add_cart('bag')
print(dipon.cart)

mahdi = Shop('mdi')
mahdi.add_cart('maiya')
mahdi.add_cart('koci')
print(mahdi.cart)