str1 = "Apple"
strlen = len(str1)
cnt = 0
rep_set = {}
for i in range(strlen):
    cnt = 0
    for j in range(strlen):
        if str1[i] == str1[j]:
            cnt = cnt + 1
            rep_set[str1[i]] = cnt

print(rep_set)