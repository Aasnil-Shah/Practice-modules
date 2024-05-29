s1 = "Abcwe"
s2 = "Xyz"
out_str = ""
len_s1 = len(s1)
len_s2 = len(s2)
diff = len_s1 - len_s2
for i in range(min(len_s1,len_s2)):
        out_str += s1[i] + s2[-i-1]
if diff > 0:
    out_str += s1[len_s2:]
elif diff <0:
    out_str += s2[:-diff]
else:
    pass

print(out_str)