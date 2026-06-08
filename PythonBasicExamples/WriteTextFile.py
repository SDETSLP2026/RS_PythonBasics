# Problem statement -
# 1. Read the file & store all the lines in the list
# 2. Reverse the list
# 3. Write the list back to the file

# file = open('test.txt')
# file.close()
# Instead of writing above 2 lines, we can write it in an optimized way as -
# with open('test.txt') as file: # In this case we don't need to close the file explicitly


with open('test.txt', 'r') as reader:  # Open a file in read mode
    content = reader.readlines()  # [apple,ball,cat,dog,elephant]
    # print(content)
    reversed(content)  # [elephant,dog,cat,ball,apple]
    with open('test.txt', 'w') as writer: #Open a file in write mode
        for line in reversed(content):
            writer.write(line)
