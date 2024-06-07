'''Given a number count the total number of digits in a number. For example, the number is 75869, so the output should be 5.'''

num = int(input("Enter the number you want to find length of:"))
if num>0:
    print("length of number is:",len(str(num)))
else:
    print("length of number is:",len(str(num).split("-")[1]))