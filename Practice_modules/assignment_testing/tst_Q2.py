str1 = "32.054,23"
str2 = ""
for char in str1:
    if char == ".":
        str2 += ","
    elif char == ",":
        str2 += "."
    else:
        str2 += char 
print(str2)
#str1.replace('.',',')