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

class Greetings:
    def good_morning(name):
        print(f'Good morning {name}')
        
    def good_afternoon(name):
        print(f'Good afternoon {name}')
        
    def good_evening(name):
        print(f'Good evening {name}')
        
        
Greetings.good_afternoon('John')
Greetings.good_morning('Peter')
Greetings.good_evening('Jane') 
#______________________________________________________________________________

class Student:
    def __init__(self, first, last, age, major):
        self.first = first 
        self.last = last
        self.age = age
        self.major = major
    
    def profile(self):
        print(f"Student name {self.first + ' ' + self.last}")
        print(f"Student age: {self.age}")
        print(f"Major: {self.major}")
        
    
    
s = Student('Sally' , 'Harris', 20, 'Biology')    
    
s.profile()
#______________________________________________________________________________

class Student:
    def __init__(self, first, last, age, major):
        self.first = first 
        self.last = last
        self.age = age
        self.major = major
        self.courses = [] 
    
    def profile(self):
        print(f"Student name {self.first + ' ' + self.last}")
        print(f"Student age: {self.age}")
        print(f"Major: {self.major}")
        
        
    def enrol(self, course):
        self.courses.append(course)
        print(f"enrolled {self.first} in {course}")
        
    
    def show_courses(self):
        print(f"{self.first + ''  + self.last} is taking the following courses")
        for course in self.courses:
            print(course)
        
                
s = Student('Sally' , 'Harris', 20, 'Biology')    
    
s.enrol('Biochemistry I')    
# enrolled Sally in Biochemistry I

s.enrol('Literature')    
# enrolled Sally in Literature

s.enrol('Mathematics')
# enrolled Sally in Mathematics

s.show_courses()
# SallyHarris is taking the following courses
# Biochemistry I
# Literature
# Mathematics 
#______________________________________________________________________________
#______________________________________________________________________________