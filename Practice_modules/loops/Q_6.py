num = int(input("Enter the number you want to find length of:"))
if num>0:
    print("length of number is:",len(str(num)))
else:
    print("length of number is:",len(str(num).split("-")[1]))