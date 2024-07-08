def sum(num1,num2,num3=0):
    result = num1+num2+num3
    return result
total = sum(90,10,5)
#print('total = ',total)

def all_sum(num1,num2,*numbers):
    print(numbers)
    sum_a=0
    for i in numbers:
        print(i)
        sum_a = sum_a+i
    return sum_a

    

total = all_sum(1,2,5,5,5)
print('all sum ',total)

def do_a_lot(*args):
    print(args) # send parameter as like numbers of variable 
    