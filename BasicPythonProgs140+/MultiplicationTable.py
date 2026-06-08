"""
Program 17
Write a Python Program to Display the multiplication Table for a given number.
"""

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
