'''Given an input string, count occurrences of all characters within a string'''

str1 = "Apple"
rep_dict = {}
for i in str1:
    if i in rep_dict:
        rep_dict[i] += 1
    else:
        rep_dict[i] = 1
print(rep_dict)