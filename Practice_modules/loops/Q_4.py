'''Print multiplication table of given number. For example num = 2 so the output should be
2
4
6
8
10
12
14
16
18
20'''

d = int(input("Enter the number you want the multiplication number of:"))
for i in range(1,11):
    print(d*(i))