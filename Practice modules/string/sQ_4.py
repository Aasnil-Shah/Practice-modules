str1 = "PyNaTive"
out = ""
for i in str1:
    if i.islower():
        out = out + i
for i in str1:
    if i.isupper():
        out = out + i
print(out)