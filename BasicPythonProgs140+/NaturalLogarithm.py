"""
Program 30
Write a Python Program to calculate the natural logarithm of any number.
the natural logarithm, often denoted as ln, is a mathematical function that represents the logarithm to the base e, where e
is the mathematical constant approximately equal to 2.71828.
In other words, for a positive number x, the natural logarithm of x is the exponent y that satisfies the equation e^y = x.
Mathematically, the natural logarithm is expressed as: ln(x)
It is commonly used in various branches of mathematics, especially in calculus and mathematical analysis,
as well as in fields such as physics, economics, and engineering.
The natural logarithm has properties that make it particularly useful in situations involving exponential growth or decay.
"""
import math

num = float(input("Enter a number: "))

if num <=0:
    print("Please enter a positive number.")
else:
    # Calculate the natural logarithm (base e) of the number
    result = math.log(num)
    print(f"The natural logarithm of {num} is: {result}")