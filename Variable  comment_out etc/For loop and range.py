numbers = [1,2,3,4,5]
sum=0
for i in numbers:
    sum = sum+i
    if sum >10:
        print('big value ',sum)
print('the sum of the array is ',sum)


for i in range(1,10 ,2):
    print(i)

numb = [1, 2, 3, 4, 5]
for index in range(len(numb)):
    value = numb[index]
    print("Index:", index, "Value:", value)