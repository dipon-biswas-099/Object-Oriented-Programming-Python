def multiple():
    return 3,4
print(multiple()) # for touple we use first bracket
things = 'pen','tripod','a','b','c','d'
print(type(things))
print(things[0])  # touple elements

print(things[-2])
print(things[3:6]) # print element 3 to 6 number index 


# finds
if 'tripod' in things:
    print('exist')

for item  in things:
    print(item)

# size of touple
print(len(things))

mega = ([2,3,4],[5,6,7])
print(type(mega))
print(mega[0])
mega[0][1]=666
print(mega[0])