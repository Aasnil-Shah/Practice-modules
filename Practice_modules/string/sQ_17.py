str1 = "Emma25 is a Data scientist50 and an AI expert"
strlist = str1.split()
for substr in strlist:
    flag_alph = False
    flag_digit = False
    for j in substr:
        if j.isalpha():
            flag_alph = True
        if j.isdigit():
            flag_digit = True
    if flag_alph and flag_digit:
        print(substr)