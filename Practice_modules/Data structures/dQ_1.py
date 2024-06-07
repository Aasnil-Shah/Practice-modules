'''Given a two list. Create a third list by picking an odd-index element from the first
list and even index elements from the second list'''

listone = [3,6,9,12,15,18,21]
listtwo = [4,8,12,16,20,24,28]
print("Elements with odd number of index in list one:\n",listone[1::2])
print("Elements with even number of index in list two:\n",listtwo[::2])
print("Printing the final third list:\n", listone[1::2]+listtwo[::2])