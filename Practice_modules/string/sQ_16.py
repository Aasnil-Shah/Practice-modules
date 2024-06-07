'''Removal all the characters other than integers from string.'''

str1 = "I am 25 years and 10 months old"
str_num = ""
for str in str1:
    if str.isdigit():
        str_num = str_num + str

print(str_num)