'''Remove empty strings from a list of strings.'''

str_list = ["Emma","Jon","","Kelly",None,"Eric",""]
for i in str_list:
    if not i:
        str_list.remove(i)
print(str_list)