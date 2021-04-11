def maximal_difference(A):
    min_A = A[0]
    max_A = A[0]
    for i in range(len(A)):
        if A[i] > max_A:
            max_A = A[i]
        elif A[i] < min_A:
            min_A = A[i]

    return abs(max_A - min_A)
