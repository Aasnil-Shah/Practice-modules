def minmax(a):
    min_val = max_val = a[0]
    for i in a[1:]:
        if i < min_val:
            min_val = i
        if i > max_val:
            max_val = i
    return min_val,max_val

lst = [1,3,3,1111,1,134]
ans = minmax(lst)
print("minimum no in list is:",ans[0])
print("maximum no in list is:",ans[1])