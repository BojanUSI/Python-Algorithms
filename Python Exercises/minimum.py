def minimum(A):
    min_check = A[0]
    for a in A:
        if a < min_check:
            min_check = a
    
    return min_check