# ===== PYTHON EXERCISES =====
# Practice problems to master the basics

# EXERCISE 1: Calculator
# Create a program that takes two numbers and prints their sum, difference, product
# Expected output example: 
#   5 + 3 = 8
#   5 - 3 = 2
#   5 * 3 = 15
# TODO: Write your code here
num1 = 5
num2 = 3
# ... your code ...


# EXERCISE 2: Temperature Conversion
# Write a program that converts Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32
# TODO: Write your code here


# EXERCISE 3: Grade Calculator
# Ask for a score (0-100) and print the grade:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
# TODO: Write your code here


# EXERCISE 4: Print Numbers 1 to 10
# Use a for loop to print numbers 1 through 10
# TODO: Write your code here


# EXERCISE 5: Sum of Numbers
# Calculate the sum of all numbers from 1 to 10 using a loop
# Expected output: 55
# TODO: Write your code here


# EXERCISE 6: Reverse a List
# Create a list [1, 2, 3, 4, 5] and print it in reverse order
# TODO: Write your code here


# EXERCISE 7: Count Vowels
# Write a function that counts vowels in a string
# Example: count_vowels("hello") should return 2
# TODO: Write your code here


# EXERCISE 8: Multiplication Table
# Write a program that prints the multiplication table for 5 (5*1=5, 5*2=10, etc)
# TODO: Write your code here


# EXERCISE 9: Find Maximum
# Write a function that takes a list of numbers and returns the maximum value
# Example: find_max([3, 7, 2, 9, 1]) should return 9
# TODO: Write your code here


# EXERCISE 10: Dictionary Practice
# Create a dictionary for a book with keys: title, author, pages, year
# Print each key and value
# TODO: Write your code here


# ===== SOLUTIONS (Scroll down to see answers) =====
print("\n" + "="*60)
print("SOLUTIONS BELOW - Try exercises first before looking!")
print("="*60 + "\n")

# SOLUTION 1
print("--- SOLUTION 1: Calculator ---")
num1 = 5
num2 = 3
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# SOLUTION 2
print("\n--- SOLUTION 2: Temperature Conversion ---")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# SOLUTION 3
print("\n--- SOLUTION 3: Grade Calculator ---")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")

# SOLUTION 4
print("\n--- SOLUTION 4: Print Numbers 1 to 10 ---")
for i in range(1, 11):
    print(i, end=" ")
print()

# SOLUTION 5
print("\n--- SOLUTION 5: Sum of Numbers ---")
total = 0
for i in range(1, 11):
    total += i
print(f"Sum of 1 to 10: {total}")

# SOLUTION 6
print("\n--- SOLUTION 6: Reverse a List ---")
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(f"Original: {numbers}")
print(f"Reversed: {reversed_list}")

# SOLUTION 7
print("\n--- SOLUTION 7: Count Vowels ---")
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

result = count_vowels("hello world")
print(f"Vowels in 'hello world': {result}")

# SOLUTION 8
print("\n--- SOLUTION 8: Multiplication Table ---")
n = 5
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

# SOLUTION 9
print("\n--- SOLUTION 9: Find Maximum ---")
def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

result = find_max([3, 7, 2, 9, 1])
print(f"Maximum value: {result}")

# SOLUTION 10
print("\n--- SOLUTION 10: Dictionary Practice ---")
book = {
    "title": "Python Basics",
    "author": "John Doe",
    "pages": 350,
    "year": 2024
}
for key, value in book.items():
    print(f"{key}: {value}")
