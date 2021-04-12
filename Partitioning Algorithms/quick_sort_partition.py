def partition(A, begin, end):
    assert end - begin > 1

    # pick a pivot element: deterministically A[end-1]
    pivot = A[end - 1]
    q = begin

    for i in range(begin, end-1):
        if A[i] < pivot:
            A[i], A[q] = A[q], A[i]
            q += 1
        

    return q