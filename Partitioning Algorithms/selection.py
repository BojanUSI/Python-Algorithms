def selection(A, k):
    v = A[len(A) // 2]
    Al = []
    Ar = []
    Av = []
    for i in range(len(A)):
        if A[i] < v:
            Al.append(A[i])
        elif A[i] == v:
            Av.append(A[i])
        else:
            Ar.append(A[i])
    
    if k <= len(Al):
        return selection(Al, k)
    elif k > len(Al) + len(Av):
        return selection(Ar, k - len(Al) - len(Av))
    else:
        return v