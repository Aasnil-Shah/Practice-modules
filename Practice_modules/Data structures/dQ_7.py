'''Given a dictionary get all values from the dictionary and add it in a list but don’t
add duplicates'''

speed = {'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'aug':44,'sep':54}
speed_val = speed.values()  #list1 = (dict.fromkeys(speed))
list1 = list(set(speed_val))
print(list1)