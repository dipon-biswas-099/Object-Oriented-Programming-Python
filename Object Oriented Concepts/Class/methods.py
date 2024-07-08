def call():
    print('calling someone I dont know')
    return 'call done'

class phone:
    price = 12000
    color = 'blue'
    brand ='samsung'
    feature =['camera','apeaker','hammer']
    
    def call(self):  #call is a method 
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'sending sms to {phone} and massage:{sms}'
        return text
        

my_phone = phone()
print(my_phone.feature)
my_phone.call()
result = my_phone.send_sms(4111,'i forget you')
#print(my_phone.send_sms(4111,'i forget you'))
print(result)
