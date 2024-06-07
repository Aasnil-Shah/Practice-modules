'''Arrange string characters such that lowercase letters should come first. 
Given an input string with the combination of the lower and upper case arrange
characters in such a way that all lowercase letters should come first'''

str1 = "PyNaTive"
out1 = ""
out2 = ""
for i in str1:
    if i.islower():
        out1 += i
    else:
        out2 += i
print(out1 + out2)