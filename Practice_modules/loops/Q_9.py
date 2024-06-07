'''Display -10 to -1 using for loop. Expected output: 
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1  '''

d = int(input("Enter the number you want to begin with:"))
if d<0:
    for i in range(d,0,1):
        print(i)
else:
    print("Enter a negative number.")