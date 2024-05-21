num = int(input("Enter a non-single digit positive number you want to find the nearest palindrome for:"))
lwr_num = num
upr_num = num
lwr_pl = 0
upr_pl = 0
fg_lwr = False
fg_upr = False
str_upr = ""
str_lwr = ""
while not fg_lwr:
    str_lwr = str(lwr_num)
    if str_lwr[:] == str_lwr[::-1]:
        fg_lwr = True
        lwr_pl = lwr_num
    else:
        lwr_num = lwr_num - 1
diff_lwr = num - lwr_num
while not fg_upr:
    str_upr = str(upr_num)
    if str_upr[:] == str_upr[::-1]:
        fg_upr = True
        upr_pl = upr_num
    else:
        upr_num = upr_num + 1
diff_upr = upr_num - num
if diff_upr > diff_lwr:
    print("The nearest palindrome is:", lwr_pl)
else:
    print("The nearest palindrome is:", upr_pl)