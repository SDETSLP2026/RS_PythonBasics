"""
Program 54: Write a Python program to find N largest elements from a list.
"""

def find_n_largest_number(list, n):
    #Sort the list in descending order
    sorted_list = sorted(list, reverse=True)

    #Get the first n elements
    largest_elements = sorted_list[:n]

    return largest_elements

# Sample list of numbers
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

# Number of largest elements to find
N = int(input("N = "))

# Find the N largest elements from the list
result = find_n_largest_number(numbers, N)

# Print the N largest elements
print(f"The {N} largest elements from the list are:", result)
