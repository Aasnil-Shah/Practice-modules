'''Find all occurrences of “USA” in given string ignoring the case.'''

str1 = "Welcome to USA. usa is awesome, isn't it! usa USA!! USA!!!!!"

cnt = 0
cnt = str1.lower().count("usa") #+ str1.count("USA")
print("The USA count is:",cnt)