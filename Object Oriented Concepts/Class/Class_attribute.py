class Shop:
    cart=[] # class attribute
    def __init__(self, buyer):
        self.buyer = buyer

    def add_cart(self,item):
        self.cart.append(item)


dipon = Shop('dipon')
dipon.add_cart('shoes')
dipon.add_cart('phone')
print(dipon.cart)

mahdi = Shop('mahdi')
mahdi.add_cart('phone')
print(mahdi.cart)
