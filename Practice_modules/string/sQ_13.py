'''Split a given string on hyphens into several substrings and display each
substring.'''

str1 = "Emma-is-a-data-scientist"
strlist = str1.split(sep="-")
for i in strlist:
    print(i)