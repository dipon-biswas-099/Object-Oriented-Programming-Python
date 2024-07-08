numbers = [12,13,14,15,16]
numbers.append(65)
print(numbers)

numbers.insert(2,20) #insert(index , element)
print(numbers)

numbers.remove(12) #remove(element)
print(numbers)


if 13 in numbers:
    numbers.remove(13)
print(numbers)


last = numbers.pop()
print(last, numbers)

index = numbers.index(16) #index of 16
print(index)

print(numbers)
if 5 in numbers:
    index = numbers.index(15)
print('the index of 15 is ',index)

sorted = numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)