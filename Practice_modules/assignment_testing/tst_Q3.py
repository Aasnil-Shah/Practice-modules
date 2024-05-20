str1 = "listen"
str2 = "silent"
#str1 = "read"
#str2 = "dear"
len1 = len(str1)
len2 = len(str2)
if len1 == len2:
    cnt1 = 0
    cnt_set1 = {}
    for i in range(len1):
        cnt1 = 0
        for j in range(len1):
                if str1[i] == str1[j]:
                    cnt1 = cnt1 + 1
                    cnt_set1[str1[i]] = cnt1
    cnt2 = 0
    cnt_set2 = {}
    for i in range(len2):
        cnt2 = 0
        for j in range(len2):
                if str2[i] == str2[j]:
                    cnt2 = cnt2 + 1
                    cnt_set2[str2[i]] = cnt2
    if cnt_set1 == cnt_set2:
        print("The strings are an anagram")
    else:
         print("Strings are not anagram")
else:
    print("Enter strings of equal length")