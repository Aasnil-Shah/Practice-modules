#str1 = "JohnDipPeta"
str1 = "JaSonAy"
strlen = len(str1)
if strlen > 6:
    index = int((strlen-1)/2)
    out_str = str1[index-1] + str1[index] + str1[index+1]
    print(out_str)
else:
    print("Enter a string of length > 6")