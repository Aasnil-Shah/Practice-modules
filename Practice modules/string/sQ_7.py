s1 = "Yn"
s2 = "PYnative"
is_there = False
for i in s1:
   #index = s2.find(i)
    for j in s2:
        if i == j:
            is_there = True
            break
        else:
            is_there = False
    if is_there == False:
       break

print(is_there)