#list , array , collection is same (simple term )
numbers = [45,56,12,89,87,32,89,59,46,93]
#index  = -10 -9 -8 -7 -6 -5 -4-3 -2-1
print(numbers[3], numbers[-3])

#list(start : end ) start from the start index and stop  before the end  
print(numbers[2:6])

#list(start : end : step)

print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[7:2:-1])

print(numbers[4:])
print(numbers[:5])

print(numbers[:])# shortcut to copy a list

#for reverse the list shortcut
print(numbers[::-1])