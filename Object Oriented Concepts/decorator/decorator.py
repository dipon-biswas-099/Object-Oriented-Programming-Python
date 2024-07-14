#decorator nested function with func parameter
import math
import time
def timer(func):
    def inner(*args,**kwargs):
        print('timer started')
        start = time.time()
       # print(func)
        func(*args,**kwargs)
        end = time.time()
        print(f'total time taken {end-start} ')

    return inner
#timer()()
@timer #decorator
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(f'factorial of  {n} is : {result}')



get_factorial(12)




