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

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#_____________________________________________________________

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#_____________________________________________________________


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#_____________________________________________________________

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#_____________________________________________________________
  
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#_____________________________________________________________
  
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
  
#_____________________________________________________________
#_____________________________________________________________
#_____________________________________________________________
#_____________________________________________________________
#_____________________________________________________________


