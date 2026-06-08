"""
Program 53: Write a Python program to find the second-largest number in a list.
"""

# sample list of numbers
numbers = [30, 10, 45, 5, 20]

# Sort the list in ascending order
numbers.sort(reverse=True)

# check if there are at least 2 elements in the list
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is: ", second_largest)
else:
    print("The list does not contain the second largest number")