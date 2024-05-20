str1 = "/* Jon is a @developer & musician"
str1_new = ""
for str in str1:
    if str.isalnum() or str.isspace():
        str1_new = str1_new + str

print(str1_new)