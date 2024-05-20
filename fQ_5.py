def sumn(a):
    if a == 1:
        return(a)
    else:
        return(a + sumn(a-1))

n=5
out = sumn(n)
print(out)