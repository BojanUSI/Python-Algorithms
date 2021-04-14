def partition_zero(A):
    j = 0
    for i in range(len(A)):
        if A[i] < 0:
            A[i], A[j] = A[j], A[i]
            j += 1
    
    i = j
    for i in range(len(A)):
        if A[i] == 0:
            A[i], A[j] = A[j], A[i]
            j += 1


