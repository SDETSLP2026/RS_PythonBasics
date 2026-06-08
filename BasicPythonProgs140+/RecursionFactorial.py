"""
Program 28
Write a Python Program to Find Factorial of Number Using Recursion.
The factorial of a non-negative integer ( n ) is the product of all positive integers less than orequal to ( n ).
It is denoted by ( n! ) and is defined as:
n! = n X (n-1) X (n-2) X .... X 3 X 2 X 1
For example:
5! = 5 X 4 X 3 X 2 X 1 = 120
0! is defined to be 1.
Factorials are commonly used in mathematics, especially in combinatorics and probability,
to count the number of ways a set of elements can be arranged or selected.
"""

def recursion_factorial(n):
    if n == 1:
        return n
    else:
        return n*recursion_factorial(n-1)

num = int(input("Enter the number: "))

# Check if the number is negative
if num < 0:
    print("Sorry, Factorial doesn't exist for negative numbers.")
elif num ==0:
    print("The factorial of 0 is 1.")
else:
    print("The factorial of ", num, "is: ", recursion_factorial(num))