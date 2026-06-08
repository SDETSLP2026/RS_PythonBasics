"""
Program 52: Write a Python program to find the largest number in a list.
"""

# Sample list of numbers
numbers = [30, 10, -45, 5, 20]

# Creating a variable to store the smallest number in the list
maximum = numbers[0]

# Iterate through the list & update min value
for i in numbers:
    if i > maximum:
        maximum = i

print("The largest number in the list is: ", maximum)
