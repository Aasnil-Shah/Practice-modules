'''String characters balance Test. 
We’ll say that a String s1 and s2 is balanced if all the chars in the s1 are there in s2. characters position doesn’t matter.'''

s1 = "Yn"
s2 = "PYnative"
is_there = True
for i in s1:
   index = s2.find(i)
   if index == -1:
      is_there = False
      break
print(is_there)