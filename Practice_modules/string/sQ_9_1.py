'''Given a string, return the sum and average of the digits that appear in the string,
ignoring all other characters.'''

str1 = "English = 78 Science = 83 Math = 68 History = 65"
outp = [0,0]
strlist = str1.split(sep=" ")
for i in strlist:
    if i.isdigit():
        outp[0] += int(i)
        outp[1] += 1
    else:
        pass

print("The sum of digits in string is:", outp[0])
print("The average of digits in string is:", outp[0]/outp[1])