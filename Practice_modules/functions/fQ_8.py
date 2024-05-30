def compress_string(string1):
    c_str = ""
    c_dict = {}
    for substring in string1:
        c_dict[substring] = string1.count(substring)
    for char in c_dict.keys():
        c_str += char + str(c_dict[char])
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
            