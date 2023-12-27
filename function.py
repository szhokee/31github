def my_function():
  print("Hello from a function")

my_function()

#______________________________________________________________________________

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#______________________________________________________________________________

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#______________________________________________________________________________

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#______________________________________________________________________________

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#______________________________________________________________________________

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#______________________________________________________________________________
#______________________________________________________________________________