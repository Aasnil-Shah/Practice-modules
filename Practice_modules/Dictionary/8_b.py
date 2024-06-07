'''Exercise 8-b: Editing Python Dictionaries
Change Plato's birth year from B.C. 427 to B.C. 428'''

dict1 = {"name":"Plato","country":"Ancient Greece","born":-427,"teacher":"Socrates","student":"Aristotle"}
dict1["born"] = -428
print(dict1["born"])