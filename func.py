def learn_to_code():
    print("You can learn to code for free on Pythonist")

learn_to_code()


#______________________________________________________________________________

def learn_to_code():
    print("You can learn to code for free on freeCodeCamp")

    def learn_what_language():
        print("You can learn any programming language on the freeCodeCamp YouTube channel")
    
    learn_what_language()

learn_to_code()

#______________________________________________________________________________

def divNum(a, b):
    if b != 0:
        return a/b
    else:
        return 0

print(divNum(4, 2))
print(divNum(2, 0)) 

#______________________________________________________________________________

def func_1(a):
    def func_2(b):
        return a-b
    return func_2

x = func_1(100)
print ("The value of a-b is", x(50))

def another_func(a):
    return a*10

def func():
    return another_func

y = func()
print ("\nThe value of a*b is", y(10))

#______________________________________________________________________________
#______________________________________________________________________________
#______________________________________________________________________________
#______________________________________________________________________________
#______________________________________________________________________________