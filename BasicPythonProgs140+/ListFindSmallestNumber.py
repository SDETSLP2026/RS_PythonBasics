"""
Program 51: Write a Python program to find the smallest number in a list.
"""

# Sample list of numbers
numbers = [30, 10, -45, 5, 20]

# Creating a variable to store the smallest number in the list
minimum = numbers[0]

# Iterate through the list & update min value
for i in numbers:
    if i < minimum:
        minimum = i

print("The smallest number in the list is: ", minimum)
