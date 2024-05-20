num = int(input("Enter the number you want to find the factorial of:"))
fact = 1
for i in range(num):
    fact = fact * (num - i)
print(fact)