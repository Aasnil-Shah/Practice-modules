'''Write a program to reverse middle words of string. 
Input: Hi how are you python
Output: Hi woh era uoy python'''

str1 = "Hi How are you python ahoy captain"
r_str1 = ""
wrd_lst = str1.split()
len_wrds = len(wrd_lst)
cnt = 0
for wrd in wrd_lst:
    if (cnt == 0) or (cnt == len_wrds-1):
        r_str1 += wrd + " "
    else:
        r_str1 += wrd[::-1] + " "
    cnt += 1
print(r_str1)