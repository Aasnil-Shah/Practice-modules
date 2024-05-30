def inputadd(a,b):
    def add(a,b):
        sum1 = a + b
        return sum1
    return add(a,b) + 5

sol = inputadd(2,3)
print(sol)