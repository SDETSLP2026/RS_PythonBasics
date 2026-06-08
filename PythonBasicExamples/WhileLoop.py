from xml.dom.minidom import ProcessingInstruction

it = 4

while it > 1: # We need to ensure to false this condition
    if it != 3: # If we need to skip 3
        print(it)  # 4, 2

    it = it - 1

print("While loop execution is done.")

print("**************************************************")

x = 10

while x > 1:
    if x == 9:
        x = x - 1
        continue # This will skips the set condition and proceed with remaining iterations

    if x == 3:
        break # This will came out of loop when the condition is satisfied.

    print(x)

    x = x -1


print("While loop stops on the occurrence of 3")