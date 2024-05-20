len = int(input("Enter the length of pattern:"))
for i in range(len+1):
    x = len - i
    for j in range(x):
        print(x-j, end = " ")
    print()