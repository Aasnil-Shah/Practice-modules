str1 = "PYnative"
r_str1 = ""
strlen = len(str1)
for i in range(strlen):
    r_str1 = r_str1 + str1[strlen - i - 1]

print(r_str1)