'''Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of
s1.'''

s1 = "Ault"
s2 = "Kelly"
len_s1 = len(s1)
#len_s2 = len(s2)
mid_s1 = int((len_s1/2))
out_str = s1[:mid_s1] + s2 + s1[mid_s1:]
print(out_str)