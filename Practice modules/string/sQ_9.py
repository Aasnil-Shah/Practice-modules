str1 = "English = 78 Science = 83 Math = 68 History = 65"
strlen = len(str1)
sum = 0
cnt_num = 0
num = ""
for i in range(strlen-1):
    if str1[i].isdigit():
        if str1[i+1] == " ":
            num = num + str1[i]
            sum = sum + int(num)
            num = ""
            cnt_num = cnt_num + 1
        else:
            num = num + str1[i]
if str1[strlen-1].isdigit():
    num = num + str1[strlen-1]
    sum = sum + int(num)
    cnt_num = cnt_num + 1

print("The sum of digits in string is:", sum)
print("The average of digits in string is:", sum/cnt_num)