
fruits=("mango","orange","banana","melon","kiwi")
print(fruits)

# accessing
print(len(fruits))
print(fruits[1])
print(fruits[1:3])
print(fruits[-1])

# concatenatinating
fruits2=("grapes","berries","aple")
fruits3=(fruits+fruits2)
print(fruits3)

# Checking type
print(type(fruits3))

# Adding  items
listT=list(fruits3)
print(listT)
listT.extend(["sweet banana","blue berries"])
print(listT)

# Removing an item
print(listT.pop())

tupleA=tuple(listT)
print(type(tupleA))

# print each item
for x in tupleA : 
    print(x)











