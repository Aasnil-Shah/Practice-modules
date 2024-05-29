s1 = "America"
s2 = "Japan"
len_s1 = len(s1)
len_s2 = len(s2)
mid_s1 = int(((len_s1-1)/2))
mid_s2 = int(((len_s2-1)/2))
out_str = s1[0] + s2[0] + s1[mid_s1] + s2[mid_s2] + s1[-1] + s2[-1]
print(out_str)