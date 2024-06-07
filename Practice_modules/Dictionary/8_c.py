'''Exercise 8-c: Adding a List to Python Dictionary (Nested Data)
Dictionaries can have nested data too. Also, you can add a new key to a
dictionary as they are mutable (changeable). Try to add the key "work"
to dict with values shown below. "work": ["Apology", "Phaedo", "Republic", "Symposium"]'''

dict1 = {"name":"Plato","country":"Ancient Greece","born":-427,"teacher":"Socrates","student":"Aristotle"}
dict1["work"] =  ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict1)