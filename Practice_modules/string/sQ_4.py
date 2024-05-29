str1 = "PyNaTive"
out1 = ""
out2 = ""
for i in str1:
    if i.islower():
        out1 += i
    else:
        out2 += i
print(out1 + out2)