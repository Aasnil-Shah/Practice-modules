list1 = [2,3,4,5,6,7,8]
list2 = [4,9,16,25,36,49,64]
set1 = set()
for val1 in list1:
    for val2 in list2:
        if val2 == (val1**2):
            tuple1 = tuple((val1,val2))
            print(tuple1)
            set1.add(tuple1)
print(set1)