def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b

result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12


def add(a, b):
    return a + b

sum_result = add(3, 5)  # sum_result gets the value 8


def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)

print_numbers(5)  # Output: 1 2 3 4 5


def greet(name):
    return "Hello, " + name

for _ in range(3):
    print(greet("Alice"))


def beer(name):
    return'Hello? ' + name
for i in range(3):
    print(beer("ALICE"))

