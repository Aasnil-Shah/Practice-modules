str_list = ["Emma","Jon","","Kelly",None,"Eric",""]
lst_len = len(str_list)
for i in range(lst_len-1):
    if str_list[i] == "":
        del str_list[i]
print(str_list)