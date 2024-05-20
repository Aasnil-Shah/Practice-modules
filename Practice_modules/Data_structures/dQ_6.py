rollno = [47,64,69,37,76,83,95,97]
new_lst = []
dict = {'Jhon':47,'Emma':69,'Kelly':76,'Jason':97}
flag = False
for val in rollno:
    flag = False
    for info in dict:
        if dict.get(info) == val:
            flag = True
    if flag:
        new_lst.append(val)
print("After removing the extra items:", new_lst)