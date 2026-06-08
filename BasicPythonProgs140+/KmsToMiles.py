"""
Program 6
Write a Python program to convert kilometers to miles.
# Conversion factor: 1 kilometer = 0.621371 miles
"""

kms = float(input("Enter the distance in KMs: "))
conversion_factor = 0.621371
miles = kms * conversion_factor

print(f"{kms} KMs is equal to {miles} miles")