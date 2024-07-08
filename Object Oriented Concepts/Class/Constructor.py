class Phone:
    manufactured = ' chaina'
    
    #constructor 
    def __init__(self,woner,brand,price):
        self.woner = woner
        self.brand = brand
        self.price = price
    
    def send_sms(self, phone, sms):
        text = f'sending to :{phone} {sms}'
        print(text)

my_phone = Phone('kala can','oppo','9800')
print(my_phone.brand,my_phone.woner)


her_phone = Phone('she','iphone',110000)
print(her_phone.brand,her_phone.price)