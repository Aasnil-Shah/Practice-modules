'''Create an inner function to calculate the addition in the following way:
 Create an outer function that will accept two parameters a and b
 Create an inner function inside an outer function that will calculate the
addition of a and b
 At last, an outer function will add 5 into addition and return it'''

def inputadd(a,b):
    def add(a,b):
        sum1 = a + b
        return sum1
    return add(a,b) + 5

sol = inputadd(2,3)
print(sol)