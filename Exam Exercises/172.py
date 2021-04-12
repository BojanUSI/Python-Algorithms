def algo_x(A):
    B = [None] * len(A)
    for i in range(0, len(A)):
        B[i] = A[i]

    i = 0
    x = 1
    while i < len(A):
        B[i] = B[i] - 1
        if B[i] == 0:
            B[i] = A[i]
            i += 1
        else:
            x += 1
            i = 1
    
    return x



def better_algo_x(A):
    m = 1
    for a in A:
        m *= a

    return m