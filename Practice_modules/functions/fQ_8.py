def compress_string(string):
    uc_str = string
    size = len(uc_str)
    c_str = ""
    count = 1
    for i in range(size-1):
        if uc_str[i] == uc_str[i+1]:
            count = count + 1
        else:
            c_str = c_str + uc_str[i] + str(count)
            count = 1
        
    if uc_str[size-1] != uc_str[size-2]:
        c_str = c_str + uc_str[size-1] + "1"
    else:
        c_str = c_str + uc_str[size-1] + str(count)
    return c_str

in1 = "AABBBCDDDD"
out1 = compress_string(in1)
print(out1)
in2 = "ABCDDDDD"
out2 = compress_string(in2)
print(out2)
in3 = "AABBBCD"
out3 = compress_string(in3)
print(out3)
            