thisset = {"apple", "banana", "cherry"}
print(thisset)

#_____________________________________________________________

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#_____________________________________________________________

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#_____________________________________________________________

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#_____________________________________________________________

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#_____________________________________________________________
  
  thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#_____________________________________________________________

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#_____________________________________________________________

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#_____________________________________________________________

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)