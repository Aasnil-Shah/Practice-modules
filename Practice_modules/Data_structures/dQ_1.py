listone = [3,6,9,12,15,18,21]
listtwo = [4,8,12,16,20,24,28]
odd_lst = []
even_lst = []
fnl_lst = []
len_lst1 = len(listone)
len_lst2 = len(listtwo)
for i in range(len_lst1):
    if i%2 != 0:
        odd_lst.append(listone[i])
for j in range(len_lst2):
    if j%2 == 0:
        even_lst.append(listtwo[j])
fnl_lst.extend(odd_lst)
fnl_lst.extend(even_lst)
print("Elements with odd number of index in list one:\n",odd_lst)
print("Elements with even number of index in list two:\n",even_lst)
print("Printing the final third list:\n", fnl_lst)