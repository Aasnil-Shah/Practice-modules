my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
listlen = len(my_list)
for i in range(listlen):
    if (i+1)%2 == 0:
        print(my_list[i], end = " ")