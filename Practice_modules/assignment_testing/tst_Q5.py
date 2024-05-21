N = 5
for i in range(N+1):
    for j in range(N-i):
        print(" ", end = "")
    for k in range(i):
        print("* ", end = "")
    print()
for l in range(N+1):
    for m in range(l):
        print(" ", end = "")
    for n in range(N-l):
        print("* ", end = "")
    print()