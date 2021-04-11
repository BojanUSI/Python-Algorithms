def bubble_sort(A):
    # Average case: Θ(n^2)
    for i in range(len(A)):
        for j in range(0, len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]