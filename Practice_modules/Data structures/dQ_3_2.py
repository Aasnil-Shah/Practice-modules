'''Given a list slice it into a 3 equal chunks and rever each list'''

list1 = [11,45,8,23,14,12,78,45,89]
cnt = 0
chnk_1 = []
chnk_2 = []
chnk_3 = []
for i in list1:
    if cnt <3:
        chnk_1.append(i)
    elif cnt>=3 and cnt<6:
        chnk_2.append(i)
    else:
        chnk_3.append(i)
    cnt += 1
print("Chunk 1:", chnk_1)
print("After reversing it", chnk_1[::-1])
print("Chunk 2:", chnk_2)
print("After reversing it", chnk_2[::-1])
print("Chunk 3:", chnk_3)
print("After reversing it", chnk_3[::-1])