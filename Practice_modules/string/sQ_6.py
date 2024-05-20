s1 = "Abc"
s2 = "Xyzwe"
out_str = ""
len_s1 = len(s1)
len_s2 = len(s2)
if len_s1 == len_s2:
    for i in range(len_s1):
        out_str = out_str + s1[i] + s2[len_s1-i-1]
elif len_s1 > len_s2:
    for i in range(len_s2):
        out_str = out_str + s1[i] + s2[len_s2-i-1]
    out_str = out_str + s1[len_s2:]
else:
    for i in range(len_s1):
        out_str = out_str + s1[i] + s2[len_s1-i-1]
    out_str = out_str + s2[len_s1:]    

print(out_str)