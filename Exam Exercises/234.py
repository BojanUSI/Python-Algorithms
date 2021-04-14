def lower_bound(A, x):
    if x > A[len(A)-1]:
        return "Not-Found"
    
    b = 0
    e = len(A)
    while b < e:
        m = (b+e) // 2
        if A[m] >= x:
            e = m
        else:
            b = m + 1
    
    return A[e]
