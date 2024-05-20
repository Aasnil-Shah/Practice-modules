def minmax(a):
    list_a = a
    mn_mx = [2^63-1,-(2^63)] 
    for i in list_a:
        if i < mn_mx[0]:
            mn_mx[0] = i
        if i > mn_mx[1]:
            mn_mx[1] = i
    return mn_mx

lst = [1,3,3,1111,1,134]
ans = minmax(lst)
print("minimum no in list is:",ans[0])
print("maximum no in list is:",ans[1])