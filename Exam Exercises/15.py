def partition_even_odd(A):
    j = 0
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            j += 1
    
    return A