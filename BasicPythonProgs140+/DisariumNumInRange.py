"""
Program 44: Write a Python program to print all disarium numbers between 1 to 100.
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

disarium_numbers = [num for num in range(1,101) if is_disarium(num)]

print("Disarium Numbers from 1 to 100: ")
for num in disarium_numbers:
    print(num, end= " | ")

"""
Output:
Disarium Numbers from 1 to 100: 
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 89 | 
"""