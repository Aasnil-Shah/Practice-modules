'''String characters balance Test. 
We’ll say that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters position doesn’t matter.'''

s1 = "Yn"
s2 = "PYnative"
set_s1 = set(s1)
set_s2 = set(s2)
print(set_s1.issubset(set_s2))