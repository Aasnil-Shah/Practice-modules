str1 = "32.054,23"
str2 = ""
'''for char in str1:
    if char == ".":
        str2 += ","
    elif char == ",":
        str2 += "."
    else:
        str2 += char '''
str1=str1.replace('.','@')
str1=str1.replace(',','.')
str1=str1.replace('@',',') #use  inttermediate symbols to solve the probblenm
print(str1)
