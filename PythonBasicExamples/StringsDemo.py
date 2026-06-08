str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1]) # a

print(str[0:5]) # if you want to get substring in python

print(str+" "+str1) # Concatenation

print(str3 in str) # Substring check

var = str.split(".") #To split a string
print(var) # ['RahulShettyAcademy', 'com']
print(var[0]) # RahulShettyAcademy
print(var[1]) # com

str4 = " great "
print(str4.strip()) # to trim the leading & trailing white spaces in the string
print(str4.lstrip()) # to trim the white spaces at left
print(str4.rstrip()) # to trim the white spaces at right

