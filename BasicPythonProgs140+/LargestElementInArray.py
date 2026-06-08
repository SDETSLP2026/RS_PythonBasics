"""
Program 33: Write a Python Program to find the largest element in an array.
"""
#1. Defining a function to find the largest number in a given array
def find_largest_element(arr):
    if not arr: # checking exception
        return "Array is empty"

    # Initializing first element as largest
    largest_element = arr[0]

    # Iterate through an array to find largest number
    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element

# Example usage:
my_array = [10, 20, 30, 99]
result = find_largest_element(my_array)
print(f"The largest element in the array is: {result}")