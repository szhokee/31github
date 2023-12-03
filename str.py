# txt = "banana"
# x = txt.center(20, "-")
# print(x)

#___________________________________________________

# sentence = "Hello, welcome to my world."
# print(sentence.endswith("."))

#___________________________________________________

# sentence = "H\te\tl\tl\to"

# print(sentence.expandtabs(1))
# print(sentence.expandtabs(2))
# print(sentence.expandtabs(3))
# print(sentence.expandtabs(4))
# print(sentence.expandtabs(5))

#___________________________________________________

# sentence = "Hello world"
# x = sentence.find("world")
# print(x)


#___________________________________________________

# name = "John"
# age = 21

# sentence = "My name is {} and I am {} years old".format(name, age)

# print(sentence)


#___________________________________________________


# sentence = "This is a test"
# x = sentence.index("is", 3, 8)

# print(x)


#___________________________________________________

sentence = "This is 50"

print(sentence.isalnum())


#___________________________________________________

words = ["This", "is", "a", "test"]
sentence = " ".join(words)

print(sentence)

#___________________________________________________

print("Hello".ljust(20, "-"))


#___________________________________________________

sentence = "Hello World"
trans_table = sentence.maketrans("o", "x")

print(sentence.translate(trans_table))


#___________________________________________________

sentence = "This is a test"
parts = sentence.partition("a")

print(parts)

#___________________________________________________

sentence = "This car is my car"
last_index = sentence.rfind("car")

print(last_index) 

#___________________________________________________

print("Hello".rjust(20, "-"))

#___________________________________________________

sentence = "This car is my car, you cannot drive it"

parts = sentence.rpartition("car")
print(parts)

#___________________________________________________

items = "apple, banana, cherry"
split_items = items.rsplit(",", 1)

print(split_items)

#___________________________________________________
#___________________________________________________
#___________________________________________________





