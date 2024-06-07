'''Python program to display all the prime numbers within a range. Note: A Prime Number is a whole number that cannot be made by multiplying
other whole numbers. Examples:
6 is not a Prime Number because it can be made by 2x3 = 6
37 is a Prime Number because no other whole numbers multiply together to make it. Given:
start = 25
end = 50
Expected output:
Prime numbers between 25 and 50 are:
29
31
37
41
43
47  '''

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