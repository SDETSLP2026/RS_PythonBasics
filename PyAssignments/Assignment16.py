"""
Handle Tuple modification exception with Try Catch
Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.

"Rahul", 25, 5.9

Print the second element of the tuple.

Attempt to change the name in the tuple to a different name and explain why this will or will not work.
"""

# Create the tuple
person = ("Rahul", 25, 5.9)

# Print the second element (age)
print(f"Age: {person[1]}")

# Attempt to change the name in the tuple (this will raise an error)
try:
    person[0] = "John"  # This will not work
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")


"""
Output:
Age: 25
Error: 'tuple' object does not support item assignment - Tuples are immutable.

Explanation:
Tuples in Python are immutable, meaning their elements cannot be changed after creation. 
Attempting to assign a new value to a specific index (like person[0] = "Amit") raises a TypeError.
Let me know if you'd like a version using a mutable data structure like a list or dictionary!
"""