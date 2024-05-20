str1 = "P@#yn26at^&i5ve"
len_str = len(str1)
cnt_chr = 0
cnt_int = 0
for i in str1:
    if i.isalpha():
        cnt_chr = cnt_chr + 1
    if i.isdigit():
        cnt_int = cnt_int + 1
cnt_spl = len_str - cnt_chr - cnt_int
print("Total no of characters:",cnt_chr)
print("Total no of digits:",cnt_int)     
print("Total no of special charas:",cnt_spl)