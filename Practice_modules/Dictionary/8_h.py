'''Exercise 8-h: Clear method to remove everything from a dictionary
Since dictionaries are mutable, they have some methods that tuples
don't have.
.clear() is one of them and it clears the whole dictionary'''

dict = {"son's name:":"Lucas", "son's eyes:":"green","son's height:":32,"son's weight:":25}

dict.clear()
print(dict)