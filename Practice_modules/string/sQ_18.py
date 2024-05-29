str1 = "/*Jon is a @developer & musician!"
spl_chr = ["/","*","@","&","!"]
for i in spl_chr:
    str1 = str1.replace(i," ")
print(str1)