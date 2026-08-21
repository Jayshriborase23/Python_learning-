# Python Functions

# 1. Basic Function
def greet():
    print("Hello, Jayshri!")
    print("Welcome to Python Functions.")


greet()


# 2. Function with Parameter
def greet_user(name):
    print("Hello,", name)


greet_user("Jayshri")


# 3. Function with Multiple Parameters
def add_numbers(a, b):
    print("Addition:", a + b)


add_numbers(10, 20)


# 4. Function with Return Value
def multiply(a, b):
    return a * b


result = multiply(5, 4)
print("Multiplication:", result)


# 5. Function with Default Parameter
def student_info(name, course="AI/ML"):
    print("Name:", name)
    print("Course:", course)


student_info("Jayshri")


# 6. Function with Multiple Return Values
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


add, sub = calculate(20, 5)

print("Addition:", add)
print("Subtraction:", sub)
