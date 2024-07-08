numbers = [1,2,3,4,5,6,71,15,25]
odds=[]
for num in numbers:
    if num%2 == 1:
        odds.append(num)

print(odds)

playes = ['sakib','tamim','mustafiz']
ages =[30,32,31]
age_com =[]
for player in playes:
    print('playes : ',player)
    for age in ages:
        print(player , age)
        age_com.append([player,age])


print(age_com)