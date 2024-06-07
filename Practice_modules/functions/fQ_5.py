'''Write a recursive function to calculate the sum of numbers from 0 to 10'''

def sumn(a):
    if a == 1:
        return(a)
    else:
        return(a + sumn(a-1))

n=5
out = sumn(n)
print(out)