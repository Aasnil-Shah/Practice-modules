def inputadd(a,b):
    num1 = a
    num2 = b
    def add():
        sum1 = num1 + num2
        return sum1
    sum = add()
    return sum

def final(c):
    ans = c + 5
    return ans

sol = inputadd(2,3)
solp_5 = final(sol)
print(solp_5)