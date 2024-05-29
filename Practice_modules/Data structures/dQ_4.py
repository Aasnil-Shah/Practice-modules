list1 = [11,45,8,11,23,45,23,45,89]
rep_dict = {}
for i in list1:
    if i in rep_dict:
        rep_dict[i] += 1
    else:
        rep_dict[i] = 1
print(rep_dict)