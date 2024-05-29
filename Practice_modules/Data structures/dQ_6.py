rollno = [47,64,69,37,76,83,95,97]
dict1 = {'Jhon':47,'Emma':69,'Kelly':76,'Jason':97}
rollno1 = []
d_values = dict1.values()
for val in rollno:
    if val in d_values:
        rollno1.append(val)    
print("After removing the extra items:", rollno1)