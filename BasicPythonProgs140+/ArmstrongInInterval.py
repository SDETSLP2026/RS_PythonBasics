"""
Program 20
Write a Python Program to Find Armstrong Number in an Interval.
"""

# Take 2 numbers from a user
lower = int(input("Enter lower limit of the interval: "))
upper = int(input("Enter upper limit of the interval: "))

for num in range(lower, upper + 1):  # Iterate through number in range
    order = len(str(num))  # Find the number of digits in num
    temp_num = num
    sum = 0

    while temp_num > 0:
        digit = temp_num % 10  # To extract the last digit of num
        sum += digit ** order
        temp_num //=  10

    # Check if 'num' is an Armstrong number
    if num == sum:
        print(num)

"""
Enter lower limit of the interval: 10
Enter upper limit of the interval: 1000
153
370
371
407
"""
