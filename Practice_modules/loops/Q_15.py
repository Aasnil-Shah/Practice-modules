'''Use a loop to display elements from a given list which are present at even
positions. Given:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected output:
20 40 60 80 100'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
listlen = len(my_list)
for i in range(1,listlen,2):
    print(my_list[i], end = " ")