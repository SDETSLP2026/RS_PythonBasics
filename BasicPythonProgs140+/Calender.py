"""
Program 8
Write a Python program to display calendar.
"""
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month number: "))

cal = calendar.month(year, month)
print(cal)