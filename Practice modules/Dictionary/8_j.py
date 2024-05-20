dict = {"son's name:":"Lucas", "son's eyes:":"green","son's height:":32,"son's weight:":25}

#ans_1 = max(zip(dict.values(), dict.keys()))[1]
max_v = -(2^63)
for i in dict:
    if isinstance(dict[i],int):
        if dict[i] > max_v:
            max_v = dict[i]
            max_key = i
ans_1 = max_key
print(ans_1)