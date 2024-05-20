str1 = "Hi How are you python"
r_str1 = ""
sub_str = ""
wrd_lst = []
strlen = len(str1)
for i in range(strlen):
    if str1[i] == " ":
        wrd_lst.append(sub_str)
        sub_str = ""
    else:
        sub_str = sub_str + str1[i]
wrd_lst.append(sub_str)
lst_len = len(wrd_lst)
mid = int((lst_len-1)/2)
for j in range(lst_len):
    temp = str(wrd_lst[j])
    if j == mid:
        r_str1 = r_str1 + temp[::-1] + " "
    elif j == (mid+1):
        r_str1 = r_str1 + temp[::-1] + " "
    elif j == (mid-1):
        r_str1 = r_str1 + temp[::-1] + " "
    else:
        r_str1 = r_str1 + temp + " "

print(r_str1)