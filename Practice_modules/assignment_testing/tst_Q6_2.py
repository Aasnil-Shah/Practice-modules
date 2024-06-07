'''Write a program which can accept a number and return the nearest palindrome
number. Input: 123000
Output: 123321'''

#num1 = input("Enter a non-single digit positive number you want to find the nearest palindrome for:")
num1 = "123000"
num_len = len(num1)
if num_len == 1:
    print(int(num1)-1)
else:
    pl_list = [0,0,0]
    if num_len % 2 == 0:
        mid = int(num_len/2)
        pl_list[0] = num1[:mid] + num1[:mid][::-1]
        pl_list[1] = str(int(num1[:mid])+1) + str(int(num1[:mid])+1)[::-1]
        pl_list[2] = str(int(num1[:mid])-1) + str(int(num1[:mid])-1)[::-1]
    else:
        mid = int(num_len/2) + 1
        pl_list[0] = num1[:mid] + num1[:mid-1][::-1]
        pl_list[1] = str(int(num1[:mid])+1) + str(int(num1[:mid-1]))[::-1]
        pl_list[2] = str(int(num1[:mid])-1) + str(int(num1[:mid-1]))[::-1]
    difflist = [abs(int(num1)-int(pl_list[0])),abs(int(num1)-int(pl_list[1])),abs(int(num1)-int(pl_list[2]))]
    pl = [pl_list[i] for i in range(len(difflist)) if difflist[i]==min(difflist)]
    print(pl[0])