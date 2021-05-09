def algo_x(A, k):
    B = algo_y(A,1,len(A)+1)
    c = 0
    for i in range(len(B)):
        if i <= k:
            c = c + B[i]
        else:
            return c
    
    return c

def algo_y(A,i,j):
    D = []
    if j - i == 1:
        D.append(A[i])
    elif j - i > 1:
        k = (i+j) // 2
        B = algo_y(A,i,k)
        C = algo_y(A,k,j)
        b = i
        c = k
        while b < k or c < j:
            if c >= j or (b < k and B[b] < C[c]):
                D.append(B[b])
                b += 1
            else:
                D.append(C[c])
                c += 1
    
    return D