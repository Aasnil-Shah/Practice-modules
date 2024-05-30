n = 5
for i in range(n+1):
    for j in range(n-i):
        print(" ", end = "")
    for k in range(i):
        print("* ", end = "")
    print()
for x in range(n+1):
    for y in range(x):
        print(" ", end = "")
    for z in range(n-x):
        print("* ", end = "")
    print()

'''n = 5
for i in range(1,n+1):
    for j in range(n+1-i,1,-1):
        print(" ", end = "")
    for k in range(1,i+1):
        print("* ", end = "")
    print()
for x in range(n+1,1,-1):
    for y in range(n+1-x,1,-1):
        print(" ", end = "")
    for z in range(1,x):
        print(" *", end = "")
    print()'''