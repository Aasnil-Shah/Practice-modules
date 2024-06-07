'''Remove duplicate from a list and create a tuple and find the minimum and
maximum number'''

list1 = [87,45,41,65,94,41,99,94]
uq_list = list(set(list1))
print("unique items:", uq_list)
print("Maximum value in the list:", max(uq_list))
print("Minimum value in the list:", min(uq_list))