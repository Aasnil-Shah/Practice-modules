''' Count all lower case, upper case, digits, and special symbols from a given string'''

str1 = "P@#yn26at^&i5ve"
len_str = len(str1)
cnt_chr = 0
cnt_int = 0
cnt_spl = 0
for i in str1:
    if i.isalpha():
        cnt_chr += 1
    elif i.isdigit():
        cnt_int += 1
    else:
        cnt_spl += 1
print("Total no of characters:",cnt_chr)
print("Total no of digits:",cnt_int)     
print("Total no of special charas:",cnt_spl)