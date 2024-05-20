def check_even(N):
    n = N
    even_no = list()
    for i in range(n+1):
        if i%2 == 0:
            even_no.append(i)
    return even_no

N=14
ans = check_even(N)
print(ans)