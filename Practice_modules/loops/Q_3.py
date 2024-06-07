'''Accept number from user and calculate the sum of all number between 1 and
given number. For example user given 10 so the output should 55.'''

sum = 0
i = 0
n = int(input("Enter the number until which you want to find the sum:"))
while i < (n+1):
    sum += i
    i += 1
print(sum)