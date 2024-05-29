#str1 = "JohnDipPeta"
str1 = "JaSonAya"
strlen = len(str1)
if (strlen > 7) and (strlen % 2 == 1):
    index = int((strlen-1)/2)
    out_str = str1[index-1:index+2] 
    print(out_str)
else:
    print("Enter a odd length string of length > 7")