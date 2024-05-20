str1 = "Emma-is-a-data-scientist"
strlen = len(str1)
sub_str = ""
for i in range(strlen):
    if str1[i] == "-":
        print(sub_str)
        sub_str = ""
    else:
        sub_str = sub_str + str1[i]
print(sub_str)