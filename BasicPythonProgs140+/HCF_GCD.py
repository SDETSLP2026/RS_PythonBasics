"""
Program 23
Write a Python Program to Find HCF.
Highest Common Factor(HCF):
HCF, or Highest Common Factor, is the largest positive integer that divides two or morenumbers without leaving a remainder.
Formula: HCF(a,b) = GCD (a,b)
For two numbers a and b, the HCF can be found using the formula:
For more than two numbers, you can find the HCF by taking the GCD of pairs of numbers ata time until you reach the last pair.
Note: GCD stands for Greatest Common Divisor.
"""

#Define a function
def compute_hcf(x,y):
    if x>y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf = i
    return hcf

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

print("The HCF is: ", compute_hcf(num1, num2))
