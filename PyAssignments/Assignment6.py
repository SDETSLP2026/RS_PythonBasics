"""
Practice using if-else statements.
Write a program that assigns a greeting to a variable.
Use an if statement to check if the greeting is "Hello".
If it matches, print "Hello there!" and "How can I assist you today?".
If it does not match, print "Greetings!".
After the if-else block, print "Program has completed."

Expected Output:
If greeting is "Hello":

Hello there!
How can I assist you today?
Program has completed.
If greeting is not "Hello":

Greetings!
Program has completed.
"""

# Assign a greeting to a variable
greeting = "Hello"  # You can change this to test different outputs

# Check if the greeting is "Hello"
if greeting == "Hello":
    print("Hello there!")
    print("How can I assist you today?")
else:
    print("Greetings!")

# Print after the if-else block
print("Program has completed.")