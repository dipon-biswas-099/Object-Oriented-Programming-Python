#kargs means value with key 
def full_name(first,last):
    name = f'full name is : {first}{last}'
    return name
#take parameters in order(serial wise)
#name = full_name('Dipon','bIswas')
name = full_name(last='Biswas', first='Diponn')
print(name)

def famus_name(first,last,**addition):
    name = f'{first} {last}'
   # print(addition['title'])
    for key ,value in addition.items():
        print(key,value)
    return name
name = famus_name(first='alu',last='kodu',title="moris",addition="ad")
print(name)

# multiple return from a function
def a_lot(num1,num2):
    sum = num1+num2
    mul = num1*num2
    remain= num1-num2
    return sum,mul,remain

everything = a_lot(5,3)
print(everything) 
