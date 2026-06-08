"""
Program 16
Write a Python Program to Find the Factorial of a Number.
Factorial of 4 = 4*3*2*1 = 24
"""

num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(f"The factorial of {num} is {fact}")
