'''Write a program to find two string Anagram or Not. (Anagram Ex: 1. listen, Silent . 2. Read,Dear'''

str1 = "listen"
str2 = "silent"
#str1 = "read"
#str2 = "dear"
lst_str1 = list(str1.lower())
lst_str2 = list(str2.lower())
lst_str1.sort()
lst_str2.sort()
if lst_str1 == lst_str2:
    print("The strings are anagram")
else:
    print("The strings aren't an anagram")