"""
Program 40: Write a Python Program to Sort Words in Alphabetic Order.
"""

# Take multiple names as an input from user
my_str = input("Enter a string: ")

# Breakdown the string in the list of words
words = [word.capitalize() for word in my_str.split()]

# Sort the list
words.sort()

# display the sorted words
print("The sorted words are: ")
for word in words:
    print(word)

"""
Output:
Enter a string: suresh ramesh vibhuti gulgule raji ram shyam ajay
The sorted words are: 
Ajay
Gulgule
Raji
Ram
Ramesh
Shyam
Suresh
Vibhuti
"""