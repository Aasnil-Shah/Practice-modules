strint = input("Enter the integer to reverse:")
strlen = len(strint)
rstrint = ""
for i in range(strlen):
    rstrint = rstrint + strint[-i-1]
print(rstrint)