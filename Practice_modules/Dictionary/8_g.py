'''Exercise 8-g: Get Method of Dictionaries for Sophisticated Value Calling
.get() method can be used just to get the value of a key. But it has more
tricks up its sleeve. Try to look for key: "son's age" and if nothing comes up make the .get()
return "2".'''

dict = {"son's name:":"Lucas", "son's eyes:":"green","son's height:":32,"son's weight:":25}
print(dict.get("son's age:",2))