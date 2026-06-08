# For Loop

obj = [2, 3, 5, 7, 9]  # List
for i in obj:
    print(i)
    # print(i*2) # To print double values in the list
print("***********************************")
# Sum of first 5 natural numbers 1+2+3+4+5
# range(i,j) => i to j-1
summation = 0 #for(i=0;i<5;i++/i=i+1)
for j in range(1, 6): #The j is incremented by 1 by default
    summation = summation + j
print(summation)
print("***********************************")
#for(i=0;i<5; i=i+2)
for k in range(1,10,2): #If the k needs to be incremented by 2 then add 3rd parameter
    print(k)
print("***********************************")
#for(i=0;i<5; i=i+2)
for x in range(10): #Starting & increment parameter is not given then default considered as (0,10,1)
    print(x) #(0 to 9)