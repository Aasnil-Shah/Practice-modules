str1 = "Hi How are you python ahoy captain"
r_str1 = ""
wrd_lst = str1.split()
lst_len = len(wrd_lst)
for j in range(lst_len):
    if lst_len % 2 == 0:
        mid = int((lst_len)/2)
        if j in range(mid-2,mid+2):
            r_str1 += wrd_lst[j][::-1] + " "
        else:
            r_str1 += wrd_lst[j] + " "
    else:
        mid = int((lst_len-1)/2)
        if j in range(mid-1,mid+2):
            r_str1 += wrd_lst[j][::-1] + " "
        else:
            r_str1 += wrd_lst[j] + " "

print(r_str1)