speed = {'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'aug':44,'sep':54}
list1 = []
final_lst = []
for label1 in speed:
    val1 = speed.get(label1)
    list1.append(val1)
list1 = list(dict.fromkeys(list1))
print(list1)