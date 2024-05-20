str1 = "32.054,23"
str2 = ""
for char in str1:
    if char == ".":
        str2 = str2 + ","
    elif char == ",":
        str2 = str2 + "."
    else:
        str2 = str2 + char 
print(str2)