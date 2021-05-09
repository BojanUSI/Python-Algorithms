def algo_x(A):
    for i in range(2, len(A)):
        for j in range(1, i-1):
            for k in range(0, j-1):
                if abs(A[i] - A[j]) == abs(A[j]- A[k])  or \
                abs(A[i] - A[k]) == abs(A[k]-A[j]) or \
                abs(A[k] - A[i]) == abs(A[i]-A[j]):
                    return True

    return False