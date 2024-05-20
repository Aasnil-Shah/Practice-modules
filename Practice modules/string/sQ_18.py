str1 = "/*Jon is a @developer & musician!"
new_str1 = ""
for str in str1:
    if str.isalnum() or str.isspace():
        new_str1 = new_str1 + str
    else:
        new_str1 = new_str1 + "#"

print(new_str1)