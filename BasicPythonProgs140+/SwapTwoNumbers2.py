"""
Program 10
Write a Python program to swap two variables without temp variable.
"""

# Input 2 variables
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")

# Display the original values
print(f"Original values: a = {a}, b = {b}")

# Swap the values without using temp variable
a, b = b, a

# Display the swapped values
print(f"Swapped values: a = {a}, b = {b}")