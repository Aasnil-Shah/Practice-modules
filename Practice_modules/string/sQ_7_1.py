s1 = "Yn"
s2 = "PYnative"
is_there = True
for i in s1:
   index = s2.find(i)
   if index == -1:
      is_there = False
      break
print(is_there)