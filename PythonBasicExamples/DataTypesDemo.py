"""
Data types in Python
#1. Numeric
1.1 Int
1.2 Float
1.3 Long (Deprecated in py3+ )
1.4 Complex

2. String
3. List
4. Tuple
5. Dictionary

"""
# Numeric Data Type
print("Numeric examples -")
# create a variable with integer value.
a = 100
print("The type of variable having value", a, " is ", type(a))

# create a variable with float value.
b = 10.2345
print("The type of variable having value", b, " is ", type(b))

# create a variable with complex value.
c = 100 + 3j
print("The type of variable having value", c, " is ", type(c))

# --------------------------------------------------------------------------
# String Data Type
print("String examples -")
a = "string in a double quote"
b = 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a, "concatenated with", b)

# using '+' to concatenate the two or several strings
print(a + " concatenated with " + b)

# --------------------------------------------------------------------------

# List Data Type - in the square brackets
print("List examples -")
# list of having only integers
a = [1, 2, 3, 4, 5, 6]
print(a)

# list of having only strings
b = ["hello", "john", "reese"]
print(b)

# list of having both integers and strings
c = ["hey", "you", 1, 2, 3, "go"]
print(c)

# index are 0 based. this will print a single character
print(c[1])  # this will print "you" in list c

# RS Example
values = [1, 2, "Swapnil", 4, 5]

print(values[0])  # 1
print(values[1])  # 2
print(values[2])  # Swapnil
print(values[3])  # 4
print(values[4])  # 5
print(values[-1])  # 5 - The last index

print(values[1:3])  # 2, Swapnil

values.insert(3, "Snehal")
print(values)  # [1, 2, 'Swapnil', 'Snehal', 4, 5]

values.append("End of List")  # [1, 2, 'Swapnil', 'Snehal', 4, 5, 'End of List']
print(values)  # [1, 2, 'Swapnil', 'Snehal', 4, 5, 'End of List']

del values[1]
print(values)  # [1, 'Swapnil', 'Snehal', 4, 5, 'End of List']

# --------------------------------------------------------------------------

# Tuple =>
print("Tuple examples -")

# tuple having only integer type of data.
a = (1, 2, 3, 4)
print(a)  # prints the whole tuple

# tuple having multiple type of data.
b = ("hello", 1, 2, 3, "go")
print(b)  # prints the whole tuple

# index of tuples are also 0 based.
# Tuple is same as LIST data type but immutable
val = (1, 2, "Swapnil", 4.5)
print(val)  # (1, 2, 'Swapnil', 4.5)
print(val[1])  # 2

# val[2] = "Rahul" => 'tuple' object does not support item assignment
# In tuples, the data can't be inserted/modified/deleted.

# --------------------------------------------------------------------------

# Dictionary =>
# unordered sequence of data in key-value pair form
# written within curly braces in the form key:value
# very useful to retrieve data in an optimized way among a large amount of data.
print("Dictionary examples -")
# a sample dictionary variable
a = {1: "first name", 2: "last name", "age": 33}

# print value having key=1
print(a[1])
# print value having key=2
print(a[2])
# print value having key="age"
print(a["age"])

# RS Example {Key:Value}
dic = {"a": 2, 4: "bcd", "c": "Hello World"}
print(dic[4])  # bcd
print(dic["c"])  # Hello World

# How to create dictionary runtime
# This scenario will occur when we need to fetch data from XLS file

dict = {}

dict["First Name"] = "Swapnil"
dict["Last Name"] = "Padekar"
dict["Gender"] = "Male"

print(dict)  # {'First Name': 'Swapnil', 'Last Name': 'Padekar', 'Gender': 'Male'}
