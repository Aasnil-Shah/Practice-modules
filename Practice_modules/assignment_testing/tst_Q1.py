'''Write a program to find the ASCII value of each character of the string in python. '''

str1 = "DELL"
str_ascii = ""
for char in str1:
    ascii = ord(char)
    str_ascii += str(ascii)
print(str_ascii)