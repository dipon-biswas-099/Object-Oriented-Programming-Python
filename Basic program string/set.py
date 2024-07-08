# for using list --> []
#touple = []
# set = {}
#set is no duplicate or  uniqe items collection
numbers =[12,56,12,45,3,5,65]
print(numbers)
number_set = set(numbers)
print(number_set)
number_set.add(55)
print(number_set)
number_set.remove(3)
print(number_set)


for item in number_set:
    print(item)


if 9 in number_set:
    print('exist')
else:
    print("doesn't exist")

A ={1,2,3}
B ={2,3,4,5}
print(A & B) # print only the common elements 
print (A | B) # print common uncommon all

