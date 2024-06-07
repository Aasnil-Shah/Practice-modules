'''Find the last position of a substring “Emma” in a given string'''

str1 = "Emma is a data scientist who knows Python. Emma works at google." 
indx = str1.rindex("Emma")
print("Last occurence of Emma starts at:", indx)
#rfind returns -1 if not found rindex returns error