thistuple = ("apple", "banana", "cherry")
print(thistuple)

#_____________________________________________________________

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#_____________________________________________________________

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#_____________________________________________________________

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#_____________________________________________________________

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#_____________________________________________________________

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#_____________________________________________________________

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#_____________________________________________________________

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#_____________________________________________________________

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#_____________________________________________________________
#_____________________________________________________________