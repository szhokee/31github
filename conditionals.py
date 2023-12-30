test_value = 100

if test_value > 1:
  print("This code is executed!")

if test_value > 1000:
  print("This code is NOT executed!")

print("Program continues at this point.")

#______________________________________________________________________________

test_grade = 61

if test_grade > 60:
  print("You passed.")
else:
  print("You failed.")
#______________________________________________________________________________
  
pet_type = "fish"

if pet_type == "dog":
  print("You have a dog.")
elif pet_type == "cat":
  print("You have a cat.")
elif pet_type == "fish":
  # This is performed
  print("You have a fish")
else:
  print("Not sure!")

#______________________________________________________________________________
  
pH = 2

if pH < 7:
  print("Acidic")
elif pH > 7:
  print("Basic")
else:
  print("Neutral")

#______________________________________________________________________________
  

print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),  
#______________________________________________________________________________