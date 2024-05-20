N = int(input("Enter the number of elements of the sequence:"))
prev_seq1 = 0
prev_seq2 = 0
for i in range(N):
    if i == 0:
        next_seq = 0
    elif i == 1:
        prev_seq1 = next_seq
        next_seq = 1
    else:
        prev_seq2 = prev_seq1
        prev_seq1 = next_seq
        next_seq = prev_seq1 + prev_seq2
    print(next_seq, end = " ")