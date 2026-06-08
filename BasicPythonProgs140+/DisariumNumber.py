"""
Write a Python program to check if the given number is a Disarium Number.
A Disarium number is a number that is equal to the sum of its digits each raised to thepower of its respective position.
For example, 89 is a Disarium number because
8^1 + 9^2 = 8+81 = 89
"""

def is_disarium(num):
    # Convert the number to a String to iterate through its digits
    num_str = str(num)

    # Calculate the sum of digits raised to their respective positions
    digit_sum = sum(int(i) ** (index+1) for index, i in enumerate(num_str))

    # check if the sum is equal to original number
    return digit_sum == num

# Take a number from user
try:
    num = int(input("Enter a number: "))

    # Check if it is a disarium number
    if is_disarium(num):
        print(f"{num} is a disarium number.")
    else:
        print(f"{num} is not a disarium number.")
except ValueError:
    print("Invalid input. Please enter a valid number")