'''Given two strings, s1 and s2, create a mixed String. 
Note: create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 
and second last char of s2, and so on. Any leftover chars go at the end of the result'''

s1 = "Abc"
s2 = "Xyzwe"
out_str = ""
len_s1 = len(s1)
len_s2 = len(s2)
diff = len_s1 - len_s2
s = list(zip(s1,s2[::-1]))
for el in s:
    for subel in el:
        out_str += subel
if diff > 0:
    out_str += s1[len_s2:]
else:
    out_str += s2[:-diff]
print(out_str)