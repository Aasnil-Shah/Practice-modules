import math
lr = int(input("Enter the lower bound:"))
up = int(input("Enter the upper bound:"))
isprime = False
for cprime in range(lr,up+1):
        for i in range(2,math.floor(math.sqrt(cprime))+1):
            if cprime % i == 0:
                  break
        else:
            isprime = True
            print(cprime)              