lr = int(input("Enter the lower bound:"))
up = int(input("Enter the upper bound:"))
diff = up - lr
isprime = 0
for i in range(diff+1):
    num = lr + i
    for j in range(num-2):
        if num % (j+2) == 0:
            isprime = 0
            break
        else:
            isprime = 1
    if isprime == 1:
        print(num)