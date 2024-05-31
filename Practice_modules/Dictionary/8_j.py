dict1 = {"son's name:":"Lucas", "son's eyes:":"green","son's height:":32,"son's weight:":25}
#values = [val for val in dict1.values() if str(val).isdigit()]
values = []
for val in dict1.values():
    if str(val).isdigit():
        values.append(val)
ans_1 = [i for i in dict1 if dict1[i]==max(values)]
print(ans_1)