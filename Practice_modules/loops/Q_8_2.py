'''Reverse the following list using for loop.
list1 = [10, 20, 30, 40, 50]'''

list1 = [10, 20, 30, 40, 50]
first = 0
last = len(list1) - 1
while(first<last):
    temp = list1[first]
    list1[first] = list1[last]
    list1[last] = temp
    first += 1
    last -= 1
print(list1)