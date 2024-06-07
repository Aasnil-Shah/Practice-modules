'''Create a function which generates a Python list of all the even numbers
between 0 to N. (Where N = Any positive number provided in the function
argument)'''

def check_even(N):
    return list(range(0,N,2))

N=14
ans = check_even(N)
print(ans)