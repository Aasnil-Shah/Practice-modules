'''Given a two list of equal size create a set such that it shows the element from
both lists in the pair'''

list1 = [2,3,4,5,6,7,8]
list2 = [4,9,16,25,36,49,64]
set1 = set(zip(list1,list2))
print(set1)