import math
# 01. List Comprehension
# Syntax : new_list = [expression for item in iterable]
print("01. List Comprehension : ")
square = [x**2 for x in range(11)]
print(f"Example 1: {square}")


# 02. Example of List Comprehension
print("\n 02. Example of List Comprehension : ")
cube = [x**3 for x in range(11)]
print(f"Example 2: {cube}")

# 03 . Example of List Comprehension
print("\n 03. Example of List Comprehension : ")
odd = [x**2 for x in range(20) if x % 2 == 1]
print(f"Example 3: {odd}")


# 04. Example of List Comprehension for factorial
print("\n 04. Example of List Comprehension : ")
Factorial = [math.factorial(x) for x in range(11)]
print(f"Example 4: {Factorial}")