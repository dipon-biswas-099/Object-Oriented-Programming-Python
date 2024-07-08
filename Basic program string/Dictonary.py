numbers = [ 11,12,13,14,15,16,14]
#key value pair 
#dictionary
#object
#hash table
#overlap with set

person={'name' : 'kala chad' ,'adress ': 'kaliapur' ,'age ': 23 ,'job': 'bekar'}
print(person)
print(person['job'])
print(person.keys()) 
print(person.values())
person['language']='python'

#special dictionary looping 
for key,value in person.items():
    print(key,value)