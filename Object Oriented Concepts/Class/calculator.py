class Calculator:
    bran = 'casio'
    def add(self,num1,num2):
        addition = num1+num2
        return addition 
    
    def dituct(self, num1, num2):
        dit = num1-num2
        return dit
    
my_cal = Calculator()
result = my_cal.add(4,5)
result2 = my_cal.dituct(40,5)
print(result,result2)
         

