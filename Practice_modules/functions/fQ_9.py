def transpose(a):
    out_t_a = []
    t_a = zip(*a)
    for element in t_a:
        out_t_a.append(element)
    return out_t_a

in1 =  [[1,2,3], [4,5,6], [7,8,9]]
out1 = transpose(in1) 
print(out1)
in2 =  [['A','B','C'], ['P','Q','R'], ['X','Y','Z']]
out2 = transpose(in2) 
print(out2)