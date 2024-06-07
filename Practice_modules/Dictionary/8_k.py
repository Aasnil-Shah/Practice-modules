'''Exercise 8-k: Min function to get the key with the lowest value
What's the key with the lowest value in the dictionary'''

dict1 = {"son's name:":"Lucas", "son's eyes:":"green","son's height:":32,"son's weight:":25}

values = [val for val in dict1.values() if str(val).isdigit()]
ans_1 = [i for i in dict1 if dict1[i]==min(values)]
print(ans_1)