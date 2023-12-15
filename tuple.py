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

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#_____________________________________________________________

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#_____________________________________________________________

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#_____________________________________________________________

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#_____________________________________________________________
#_____________________________________________________________
#_____________________________________________________________
#_____________________________________________________________
#_____________________________________________________________