'''Reverse a given integer number. 
Given:
76542
Expected output:
24567'''

strint = input("Enter the integer to reverse:")
rstrint = ""
if strint.isdigit():
    strlen = len(strint)
    for i in range(strlen-1,-1,-1):
        rstrint += strint[i]
else:
    print("Enter a valid non-negative no.")
print(rstrint, end="")