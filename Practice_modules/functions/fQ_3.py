'''Write a function calculation() such that it can accept two variables and
calculate the addition and subtraction of it. And also it must return both
addition and subtraction in a single return call'''

def calculation(a,b):
    sumat = a + b
    substr = a - b
    #val = [sum,sub]
    return sumat,substr

#ans = calculation(2,4)
[sum1,sub1] = calculation(2,7)
print("Addition of numbers is:", sum1)
print("Subtractiion of numbers is:", sub1)