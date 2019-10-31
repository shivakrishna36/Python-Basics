list = [1,2,3,4,4]

# print(list[2])
# print(list[0:2])
# print(list[-3])
print(list)
del(list[4]) 
print(list)

print(list.pop(3)) #Removes and returns value
print(list.remove(3))#Removes but not returns value

lists = [x**2 for x in [1,2,3,4]] #Appends data after squaring
print(lists)

list.extend(['a','b']) #Adds the data at end of the list
print(list)

list.insert(1,'hi') #inserts at starting position
print(list)

print(sorted(lists)) #ascending order
print(list[::-1]) #prints in reverse order