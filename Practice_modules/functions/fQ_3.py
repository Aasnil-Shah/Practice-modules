def calculation(a,b):
    sum = a + b
    sub = a - b
    val = [sum,sub]
    return val

ans = calculation(2,4)
print("Addition of numbers is:", ans[0])
print("Subtractiion of numbers is:", ans[1])