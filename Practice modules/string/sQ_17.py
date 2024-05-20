str1 = "Emma25 is a Data scientist50 and an AI expert"
strlen = len(str1)
sub_str = ""
str_list = []
for i in range(strlen):
    if str1[i] == " ":
        str_list.append(sub_str)
        sub_str = ""
    else:
        sub_str = sub_str + str1[i]
str_list.append(sub_str)
for str in str_list:
    len_s = len(str)
    flag_alph = False
    flag_digit = False
    for j in range(len_s):
        if str[j].isalpha():
            flag_alph = True
        if str[j].isdigit():
            flag_digit = True
    if flag_alph and flag_digit:
        print(str)