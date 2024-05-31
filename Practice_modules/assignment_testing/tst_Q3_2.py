str1 = "listen"
str2 = "silent"
#str1 = "read"
#str2 = "dear"
isthere = False
if len(str1) >= len(str2):
    stro = str1
    stri = str2
else:
    stro = str2
    stri = str1
for chr in stro:
    if chr in stri:
        isthere = True
    else:
        isthere = False
        break
if isthere == True:
    print("The strings are anagram")
else:
    print("The strings aren't an anagram")