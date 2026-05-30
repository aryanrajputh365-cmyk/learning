# ===== PYTHON BASICS TUTORIAL =====
# Learn Python from scratch with examples and exercises

# ===== 1. VARIABLES AND DATA TYPES =====
# Variables store data. No need to declare type in Python.

# String (text)
name = "Alice"
print(name)  # Output: Alice

# Integer (whole numbers)
age = 25
print(age)  # Output: 25

# Float (decimal numbers)
height = 5.8
print(height)  # Output: 5.8

# Boolean (True/False)
is_student = True
print(is_student)  # Output: True

# Check type
print(type(name))  # Output: <class 'str'>
print(type(age))  # Output: <class 'int'>


# ===== 2. BASIC OPERATIONS =====
# Arithmetic operations
a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)  # Modulo (remainder): 1
print(a ** b)  # Exponentiation: 1000

# String operations
greeting = "Hello"
name = "World"
print(greeting + " " + name)  # String concatenation: Hello World
print(greeting * 3)  # String repetition: HelloHelloHello


# ===== 3. CONDITIONAL STATEMENTS (IF/ELSE) =====
age = 20

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")


# ===== 4. LOOPS =====

# FOR loop (iterate a fixed number of times)
print("For loop:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# FOR loop with list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# WHILE loop (iterate while condition is true)
print("\nWhile loop:")
count = 0
while count < 3:
    print(count)
    count += 1  # count = count + 1


# ===== 5. LISTS =====
# Ordered collection of items (can be modified)

numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Access first element: 1
print(numbers[-1])  # Access last element: 5
print(len(numbers))  # Length: 5

# Add to list
numbers.append(6)
print(numbers)  # [1, 2, 3, 4, 5, 6]

# Remove from list
numbers.remove(3)
print(numbers)  # [1, 2, 4, 5, 6]

# Slice (get part of list)
print(numbers[1:3])  # [2, 4]


# ===== 6. DICTIONARIES =====
# Unordered collection of key-value pairs

student = {
    "name": "Bob",
    "age": 20,
    "grade": "A"
}

print(student["name"])  # Access value: Bob
student["age"] = 21  # Modify value
student["city"] = "NYC"  # Add new key-value
print(student)


# ===== 7. FUNCTIONS =====
# Reusable blocks of code

def greet(name):
    """This function greets someone"""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Function with multiple parameters
def add(x, y):
    return x + y

result = add(5, 3)
print(result)  # Output: 8

# Function with default parameter
def power(base, exponent=2):
    return base ** exponent

print(power(3))  # Output: 9 (3^2)
print(power(3, 3))  # Output: 27 (3^3)


# ===== 8. STRING METHODS =====
text = "python"

print(text.upper())  # PYTHON
print(text.capitalize())  # Python
print(text.replace("p", "j"))  # jython
print(text.split("t"))  # ['py', 'hon']


print("\n" + "="*50)
print("SCROLL DOWN FOR EXERCISES!")
print("="*50)
