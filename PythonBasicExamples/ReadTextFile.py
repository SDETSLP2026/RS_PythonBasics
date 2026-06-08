file = open('test.txt')

# print(file.read()) # To read all the content from the file

# print(file.read(2)) # To read first 2 characters in the file

# print(file.read(7)) # First 5 letters + New line char + b

# print(file.readline())
# print(file.readline())

# Print line by line using readLine method
# line = file.readline() # To read a single line
# while line!="": # till the lines are not blank/EoF
#     print(line)
#     line = file.readline() # To go to the next line

# print(file.readlines()) # all the lines are stored as a list

# So to print line by line we can use for loop
for line in file.readlines():
    print(line)

file.close()