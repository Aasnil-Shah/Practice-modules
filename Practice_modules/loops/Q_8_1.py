list1 = [10, 20, 30, 40, 50]
list2 = []
lenlist = len(list1)
for i in range(lenlist-1,-1,-1):
    list2.append(list1[i])
print(list2)