#lamda

# def doubled(x):
#     return 2*x

# result = doubled(44)
# print(result)


# alternative 
doubled = lambda num: num *2
res = doubled(44)
print(res)

numbers = [1,2,3,4,5,6,7,8]
doubled_nums = map(doubled,numbers)
print(numbers)
print(list(doubled_nums))

actors = [
    {'name':'sabama' , 'age':45},
    {'name':'sabaa' , 'age':5},
    {'name':'sabam' , 'age':35},
    {'name':'sabam' , 'age':25},
]
juniors = filter(lambda actor: actor['age'] < 40 ,actors)
print(list(juniors))