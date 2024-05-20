list1 = [11,45,8,11,23,45,23,45,89]
lst_len = len(list1)
cnt = 0
cnt_set = {}
for i in range(lst_len):
    cnt = 0
    for j in range(lst_len):
        if list1[i] == list1[j]:
            cnt = cnt + 1
            cnt_set[list1[i]] = cnt
print("Printing count of each item:", cnt_set)