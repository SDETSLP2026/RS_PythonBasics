"""
Program 2
Write a Python program to do arithmetical operations addition and division.
"""
# Addition
# Accept 2 numbers
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))
sum_result = num1 + num2

# Display the addition details
print(f"Sum: {num1} + {num2} = {sum_result}")

# Division
# Accept 2 numbers as dividend & divisor
num3 = float(input("Enter the dividend for division: "))
num4 = float(input("Enter the divisor for division: "))

# Handle the exception for divisor = 0
if num4 == 0:
    print("Error: Division by zero is not allowed.")
else:
    div_result = num3 / num4
    # Display the division details
    print(f"Division: {num3} / {num4} = {div_result}")
