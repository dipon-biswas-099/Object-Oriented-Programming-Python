class Bank:
    def __init__(self,name , holder_name,initial_deposit) -> None:
        self.name = name # public attribute
        self._branch = 'banani 11' # protected attribute
        self.holder_name = holder_name 
        self.__balance = initial_deposit # private attribute # __balence is the syntax of  'private' balence , it can accesible under anywhere of the class but not outside of the class

    def deposit(self , amount):
        self.__balance += amount

    def Get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
        else:
            return f'fokira taka nai '


safsan = Bank('sonali ','safsan',1000)
print(safsan.holder_name)
safsan.deposit(50000)
#print(safsan.__balence)
print(safsan.Get_balance())
safsan.holder_name = 'boro vhai'
print(safsan.holder_name)