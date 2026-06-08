"""
Program 26
Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.
"""

def add(x,y):
    return  x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

def mod(x,y):
    return x%y

print("Select an operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

while True:
    # Take an inout from user
    choice = input("Enter choice (1/2/3/4/5): ")

    # check if the entered choice is one of the 5 options
    if choice in ('1','2','3','4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, " + ", num2, " = ", add(num1,num2))
        elif choice == '2':
            print(num1, " - ", num2, " = ", sub(num1,num2))
        elif choice == '3':
            print(num1, " * ", num2, " = ", mul(num1,num2))
        elif choice == '4':
            print(num1, " / ", num2, " = ", div(num1,num2))
        elif choice == '5':
            print(num1, " % ", num2, " = ", mod(num1,num2))

        # Check if the user wants another calculation
        # break the while loop if the answer is no
        next_calculation = input("Do you want another calculation? (Yes/No): ")
        if next_calculation == "No":
            break

    else:
        print("Invalid input.")