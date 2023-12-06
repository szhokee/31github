myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newSet = {element*3 for element in myList}
print("Имеющийся список:")
print(myList)
print("Созданное множество:")
print(newSet)

#___________________________________________________________________

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet = set()
for element in mySet:
   newSet.add(element**2)
print("Исходное множество:")
print(mySet)
print("Новое множество:")
print(newSet)
#___________________________________________________________________

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet = set()
for element in mySet:
    if element % 2 == 0:
        newSet.add(element)
print("Исходное множество:")
print(mySet)
print("Новое множество:")
print(newSet)
#___________________________________________________________________

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet = {element for element in mySet if element % 2 == 0}
print("Исходное множество:")
print(mySet)
print("Новое множество:")
print(newSet)
#___________________________________________________________________

mySet = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
newSet = {str(element) for element in mySet }
print("Исходное множество:")
print(mySet)
print("Новое множество:")
print(newSet)
#___________________________________________________________________
#___________________________________________________________________
#___________________________________________________________________
#___________________________________________________________________
#___________________________________________________________________
#___________________________________________________________________