'''Given a list slice it into a 3 equal chunks and rever each list'''

list1 = [11,45,8,23,14,12,78,45,89]
lst_len = len(list1)
len_3 = int(lst_len/3)
chnk_1 = []
chnk_2 = []
chnk_3 = []
for i in range(len_3):
    chnk_1.append(list1[i])
    chnk_2.append(list1[len_3 + i])
    chnk_3.append(list1[2*len_3 + i])
print("Chunk 1:", chnk_1)
print("After reversing it", chnk_1[::-1])
print("Chunk 2:", chnk_2)
print("After reversing it", chnk_2[::-1])
print("Chunk 3:", chnk_3)
print("After reversing it", chnk_3[::-1])