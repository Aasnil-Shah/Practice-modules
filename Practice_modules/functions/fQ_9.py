def transpose(a):
    matrix = a
    tp_matrix = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            tp_matrix[j][i] = matrix[i][j]
    return tp_matrix

in1 =  [[1,2,3], [4,5,6], [7,8,9]]
out1 = transpose(in1) 
print(out1)
in2 =  [['A','B','C'], ['P','Q','R'], ['X','Y','Z']]
out2 = transpose(in2) 
print(out2)