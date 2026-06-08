"""
Program 35: Write a Python Program to Split the array and add the first part to the end?
"""


def split_and_append(arr, k):
    if k <= 0 or k >= len(arr):
        return arr

    # split the array into 2 parts
    first_part = arr[:k]
    second_part = arr[k:]

    # Add the first part to the end of the second part
    result = second_part + first_part

    return result


# Test the function
arr = [1, 2, 3, 4, 5]  # Passing array as an input
k = 3
result = split_and_append(arr, k)
print("Original Array: ", arr)
print("Array after splitting and appending: ", result)
