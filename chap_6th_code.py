"""
📘 Chapter 6: Functions, Recursion & Call Stack in Python
--------------------------------------------------------
This file contains easy examples and explanations for:
✅ Functions (built-in & user-defined)
✅ Parameters & Return Values
✅ Recursion Basics
✅ Call Stack Concept
"""

# -----------------------------
# 1. What is a Function?
# -----------------------------
# A function is a block of reusable code that performs a specific task.
# Functions help to avoid repetition and make the code organized.

# Syntax:
# def function_name(parameters):
#     # code block
#     return value (optional)


def greet():
    print("Hello! Welcome to Python Functions.")


greet()  # Function call


# -----------------------------
# 2. Function with Parameters & Return
# -----------------------------
def add_numbers(a, b):
    """Return the sum of two numbers"""
    return a + b


print("Sum of 3 and 5:", add_numbers(3, 5))


# -----------------------------
# 3. Default Parameters
# -----------------------------
def welcome(name="User"):
    print(f"Welcome, {name}!")


welcome()          # Uses default value
welcome("Umar")    # Custom value


# -----------------------------
# 4. Built-in Functions
# -----------------------------
print("Length of string:", len("Python"))
print("Maximum number:", max(10, 20, 5))
print("Sum of list:", sum([1, 2, 3, 4]))


# -----------------------------
# 5. Recursion (Function Calling Itself)
# -----------------------------
# Recursion = a function calling itself to solve a smaller part of a big problem.
# Must include:
# ✅ Base Case → Stops recursion
# ✅ Recursive Case → Function calls itself

def countdown(n):
    if n == 0:          # Base case
        print("Done!")
        return
    print(n)
    countdown(n - 1)    # Recursive call


countdown(5)


def factorial(n):
    """Find factorial using recursion"""
    if n == 0 or n == 1:   # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call


print("Factorial of 5:", factorial(5))


# -----------------------------
# 6. Call Stack (How Recursion Works Internally)
# -----------------------------
"""
The Call Stack is like a stack of plates:
- Each function call is placed (PUSHED) on top of the stack.
- When a function finishes, it is removed (POPPED) from the stack.

Example: factorial(3)
Step 1: factorial(3) → waits for factorial(2)
Step 2: factorial(2) → waits for factorial(1)
Step 3: factorial(1) → returns 1
Stack unwinds:
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
"""


# -----------------------------
# 7. Sum of first n natural numbers (Recursion)
# -----------------------------
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)


print("Sum of first 5 numbers:", sum_natural(5))


# -----------------------------
# 8. Reverse a string using recursion
# -----------------------------
def reverse_string(s):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]


print("Reverse of 'Python':", reverse_string("Python"))
