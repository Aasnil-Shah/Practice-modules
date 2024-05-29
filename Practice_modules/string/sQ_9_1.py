str1 = "English = 78 Science = 83 Math = 68 History = 65"
sum = 0
cnt = 0
strlist = str1.split(sep=" ")
for i in strlist:
    if i.isdigit():
        sum += int(i)
        cnt += 1
    else:
        pass

print("The sum of digits in string is:", sum)
print("The average of digits in string is:", sum/cnt)