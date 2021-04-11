def partition(A, begin, end):

    # Complexity: Θ(n)

    assert end - begin > 1

    # pick a pivot element: deterministically A[end-1]
    pivot = A[end - 1]
    q = begin

    for i in range(begin, end-1):
        if A[i] < pivot:
            A[i], A[q] = A[q], A[i]
            q += 1
        
    A[end-1], A[q] = A[q], A[end-1]
    return q

def quick_sort(A, begin, end):

    # Worst case: q = begin or q = end - Θ(n^2)
    # Best case: q = [n/2] - Θ(n logn)

    if end - begin >= 2:
        q = partition(A, begin, end)
        quick_sort(A, begin, q)
        quick_sort(A, q+1, end)
