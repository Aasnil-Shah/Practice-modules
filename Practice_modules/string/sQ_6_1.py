'''Given two strings, s1 and s2, create a mixed String. 
Note: create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 
and second last char of s2, and so on. Any leftover chars go at the end of the result'''

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
else:
    out_str += s2[:-diff]

print(out_str)