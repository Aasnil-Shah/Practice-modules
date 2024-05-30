len = int(input("Enter the length of pattern:"))
for i in range(len,0,-1):
    for j in range(i,0,-1):
        print(j, end = " ")
    print()