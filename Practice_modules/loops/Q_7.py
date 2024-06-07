'''Print the following pattern using for loop. 
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1   '''

len = int(input("Enter the length of pattern:"))
for i in range(len,0,-1):
    for j in range(i,0,-1):
        print(j, end = " ")
    print()