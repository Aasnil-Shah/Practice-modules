list1 = [10, 20, 30, 40, 50]
list2 = list(list1)
#list1.reverse()
lenlist = len(list1)
for i in range(lenlist):
    list2[i] = list1[-i-1]
print(list2)