"""
Program 36: Write a Python Program to check if given array is Monotonic.
A monotonic array is one that is entirely non-increasing or non-decreasing.
"""


def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing


# Test the function
arr1 = [1, 2, 2, 3]  # Monotonic (non-decreasing)
arr2 = [3, 2, 1]  # Monotonic (non-increasing)
arr3 = [1, 3, 2, 4]  # Non-monotonic

# Print the result
print("Is arr1 monotonic?: ", is_monotonic(arr1))  # True
print("Is arr2 monotonic?: ", is_monotonic(arr2))  # True
print("Is arr3 monotonic?: ", is_monotonic(arr3))  # False
