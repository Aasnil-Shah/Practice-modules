'''Print the following pattern. 
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5'''

len = int(input("Enter the end number of the patern:"))
#d = 5
for i in range(1,len+1):
    for j in range(i):
        print(j+1, end = " ")
    print()