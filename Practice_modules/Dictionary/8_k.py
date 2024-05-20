dict = {"son's name:":"Lucas", "son's eyes:":"green","son's height:":32,"son's weight:":25}

#ans_1 = min(zip(dict.values(), dict.keys()))[1]
min_v = 2^63 - 1
for i in dict:
    if isinstance(dict[i],int):
        if dict[i] < min_v:
            min_v = dict[i]
            min_key = i
ans_1 = min_key
print(ans_1)