def partition(A, v):

    pivot = v
    q = 0

    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[q] = A[q], A[i]
            q += 1
        
    pivot, A[q] = A[q], pivot
    
    return partition_equal(A,v,q)

def partition_equal(A, v, q):
    t = q + 1
    for i in range(q+1, len(A)):
        if A[i] == v:
            A[t], A[i] = A[i], A[t]
            t += 1
    
    return A

